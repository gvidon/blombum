from django.contrib.auth.models import User
from django.utils.translation   import ugettext_lazy as _
from django.db                  import models


class Nonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=40)

    def __unicode__(self):
        return u"Nonce: %s, %s" % (self.id, self.server_url)

class Association(models.Model):
    server_url = models.TextField(max_length=2047)
    handle = models.CharField(max_length=255)
    secret = models.TextField(max_length=255) # Stored base64 encoded
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField(max_length=64)

    def __unicode__(self):
        return "Association: %s, %s" % (self.server_url, self.handle)


class UserAssociation(models.Model):
    openid_url = models.CharField(blank=False, max_length=255)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return "Openid %s with user %s" % (self.openid_url, self.user)
    
    class Meta:
        verbose_name        = _('User openid association')
        verbose_name_plural = _('User openid associations')
