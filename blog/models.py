from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse

# Create your models here.

class EntryQuerySet(models.QuerySet):
	def published(self):
		return self.filter(published=True)


class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug


class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = MarkdownField()
	slug = models.SlugField(max_length=200, unique=True)
	published = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tag)

	objects = EntryQuerySet.as_manager()

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"]