import re

from django.utils.translation import ugettext_lazy as _
from django                   import forms
from models                   import StaticPage

class StaticPageAdminForm(forms.ModelForm):
	class Meta:
		model = StaticPage
	
	def clean_url(self):
		if not re.match('^[a-zA-Z\d\-]+$', self.cleaned_data['url']):
			raise forms.ValidationError(_(u'You can use only latin characters, digits and "-" here'))
		
		return self.cleaned_data['url']
