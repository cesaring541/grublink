# Create your views here.


from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from main.models import Section,Slide

from django.utils import translation

def load_admin(request):
	request.session['user']='admin'
	return HttpResponseRedirect("/")

def home(request):
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	slides=Slide.objects.all().order_by('slide_index')
	slides_pagers=range(1,len(slides)+1)

	return render_to_response ('index.html', {'sections':sections, 'slides':slides, 'slides_pagers':slides_pagers}, context_instance=RequestContext(request))

def add_section(request):


	name=request.POST.get('section_name')
	title=request.POST.get('section_title')
	language=str(request.LANGUAGE_CODE)
	next_index=int(request.POST.get('section_index'))

	new_section=Section(section_name=name, section_title=title, section_lang=language, section_author=request.session.get('user'), section_index=next_index)

	new_section.save()

	return HttpResponseRedirect("/")

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

	return HttpResponseRedirect("/")


def delete_section(request, identification):
	
	section = Section.objects.get(id=identification)
	section.delete()
	return HttpResponseRedirect("/")

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
	return HttpResponseRedirect("/")

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

	return HttpResponseRedirect("/")

def delete_slide(request, identification):
	
	slide = Slide.objects.get(id=identification)
	slide.delete()
	return HttpResponseRedirect("/")