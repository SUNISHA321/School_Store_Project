from schoolstoreapp.models import Department,Course
from django import forms
from django.core.exceptions import ValidationError
class CourseForm(forms.Form):

   CHOICES = [('Male','Male'),('Female','Female')]
   name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border-0','id':'name'}))
   Dob = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))
   Age = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control border-0'}))
   Gender = forms.CharField(label='Gender', widget=forms.RadioSelect(choices=CHOICES))
   phone_number = forms.CharField(widget=forms.TextInput(attrs={'size': 10, 'maxlength': 5,'type':'number','class':'form-control border-0'}))

   Email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control border-0'}))
   Address = forms.CharField(widget=forms.Textarea(attrs={"rows": "5",'class':'form-control border-0'}))

   department=forms.ModelChoiceField(queryset=Department.objects.all(),empty_label="Department")
   COURSE_CHOICES = [
      ('', 'Course'),
   ]
   # course=forms.ModelChoiceField(queryset=Course.objects.all(),empty_label="Course")
   course=forms.CharField(widget=forms.Select(choices=COURSE_CHOICES,attrs={'class':'form-control border-0'}))

   PURPOSE_CHOICES = [
      ('Enquiry', 'Enquiry'),
      ('Return', 'Return'),
   ]
   MATERIAL_CHOICES = [
      ('Book', 'Book'),
      ('Pen', 'Pen'),
   ]

   Purpose = forms.CharField(widget=forms.Select(choices=PURPOSE_CHOICES,attrs={'class':'form-control border-0'}))
   Material = forms.MultipleChoiceField(choices=MATERIAL_CHOICES, widget=forms.CheckboxSelectMultiple())
   # def clean_name(self):
   #    name = self.cleaned_data['name']
   #    if len(name) > 3:
   #       raise ValidationError('myError')
   #    return name

   def clean_phone_number(self):
      phone_number = self.cleaned_data['phone_number']
      if len(phone_number) > 11 :
         raise ValidationError('Phone number must be 10 digit limit')
      return phone_number



