from django.conf import settings
from django.contrib.comments.models import FreeComment
from django.db import models
import roman

class Resource(models.Model):
    name = models.CharField(max_length=128, unique=True)
    value = models.TextField()
    def __unicode__(self):
        return self.name

class Legislation(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.TextField(blank=True, null=True)
    allow_comments = models.BooleanField(default=True)
    def get_absolute_url(self):
        return "/bill/%s/" % (self.slug)
    def get_sections_comment_count(self):
        sections = Section.objects.filter(title__legislation=self)
        section_ids = [section.id for section in sections]
        comment_count = FreeComment.objects.filter(object_id__in=section_ids,
            content_type__app_label__exact="legislation",
            content_type__model__exact="section", site__id__exact=settings.SITE_ID).count()
        return comment_count
    def __unicode__(self):
        return self.name
    
class Title(models.Model):
    legislation = models.ForeignKey(Legislation, related_name="titles")
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    extra_content = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ['number','name']
    def roman_number(self):
        return roman.toRoman(self.number)
    def get_absolute_url(self):
        return "/bill/%s/%i/" % (self.legislation.slug, self.number)
    def get_sections_comment_count(self):
        section_ids = [section.id for section in self.sections.all]
        comment_count = FreeComment.objects.filter(object_id__in=section_ids,
            content_type__app_label__exact="legislation",
            content_type__model__exact="section", site__id__exact=settings.SITE_ID).count()
        return comment_count
    def __unicode__(self):
        return "TITLE %s - %s" % (roman.toRoman(self.number), self.name)

class Section(models.Model):
    title = models.ForeignKey(Title, related_name="sections")
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)
    text = models.TextField()
    class Meta:
        ordering = ['number','name']
    def get_absolute_url(self):
        return "/bill/%s/%i/%i/" % (self.title.legislation.slug, self.title.number, self.number)
    def __unicode__(self):
        return "Sec. %i. %s" % (self.number, self.name)