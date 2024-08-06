from django.db import models
from django.utils.text import slugify

# Create your models here.
class Skills(models.Model):
    name = models.CharField(max_length=200)


class Location(models.Model):
    street = models.CharField(max_length=200) 
    city = models.CharField(max_length=200)
    state= models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)
        
class Author(models.Model):
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    designation  = models.CharField(max_length=200)

class JobPost(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time','F'),
        ('Part Time','P'),

    ]
    titel  = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    expiry = models.DateField(null=True)
    salary = models.IntegerField()
    slug = models.SlugField(null=True,max_length=50,unique=True)
    Location = models.OneToOneField(Location,on_delete = models.CASCADE ,null=True) # onetone
    Author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True) #many to one 
    skills = models.ManyToManyField(Skills)
    type = models.CharField(max_length=200, null=False,choices=JOB_TYPE_CHOICES)

    def save(self, *args,**kwargs):
        if not self.id:
            self.slug = slugify(self.titel)
        return super(JobPost , self).save(*args, **kwargs)

    def __str__(self):
        # return self.titel
        return f"{self.titel} with salary {self.salary}"





 