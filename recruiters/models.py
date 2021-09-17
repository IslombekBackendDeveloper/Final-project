from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django_countries.fields import CountryField
from django.utils import timezone
from autoslug import AutoSlugField




class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Remote', 'Remote'),

    ]
    SKILL_CHOICES = [
        ('HTML/CSS','HTML/CSS'),
        ('JavaScript','JavaScript'),
        ('PHP','PHP'),
        ('PYTHON','PYTHON'),
        ('Java','Java'),
        ('C++','C++'),
        ('TypeScript','TypeScript'),
        ('Swift','Swift'),
        ('DESKTOP','DESKTOP'),  
        ('ANDROID','ANDROID'),
    ]
    recruiter = models.ForeignKey(
        User, related_name='jobs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=200)
    location = CountryField(blank_label='(select country)')
    Offered_salary = models.PositiveIntegerField( null=True)
    description = models.TextField()
    Expiration_date = models.DateField(null=True)
    skills_req = models.CharField(max_length=200, choices=SKILL_CHOICES)
    job_type = models.CharField(
        max_length=30, choices=JOB_TYPE_CHOICES, default='Full Time', null=True)
    link = models.URLField(null=True, blank=True)
    slug = AutoSlugField(populate_from = 'title', unique = True, null=True),
    date_posted = models.DateTimeField(default=timezone.now)
    company_logo = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Applicants(models.Model):
    job = models.ForeignKey(
        Job, related_name='applicants', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='applied', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant


class Selected(models.Model):
    job = models.ForeignKey(
        Job, related_name='select_job', on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User, related_name='select_applicant', on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.applicant