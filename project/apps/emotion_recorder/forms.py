from django import forms

from .models import Emotions


class EmotionForm(forms.ModelForm):

    description = forms.CharField(max_length=255, widget=forms.Textarea)
    
    class Meta:
        model = Emotions
        fields = ("description",)