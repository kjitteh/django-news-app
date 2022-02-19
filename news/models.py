from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=20)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.title


class Article(models.Model):
	cover = models.CharField(max_length=200, help_text="Enter url of cover image")
	title = models.CharField(max_length=200)
	overview = models.CharField(max_length=500, help_text="Enter a brief descripton of the news")
	content = RichTextField()
	pub_date = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

	class Meta:
		ordering = ('-pub_date',)

	def __str__(self):
		return self.title
