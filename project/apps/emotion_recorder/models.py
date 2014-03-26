from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models
from django.db.models.query import QuerySet
from django.db.models import permalink

from lxml import etree

import re
import unidecode

def slugify(desc):
    str = unidecode.unidecode(desc).lower()
    return re.sub(r'\W+','-',desc)

def today():
    now = datetime.now()
    start = datetime.min.replace(year=now.year, month=now.month, day=now.day)
    end = (start + timedelta(days=1)) - timedelta.resolution
    return (start, end)

class EmotionQuerySet(QuerySet):
    def today(self):
        return self.filter(pub_date__range=today())

class EmotionManager(models.Manager):
    """docstring for EmotionManager"""
    def get_query_set(self):
        return EmotionQuerySet(self.model)
    
    def today(self):
        self.get_query_set().today()


class Emotions(models.Model):
    """Table of emotions, for recording emotions that user posted"""
    
    slug = models.SlugField(max_length=255, blank=True, null=True)
    pub_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, related_name='emotions_author')
    #xml_path = models.CharField(blank=True, null=True)
    description = models.TextField()
    latest = models.BooleanField(default=True)

    objects = EmotionManager()

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ('-pub_date',)
        verbose_name_plural = 'Emotion'
        app_label = 'emotion_recorder'
        db_table = 'emotions'
        managed = True

    def __unicode__(self):
        return u"%s posted '%s' at %s" %(self.author, self.description,
            self.pub_date.strftime("%Y-%b-%d"))

    @permalink
    def get_absolute_url(self):
        return ("emotion_recorder_view", None, {'slug': self.slug})

    def read_archived_post(self, time_stamp=None, count=10):
       	"""Return the latest posts"""

        pass

    def save(self, **kwargs):
        """Save emotions"""
        #auto generate slug field
        self.slug = slugify(self.description)

        Emotions.objects.filter(author=self.author, latest=True).update(latest=False)
        super(Emotions, self).save(**kwargs)

    def todays_emotions(self):

        return Emotions.objects.today()

