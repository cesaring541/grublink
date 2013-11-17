#coding=utf-8
# Create your views here.


from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from infelcom.models import Section, Slide, Aspect, Content
import re

from django.utils import translation

def logout(request):
	del request.session['user']
	return HttpResponseRedirect("/infelcom")

def load_admin(request):
	request.session['user']='admin'
	return HttpResponseRedirect("/infelcom")

def home(request):

	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	slides=Slide.objects.all().order_by('slide_index')
	slides_pagers=range(1,len(slides)+1)
	aspects= Aspect.objects.all().order_by('index')

	return render_to_response ('infelcom-index.html', 
							  	{'sections':sections, 
							  	 'slides':slides, 
							  	 'slides_pagers':slides_pagers,
							  	 'aspects':aspects
							  	}, context_instance=RequestContext(request))

def add_section(request):

	print "holaaaa"

	name=request.POST.get('section_name')
	title=request.POST.get('section_title')
	language=str(request.LANGUAGE_CODE)
	next_index=int(request.POST.get('section_index'))

	new_section=Section(section_name=name, section_title=title, section_lang=language, section_author=request.session.get('user'), section_index=next_index)

	new_section.save()
	new_content=Content(section_id=new_section, text="No se ha definido contenido para esta sección")

	return HttpResponseRedirect("/infelcom")

def update_sections(request):
	data=request.POST.get('data')

	rows=data.split(';')

	for row in rows:
		fields=row.split(',')
		section=Section.objects.get(id=fields[0])
		section.section_name=fields[1]
		section.section_title=fields[2]
		section.section_index=fields[3]
		section.save()

	return HttpResponseRedirect("/infelcom")


def delete_section(request, identification):
	section = Section.objects.get(id=identification)
	section.delete()
	return HttpResponseRedirect("/infelcom")

def add_slide(request):
	name=request.POST.get('name')
	title=request.POST.get('title')
	abstract=request.POST.get('abstract')
	link=request.POST.get('link')

	bg=request.FILES.get('bg')
	icon=request.FILES.get('icon')
	index=request.POST.get('index')


	print(bg,icon)


	new_slide=Slide(slide_name=name, 
		slide_title=title, slide_abstract=abstract, slide_lang=request.LANGUAGE_CODE, 
		slide_author=request.session['user'],
		slide_link=link, slide_bg=bg, slide_icon=icon, slide_index=int(index))


	print(new_slide.slide_bg)

	new_slide.save()
	return HttpResponseRedirect("/infelcom")

def update_slide(request):

	id=request.POST.get('id')
	name=request.POST.get('name')
	title=request.POST.get('title')
	abstract=request.POST.get('abstract')
	link=request.POST.get('link')
	bg=request.FILES.get('bg')
	icon=request.FILES.get('icon')
	index=request.POST.get('index')

	slide=Slide.objects.get(id=id)

	slide.slide_name=name
	slide.slide_title=title
	slide.slide_abstract=abstract
	slide.slide_link=link
	slide.slide_bg=bg if bg else slide.slide_bg
	slide.slide_icon=icon if icon else slide.slide_icon
	slide.slide_index=int(index)

	slide.save()

	return HttpResponseRedirect("/infelcom")

def delete_slide(request, identification):
	
	slide = Slide.objects.get(id=identification)
	slide.delete()
	return HttpResponseRedirect("/")


def add_aspect(request):
	title=request.POST.get('title')
	icon_name=request.POST.get('icon')
	index=request.POST.get('index')
	content=request.POST.get('content')

	content = re.sub(r'style=".*"', "", content,0)

	new_aspect=Aspect(
		title=title, lang=request.LANGUAGE_CODE, 
		icon_name=icon_name, index=int(index), content=content)


	# print(new_slide.slide_bg)

	new_aspect.save()

	return HttpResponseRedirect("/infelcom")

def update_aspect(request):
	id=request.POST.get('id')
	title=request.POST.get('title')
	icon_name=request.POST.get('icon')
	index=request.POST.get('index')
	content=request.POST.get('content')


	content = re.sub(r'style=".*"', "", content,0)

	print "ajajajajjaa",content

	aspect=Aspect.objects.get(id=id)

	aspect.title=title
	aspect.icon_name=icon_name
	aspect.index=index
	aspect.content=content
	



	# print(new_slide.slide_bg)

	aspect.save()

	return HttpResponseRedirect("/infelcom")

def delete_slide(request, identification):
	
	aspect = Aspect.objects.get(id=identification)
	aspect.delete()
	return HttpResponseRedirect("/infelcom")