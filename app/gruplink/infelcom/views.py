#coding=utf-8
# Create your views here.


from django.shortcuts import render_to_response, HttpResponseRedirect
from django.template import RequestContext
from infelcom.models import Section, Slide, Aspect, Content, Member, ProfileLinks, Project, Product
import re

from django.utils import translation

def logout(request):
	del request.session['user']
	return HttpResponseRedirect("/infelcom/#inicio")

def load_admin(request):
	request.session['user']='admin'
	return HttpResponseRedirect("/infelcom/#inicio")

def home(request):

	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	slides=Slide.objects.all().order_by('slide_index')
	slides_pagers=range(1,len(slides)+1)
	aspects= Aspect.objects.all().order_by('index')
	members=Member.objects.all()
	links=ProfileLinks.objects.all()
	projects=Project.objects.all()
	products=Product.objects.all()
	contents=Content.objects.all()
	
	if request.method=="POST":
		if request.POST.get("charge"):
			if request.POST.get("charge") != "all":
				members=Member.objects.filter(charge=request.POST.get("charge"))
		request.session['filtering_charge_by']=request.POST.get("charge")

	return render_to_response ('infelcom-index.html', 
							  	{'sections':sections, 
							  	 'slides':slides, 
							  	 'slides_pagers':slides_pagers,
							  	 'aspects':aspects,
							  	 'members':members,
							  	 'links':links,
							  	 'projects':projects,
							  	 'products':products,
							  	 'contents':contents
							  	}, context_instance=RequestContext(request))

def add_section(request):

	print "holaaaa"

	name=request.POST.get('section_name')
	title=request.POST.get('section_title')
	language=str(request.LANGUAGE_CODE)
	next_index=int(request.POST.get('section_index'))

	new_section=Section(section_name=name, section_title=title, section_lang=language, section_author=request.user, section_index=next_index)

	new_section.save()
	new_content=Content(section_id=new_section, text="No se ha definido contenido para esta sección")
	new_content=Content(section_id=new_section, text="No se ha definido contenido para esta sección")
	new_content.save()

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


def update_content(request):

	id=request.POST.get('id')
	text=request.POST.get('text')

	content=Content.objects.get(id=id)
	content.text=text
	content.save()

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

	new_slide=Slide(slide_name=name, 
		slide_title=title, slide_abstract=abstract, slide_lang=request.LANGUAGE_CODE, 
		slide_author=request.user,
		slide_link=link, slide_bg=bg, slide_icon=icon, slide_index=int(index))

	new_slide.save()

	return HttpResponseRedirect("/infelcom/#inicio")

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

	new_aspect.save()

	return HttpResponseRedirect("/infelcom/#grupo")

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

	aspect.save()

	return HttpResponseRedirect("/infelcom/#grupo")

def delete_aspect(request, identification):

	aspect=Aspect.objects.get(id=identification)
	aspect.delete()

	return HttpResponseRedirect("/infelcom/#grupo")


def load_profile_form(request):
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	all_projects=Project.objects.all()
	all_products=Product.objects.all()

	return render_to_response ('member.html', 
							  	{'adding':True, 'sections':sections, 'all_projects':all_projects, 'all_products':all_products}, context_instance=RequestContext(request))

def load_profile(request, identification):
	
	member = Member.objects.get(id=identification)
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	links=ProfileLinks.objects.filter(member=member)
	all_projects=Project.objects.all()
	user_projects=Project.objects.filter(members__id__exact=member.id)
	all_products=Product.objects.all()
	user_products=Product.objects.filter(members__id__exact=member.id)

	return render_to_response ('member.html', 
							  	{'sections':sections, 
							  	 'member':member,
							  	 'links':links,
							  	 'all_projects':all_projects,
							  	 'user_projects':user_projects,
							  	 'all_products':all_products,
							  	 'user_products':user_products
							  	}, context_instance=RequestContext(request))

def add_member(request):

	name=request.POST.get('name')
	last_name=request.POST.get('lastname')
	charge=request.POST.get('charge')
	cvlac=request.POST.get('cvlac')
	description=request.POST.get('description')
	profile_img=request.FILES.get('image') if request.FILES.get('image') else "profiles_img/profile.png"


	new_member=Member(name=name, last_name=last_name, charge=charge,
		profile_img=profile_img, cv_lac=cvlac, about=description)
	new_member.save()

	projects=request.POST.getlist('projects')
	products=request.POST.getlist('products')
	
	for project_id in projects:
		project_id=int(project_id)
		project=Project.objects.get(id=project_id)
		project.members.add(new_member)
		project.save()

	for product_id in products:
		product_id=int(product_id)
		product=Product.objects.get(id=product_id)
		product.members.add(new_member)
		product.save()



	return HttpResponseRedirect("/infelcom/#miembros")

def update_member(request, identification):

	member=Member.objects.get(id=identification)

	name=request.POST.get('name')
	last_name=request.POST.get('lastname')
	charge=request.POST.get('charge')
	cvlac=request.POST.get('cvlac')
	description=request.POST.get('description')
	profile_img=request.FILES.get('image') if request.FILES.get('image') else member.profile_img


	member.name=name
	member.last_name=last_name
	member.charge=charge
	member.profile_img=profile_img
	member.cv_lac=cvlac
	member.about=description

	member.save()

	projects=request.POST.getlist('projects')
	products=request.POST.getlist('products')

	del_projects=Project.objects.filter(members__id__exact=member.id)

	for project in del_projects:
		project.members.remove(member)
	
	for project_id in projects:
		project_id=int(project_id)
		project=Project.objects.get(id=project_id)
		project.members.add(member)
		project.save()

	del_products=Product.objects.filter(members__id__exact=member.id)

	for product in del_products:
		product.members.remove(member)
	
	for product_id in products:
		product_id=int(product_id)
		product=Product.objects.get(id=product_id)
		product.members.add(member)
		product.save()

	return HttpResponseRedirect("/infelcom/#miembros")

