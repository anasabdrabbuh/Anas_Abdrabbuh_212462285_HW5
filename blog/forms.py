from django import forms
from .models import BLOGS

class BLOGForm(forms.ModelForm):

    class Meta:
        model = BLOGS
        fields = ["name", "description", "tags"]