from django.db import models


# Create your models here.
class Section(models.Model):
	section_name=models.CharField(max_length=100,null=False, unique=True)
	section_title=models.CharField(max_length=100,null=False)
	section_lang=models.CharField(max_length=2,null=False)
	section_author=models.CharField(max_length=100,null=False)
	last_modify=models.DateField(null=False, auto_now=True)
	section_index=models.IntegerField(null=False)
	locked=models.BooleanField()

class Slide(models.Model):
	slide_name=models.CharField(max_length=60,null=False, unique=True)
	slide_title=models.CharField(max_length=150,null=False)
	slide_abstract=models.CharField(max_length=500,null=False)
	slide_lang=models.CharField(max_length=2,null=False)
	slide_author=models.CharField(max_length=100,null=False)
	slide_link=models.CharField(max_length=100,null=False)
	slide_bg=models.ImageField(upload_to='slides_bg')
	slide_icon=models.ImageField(upload_to='slides_icon')
	slide_index=models.IntegerField(null=False)

	def __unicode__(self):
		return self.section_title

class Content(models.Model):
	section_id=models.ForeignKey(Section)
	text=models.CharField(max_length=100000, null=False)

	def __unicode__(self):
		return self.text

class Media(models.Model):
	media_url=models.CharField(max_length=100000,null=False)
	media_type=models.CharField(max_length=100000,null=False)
	content_id=models.ForeignKey(Content)

	def __unicode__(self):
		return self.url

class Aspect(models.Model):
	title=models.CharField(max_length=100,null=False, unique=True)
	icon_name=models.CharField(max_length=50,null=False)
	content=models.CharField(max_length=10000,null=False)
	index=models.IntegerField(null=False)
	lang=models.CharField(max_length=2,null=False)

class Member(models.Model):
	name=models.CharField(max_length=100,null=False)
	last_name=models.CharField(max_length=100,null=False)
	charge=models.CharField(max_length=50, null=False)
	profile_img=models.ImageField(upload_to='profiles_img')
	about=models.CharField(max_length=1000, null=False)
	cv_lac=models.CharField(max_length=200,null=False)

class ProfileLinks(models.Model):
	member=models.ForeignKey(Member)
	title=models.CharField(max_length=30,null=False)
	url=models.CharField(max_length=100,null=False)
	icon=models.CharField(max_length=30,null=False)

class Project(models.Model):
	title=models.CharField(max_length=200,null=False)
	description=models.CharField(max_length=1000,null=False)
	members=models.ManyToManyField(Member)
	status=models.CharField(max_length=50, null=False)
	progress=models.IntegerField(max_length=3)
	aditional_info=models.CharField(max_length=1000,null=False)
	url=models.CharField(max_length=200,null=False)

class Product(models.Model):
	title=models.CharField(max_length=200,null=False)
	description=models.CharField(max_length=1000,null=False)
	members=models.ManyToManyField(Member)
	status=models.CharField(max_length=50, null=False)
	progress=models.IntegerField(max_length=3)
	aditional_info=models.CharField(max_length=1000,null=False)
	url=models.CharField(max_length=200,null=False)



from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Slide)
def photo_post_delete_handler(sender, **kwargs):
    slide = kwargs['instance']
    storage, path = slide.slide_bg.storage, slide.slide_bg.path
    storage.delete(path)