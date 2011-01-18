from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.comments.views.comments import post_comment
from django.http import Http404, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.generic.list_detail import object_list
from humanity.forms import HumanityForm
from publicmarkup.legislation.models import Legislation, Title, Section

def index(*args, **kwargs):
    return object_list(*args, **kwargs)

def bill(request):
    legislation = Legislation.objects.get(pk=1)
    return HttpResponseRedirect(legislation.get_absolute_url())

def legislation_print(request, legislation_slug):
    legislation = Legislation.objects.get(slug=legislation_slug)
    return render_to_response("legislation/legislation_print.html", locals())

def legislation_detail(request, legislation_slug):
    
    try:
        legislation = Legislation.objects.get(slug=legislation_slug)
    except Legislation.DoesNotExist:
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        human_form = HumanityForm(request.POST, label_suffix='')
        is_human = request.POST.get('humanity', 'robot') == 'human'
        if is_human or human_form.is_valid():
            return post_comment(request)
    else:
        human_form = HumanityForm(label_suffix='')
    
    data = {
        'legislation': legislation,
        'human_form': human_form,
    }
    
    return render_to_response("legislation/legislation_detail.html", data,
                              context_instance=RequestContext(request))

def title_detail(request, legislation_slug, title_num):
    title = Title.objects.get(number=title_num, legislation__slug=legislation_slug)
    return render_to_response("legislation/title_detail.html", locals(),
                              context_instance=RequestContext(request))
    
def section_detail(request, legislation_slug, title_num, section_num):
    human_form = HumanityForm(label_suffix='')
    section_num = int(section_num)
    section = Section.objects.get(number=section_num, title__number=title_num, title__legislation__slug=legislation_slug)
    try:
        next_section = Section.objects.get(number=section_num + 1, title__number=title_num, title__legislation__slug=legislation_slug)
    except Section.DoesNotExist:
        next_section = None
    try:
        previous_section = Section.objects.get(number=section_num - 1, title__number=title_num, title__legislation__slug=legislation_slug)
    except Section.DoesNotExist:
        previous_section = None
    data = {
        "section": section,
        "next_section": next_section,
        "previous_section": previous_section,
        'human_form': human_form,
    }
    return render_to_response("legislation/section_detail.html", data,
                              context_instance=RequestContext(request))

def save_comment(request):
    if request.POST:
        human_form = HumanityForm(request.POST)
        if human_form.is_valid():
            return post_comment(request)
    else:
        raise Http404, "All you do is GET, GET, GET. How about you POST every once in a while like you used to at the beginning of our relationship?"

def save_free_comment(request):
    
    if request.POST:
        
        target = request.POST.get("target", None)
        
        if target:
            
            (ct_id, obj_id) = target.split(":")
        
            user_type = ContentType.objects.get(id=ct_id)
            
            if user_type.model == "section":
                section = Section.objects.get(pk=obj_id)
                legislation = section.title.legislation
            elif user_type.model == "legislation":
                legislation = Legislation.objects.get(pk=obj_id)
            else:
                legislation = None
        
            if legislation and legislation.allow_comments:
        
                return post_comment(request, extra_context)
                
            else:
                
                raise Http404, "Sorry, comments are not allowed on this legislation."
    
    else:
    
        raise Http404, "All you do is GET, GET, GET. How about you POST every once in a while like you used to at the beginning of our relationship?"
        
    return HttpResponseServerError("DENIED! Not really, something just broke.")