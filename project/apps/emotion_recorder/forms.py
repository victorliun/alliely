from django import forms

from .models import Emotions


class EmotionForm(forms.ModelForm):
    """Form for Emotions models"""
    
    description = forms.CharField(max_length=255, widget=forms.Textarea)
    

"""
    def clean_newsletter_tags(self):
        
        clean newsletter_tags field
        
        if self.cleaned_data.get('newsletter_tags', '').find('_'):

            raise ValidationError("Multiple tags must be separated by comma, invalid domains")

        return self.cleaned_data.get('newsletter_tags', '')
"""        
    class Meta:
        model = Emotions
        fields = ("description",)