def delete_member(request, identification):
	member=Member.objects.get(id=identification)
	links=ProfileLinks.objects.filter(member=member)

	del_projects=Project.objects.filter(members__id__exact=member.id)

	for project in del_projects:
		project.members.remove(member)

	del_products=Product.objects.filter(members__id__exact=member.id)

	for product in del_products:
		product.members.remove(member)

	for link in links:
		link.delete()

	member.delete()

	return HttpResponseRedirect("/infelcom/#miembros")



def load_project_form(request):
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	members=Member.objects.all()

	return render_to_response ('project.html', 
							  	{'adding':True, 'sections':sections, 'members':members}, context_instance=RequestContext(request))

def load_project(request, identification):
	
	project = Project.objects.get(id=identification)
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	members=Member.objects.all()
	project_members=project.members.all()
	
	return render_to_response ('project.html', 
							  	{'sections':sections, 
							  	 'project':project,
							  	 'members':members,
							  	 'project_members':project_members
							  	}, context_instance=RequestContext(request))

def add_project(request):

	title=request.POST.get('title')
	status=request.POST.get('status')
	progress=request.POST.get('progress')
	more_url=request.POST.get('more_url')
	description=request.POST.get('description')
	image=request.FILES.get('image') if request.FILES.get('image') else "projects_img/project.png"

	print title, status, progress, more_url, description, image

	new_project=Project(title=title, description=description, status=status, progress=10, url=more_url, project_img=image)
	new_project.save()

	members=request.POST.getlist('members')
	
	print members
	
	for member_id in members:
		member_id=int(member_id)
		member=Member.objects.get(id=member_id)
		new_project.members.add(member)
		new_project.save()

	return HttpResponseRedirect("/infelcom/#proyectos")

def update_project(request, identification):

	project=Project.objects.get(id=identification)

	title=request.POST.get('title')
	status=request.POST.get('status')
	progress=request.POST.get('progress')
	more_url=request.POST.get('more_url')
	description=request.POST.get('description')
	image=request.FILES.get('image') if request.FILES.get('image') else project.project_img

	project.title=title
	project.description=description
	project.status=status
	project.progress=10
	project.url=more_url
	project.project_img=image

	project.save()

	members=request.POST.getlist('members')
	members_to_del=project.members.all()

	for member in members_to_del:
		project.members.remove(member)
	
	for member_id in members:
		member_id=int(member_id)
		member=Member.objects.get(id=member_id)
		project.members.add(member)
		project.save()

	return HttpResponseRedirect("/infelcom/#proyectos")

def delete_project(request, identification):
	project=Project.objects.get(id=identification)
	
	del_members=project.members.all()

	for member in del_members:
		project.members.remove(member)

	
	project.delete()

	return HttpResponseRedirect("/infelcom/#proyectos")



def load_product_form(request):
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	members=Member.objects.all()

	return render_to_response ('product.html', 
							  	{'adding':True, 'sections':sections, 'members':members}, context_instance=RequestContext(request))

def load_product(request, identification):
	
	product = Product.objects.get(id=identification)
	
	lang=str(request.LANGUAGE_CODE)
	sections = Section.objects.filter(section_lang=lang).order_by('section_index')
	members=Member.objects.all()
	product_members=product.members.all()

	
	return render_to_response ('product.html', 
							  	{'sections':sections, 
							  	 'product':product,
							  	 'members':members,
							  	 'product_members':product_members
							  	}, context_instance=RequestContext(request))

def add_product(request):

	title=request.POST.get('title')
	more_url=request.POST.get('more_url')
	description=request.POST.get('description')
	image=request.FILES.get('image') if request.FILES.get('image') else "products_img/product.png"

	new_product=Product(title=title, description=description, url=more_url, product_img=image)
	new_product.save()

	members=request.POST.getlist('members')
	
	print members
	
	for member_id in members:
		member_id=int(member_id)
		member=Member.objects.get(id=member_id)
		new_product.members.add(member)
		new_product.save()

	return HttpResponseRedirect("/infelcom/#productos")

def update_product(request, identification):

	product=Product.objects.get(id=identification)

	title=request.POST.get('title')
	more_url=request.POST.get('more_url')
	description=request.POST.get('description')
	image=request.FILES.get('image') if request.FILES.get('image') else product.product_img

	product.title=title
	product.description=description
	product.url=more_url
	product.product_img=image

	product.save()

	members=request.POST.getlist('members')

	print "MAM", members

	members_to_del=product.members.all()

	for member in members_to_del:
		product.members.remove(member)
	
	for member_id in members:
		member_id=int(member_id)
		member=Member.objects.get(id=member_id)
		product.members.add(member)
		product.save()

	return HttpResponseRedirect("/infelcom/#productos")

def delete_product(request, identification):
	product=Product.objects.get(id=identification)
	
	del_members=product.members.all()

	for member in del_members:
		product.members.remove(member)

	
	product.delete()

	return HttpResponseRedirect("/infelcom/#productos")
