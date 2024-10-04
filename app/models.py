
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class JobManager(models.Manager):
    def get_queryset(self):
        current_date = timezone.now().date()
        expired_jobs = super().get_queryset().filter(job_applylast_date__lt=current_date)
        expired_jobs.delete()
        return super().get_queryset()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Each Customer has one User profile
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)  # Ensure email is unique in Customer
    number = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Ensure phone number is unique
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['-created_at']

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.location


class Jobs(models.Model):
    JOB_TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Job', 'Job'),
    ]
    WORK_MODE_CHOICES = [
        ('On-site', 'On-site'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),

    ]
    job_title = models.CharField(max_length=255)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    company=models.CharField(max_length=500,null=True,blank=True)
    Location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    job_posted_date = models.DateField(auto_now_add=True,null=True,blank=True)
    job_applylast_date = models.DateField(null=True, blank=True)
    experience_level = models.CharField(max_length=100)
    work_mode = models.CharField(max_length=10, choices=WORK_MODE_CHOICES,null=True,blank=True)
    job_description=models.CharField(max_length=100,null=True,blank=True)
    tags=models.CharField(max_length=200,null=True,blank=True)
    responsibilities = RichTextField(null=True, blank=True)
    qualifications = RichTextField(null=True, blank=True)
    skill1 = models.CharField(max_length=100, null=True, blank=True)
    skill2 = models.CharField(max_length=100, null=True, blank=True)
    skill3 = models.CharField(max_length=100, null=True, blank=True)
    skill4 = models.CharField(max_length=100, null=True, blank=True)
    skill5 = models.CharField(max_length=100, null=True, blank=True)
    skill6 = models.CharField(max_length=100, null=True, blank=True)
    pay_range = models.CharField(max_length=100,null=True,blank=True)
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES,null=True,blank=True)
    openings=models.PositiveIntegerField(null=True,blank=True)
    job_url = models.URLField(blank=True, null=True)

    objects = JobManager()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)  # Set only once when the object is created
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)      # Automatically update every time the object is saved

    def __str__(self):
        return self.job_title
    
    



# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=255)
    employees = models.CharField(max_length=50,null=True,blank=True)  # You could also use IntegerField if you prefer exact numbers
    industry = models.CharField(max_length=100,null=True,blank=True)
    Location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True,blank=True)
    about=RichTextField(null=True,blank=True)
    mission=RichTextField(null=True,blank=True)
    description = RichTextField(null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    carrier_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return self.company_name
    
class Referral(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='referrals')
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    linkedin_profile = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class footer(models.Model):
    insta_url = models.URLField()
    linked_url = models.URLField()
    youtube_url=models.URLField(null=True,blank=True)
    whatsapp_channel_url=models.URLField(null=True,blank=True)
    telegram_url=models.URLField(null=True,blank=True)
    about=RichTextField(blank=True,null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # For WhatsApp number
    shanu_url=models.URLField(null=True,blank=True)
    ak_url=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.phone_number