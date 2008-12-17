from django.contrib import admin
from publicmarkup.legislation.models import Resource, Legislation, Title, Section
    
class LegislationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
class SectionInline(admin.TabularInline):
    model = Section
    extra = 5
    
class TitleAdmin(admin.ModelAdmin):
    inlines = [SectionInline,]
    
admin.site.register(Resource)
admin.site.register(Legislation, LegislationAdmin)
admin.site.register(Title, TitleAdmin)