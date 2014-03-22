from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from lxml import etree

class Emotions(models.Model):
    """Table of emotions, for recording emotions that user posted"""
    
    slug = models.SlugField()
    pub_date = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, related_name='emotions_author')
    #xml_path = models.CharField(blank=True, null=True)
    description = models.TextField()
    lastest = models.BooleanField(default=True)

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ('-pub_date',)
        verbose_name_plural = 'emotions'
        app_label = 'emotion_recorder'
        db_table = 'emotions'
        managed = True

    def __unicode__(self):
        return u"%s posted '%s' at %s" %(self.author, self.description,
            self.pub_date.strftime("%Y-%b-%d"))

    def get_absolute_url(self):
        return "/er/%s/%s" %(self.pub_date.strftime("%Y/%b/%d"), self.slug)

    def read_archived_post(self, time_stamp=None, count=10):
       	"""Return the lastest posts"""

        pass

    def save(self, **kwargs):
        """Save emotions"""

        Emotions.objects.filter(author=self.author, lastest=True).update(lastest=False)
        super(Emotions, self).save(**kwargs)

