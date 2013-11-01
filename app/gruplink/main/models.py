from django.db import models


# Create your models here.
class Section(models.Model):
	section_name=models.CharField(max_length=100,null=False, unique=True)
	section_title=models.CharField(max_length=100,null=False)
	section_lang=models.CharField(max_length=2,null=False)
	section_author=models.CharField(max_length=100,null=False)
	last_modify=models.DateField(null=False, auto_now=True)
	section_index=models.IntegerField(null=False)

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
		