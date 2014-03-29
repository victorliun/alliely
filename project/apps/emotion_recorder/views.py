# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Emotions
from .forms import EmotionForm

class EmotionRecorderView(TemplateView):
    "view for homepage"
    
    template_name = "emotion_recorder/emotion_recorder.html"
    
    def get_context_data(self, **kwargs):
        """Populate all context of the template with all setting configures"""
        
        context = super(EmotionRecorderView, self).get_context_data(**kwargs)
        context.update({'STATIC_URL':settings.STATIC_URL})
        context['emotions'] = Emotions.objects.filter(latest=True)
        return context

emotion_recorder_view = EmotionRecorderView.as_view()


class EmotionCreateView(CreateView):
    """docstring for EmotionCreateView"""
    template_name = "emotion_recorder/emotion_recorder_form.html"
    form_class = EmotionForm
    success_url = "/er/"

    def get_success_url(self):
        return self.request.POST.get("next", reverse("emotion_recorder"))

    def form_valid(self, form):
        emotion = form.save(commit=False)
        emotion.author = self.request.user
        emotion.save()

        return super(EmotionCreateView, self).form_valid(form)


emotion_create_view = login_required(EmotionCreateView.as_view())
