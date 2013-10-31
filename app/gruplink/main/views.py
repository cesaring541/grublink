# Create your views here.


from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from main.models import Section

def home(request):
	sections = Section.objects.all().order_by('section_index')
	print("Hola",len(sections))
	request.session['user']='admin'

	print(request.session.get('user'))

	return render_to_response ('index.html', {'sections':sections}, context_instance=RequestContext(request))

def add_section(request):

	name=request.POST.get('section_name')
	title=request.POST.get('section_title')
	lang=request.POST.get('section_lang')
	next_index=int(request.POST.get('section_index'))

	#Section.objects.values('section_index').order_by('section_index').latest('section_index')['section_index']

	print(next_index)

	new_section=Section(section_name=name, section_title=title, section_lang=lang, section_author=request.session.get('user'), section_index=next_index)

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