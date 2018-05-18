from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib import admin
from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

from .models import Polls

class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = FlatPage
        fields = '__all__'


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = FlatPageForm

class PollsForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Polls
        fields = '__all__'
        #fields = ('name',)


class PollsAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PollsForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
#admin.site.register(Polls, PollsAdmin)
