# -*- mode: python; coding: utf-8; -*-
from django.contrib      import admin
from django.conf         import settings

from crossposting.models import Crosspost, SideService
from lib.libadmin        import BFAdmin

class SideServiceAdmin(admin.ModelAdmin):
	list_display        = ('name', 'url', 'login', 'type')
	search_fields       = ('name', 'url', 'login', 'type')
	list_filter         = ('name', 'url', 'login', 'type')

class CrosspostAdmin(admin.ModelAdmin):
	list_display = ('post', 'service')

admin.site.register(Crosspost, CrosspostAdmin)
admin.site.register(SideService, SideServiceAdmin)

class BFPostAdmin(BFAdmin):
    """
    Класс для замены метода PostForm.save(). Единственный момент где
    можно перехватить пост с уже обновленной связью crossposting_que (в джанге 1.2
    для этого есть сигнал post_save_m2m)
    """

    def get_form(self, request, obj=None, **kwargs):
        import hashlib, httplib, json, random, re, subprocess, sys
        
        from django.forms import ValidationError
        from django.db    import IntegrityError
        
        # проверить доступность сервера блогрессора
        # и если он выключен - написать на форме, что в
        # данный момент кросспостинг не доступен
        def pingup_blogressor(self):
            
            if not self.cleaned_data['crossposting_que']:
                return self.cleaned_data['crossposting_que']
            
            try:
                B = httplib.HTTPConnection(settings.BLOGRESSOR_HOST, timeout=2)
                B.request('POST', '/', '[]')
                B.close()
                
                return self.cleaned_data['crossposting_que']
            except:
                raise ValidationError(
                    u'Sorry but crossposting is not available now.'+
                    'You can save your post and try later. (' + sys.exc_info()[0] + ')')
        
        form = super(BFPostAdmin, self).get_form(request, obj, **kwargs)
        form.clean_crossposting_que = pingup_blogressor
            
        original = form.save
        
        # после сохранения поста собрать претендентов из crossposting_que,
        # записать в crosspost и запустить процесс кросспостинга
        def save_m2m(self, commit):
            md5hash = hashlib.md5()
            params  = []
            post    = original(self, commit)
            
            #построить структуру параметров блогрессора для каждого кросспоста
            for service in self.cleaned_data['crossposting_que']:
                
                code = None
                
                # сгенерирую уникальный в пределах таблицы код для каждого краулера
                while not locals().get('code'):
                    try:
                        code = Crosspost.objects.create(
                            service = service,
                            post    = post,
                            code    = md5hash.hexdigest()
                        ).code
                        
                    except IntegrityError:
                        md5hash.update(str(random.random()*50))
                
                params.append({
                    'crawler' : service.type,
                    'security': code,
                    'catcher' : request.META['HTTP_HOST'],
                    
                    'params'  : dict(map(lambda N: (N, service.__getattribute__(N)),
                        ('login', 'email', 'password') +
                        { 'blogger': ('blogid',) }.get(service.type, ())
                    ) + [
                        ('body', self.cleaned_data['text']), ('tags', self.cleaned_data['tags'])
                    ]),
                })
            
            # отправить JSON блогрессору и очистить очередь
            try:
                B = httplib.HTTPConnection(settings.BLOGRESSOR_HOST, timeout=2)
                
                B.request('POST', '/', re.sub('(\r\n|&nbsp;)', '', json.dumps(params)))
                B.close()
                
                self.cleaned_data['crossposting_que'] = []
                
            except:
                Crosspost.objects.filter(code__in=[P['security'] for P in params]).delete()
            
            return post
        
        form.save = save_m2m
        
        return form
