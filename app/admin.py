from django.contrib import admin
from .models import Category, Company, Customer, Jobs,Location, Referral, footer

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) 
    search_fields = ('name',)
    ordering=('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user','email','number')  # Ensure 'name' field exists in the model
    search_fields = ('user','number',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location',)  # Ensure 'name' field exists in the model
    search_fields = ('location',)
    ordering=('location',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name','Location')  # Ensure 'name' field exists in the model
    search_fields = ('company_name','Location')
    list_filter = ('created_at', 'Location', 'industry')  
    ordering = ('company_name',)  # Optional: Specify default ordering if needed



@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('company','name','position')  # Ensure 'name' field exists in the model
    search_fields = ('company','name','position')

@admin.register(Jobs)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'category', 'job_posted_date', 'experience_level', 'Location') 
    search_fields = ('job_title', 'category', 'Location')  # Ensure these fields exist in the Job model
    ordering=('-created_at',)
    list_filter = ('created_at', 'category', 'experience_level')  


@admin.register(footer)
class footerAdmin(admin.ModelAdmin):
    list_display = ('id','insta_url','linked_url')  # Ensure 'name' field exists in the model
