from django.conf import settings
from django.contrib.syndication.feeds import Feed
from django.contrib.comments.models import FreeComment
from django.db.models import Q
from publicmarkup.legislation.models import Legislation, Section, Title
        
class LegislationComments(Feed):
    title_template = "feeds/title.html"
    description_template = "feeds/description.html"
    
    def get_object(self, bits):
        if len(bits) < 1:
            raise ObjectDoesNotExist
        legislation_slug = bits[-1]
        return Legislation.objects.get(slug=legislation_slug)
        
    def title(self, obj):
        return "PublicMarkup.org %s comments" % obj.name
        
    def description(self, obj):
        return "Latest comments on %s" % obj.name
        
    def link(self, obj):
        return obj.get_absolute_url()
        
    def items(self, obj):
        
        sections = Section.objects.filter(title__legislation=obj)
        section_ids = [section.id for section in sections]
        
        comments = FreeComment.objects.filter(object_id__in=section_ids, content_type__app_label__exact="legislation", content_type__model__exact="section", site__id__exact=settings.SITE_ID) | FreeComment.objects.filter(object_id=obj.id, content_type__app_label__exact="legislation", content_type__model__exact="legislation", site__id__exact=settings.SITE_ID)
        comments = comments.order_by("-submit_date")[:10]
        
        return comments
        
    def item_link(self, obj):
        return "%s#comment_%s" % (obj.get_content_object().get_absolute_url(), obj.id)
        
    def item_author_name(self, obj):
        return obj.person_name
        
    def item_pubdate(self, obj):
        return obj.submit_date