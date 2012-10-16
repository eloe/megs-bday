from django.forms import ModelForm, Textarea
from core.models import *

class GuestbookEntryForm(ModelForm):
    class Meta:
        model = GuestbookEntry
        fields = ('name', 'message')
        widgets = {
            'name'   : Textarea(attrs={'cols': 80, 'rows': 1}),
            'message': Textarea(attrs={'cols': 80, 'rows': 10}),
        }