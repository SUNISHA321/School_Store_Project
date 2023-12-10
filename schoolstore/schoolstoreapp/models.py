from django.db import models

# Create your models here.
from django.urls import reverse


class Department(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='department',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='department'
        verbose_name_plural='department'

    def get_url(self):
        return reverse('school:departDetail', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Course(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    class Meta:
        ordering=('name',)
        verbose_name='course'
        verbose_name_plural='course'
    def __str__(self):
        return '{}'.format(self.name)
class Apply(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    PURPOSE_CHOICES = (
        ('Male', 'Enquiry'),
        ('Return', 'Return')
    )
    name=models.CharField(max_length=250)
    date = models.DateField()
    age = models.CharField(max_length=10)
    slug=models.SlugField(max_length=250,unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=128)
    phonenumber=models.IntegerField()
    email=models.CharField(max_length=250)
    address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    purpose = models.CharField(choices=PURPOSE_CHOICES, max_length=128)
    material=models.CharField(max_length=250)
    class Meta:
        ordering=('name',)
        verbose_name='apply'
        verbose_name_plural='apply'
    def __str__(self):
        return '{}'.format(self.name)






