from django.db import models

# Create your models here.
class Author(models.Model):
	full_name = models.CharField(max_length=100)
	birth_year = models.SmallIntegerField()
	country = models.CharField(max_length=2)

	def __str__(self):
		return self.full_name

class Publish(models.Model):
	publish_name = models.CharField(max_length=96)

	def __str__(self):
		return self.publish_name

class Friend(models.Model):
	friend_name = models.CharField(max_length=30)

	def __str__(self):
		return self.friend_name

class Book(models.Model):
	ISBN = models.CharField(max_length=13)
	title = models.TextField()
	description = models.TextField()
	year_release = models.SmallIntegerField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	publish_book = models.ForeignKey(Publish, on_delete=models.CASCADE, null=True, blank=True, related_name='book')
	price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	copy_count = models.IntegerField(default=1)
	friend = models.ManyToManyField(Friend, blank=True, related_name='books')
	cover = models.ImageField(upload_to='cover/%Y/%m/%d', blank=True)

	def __str__(self):
		return self.title

