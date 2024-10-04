from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth import authenticate, login as auth_login  # Rename login to auth_login
from django.db.models import Q  
from django.db import models
from app.models import Category, Company, Customer,Jobs, footer
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.utils.crypto import get_random_string
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        # Authenticate using email instead of username
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
                auth_login(request, user)  # Use auth_login instead of login
                return redirect('index')
        else:
            return render(request, 'login.html', {'error': "Invalid email or password"})

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def splash(request):
     return render(request,'splash.html')

@csrf_protect
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')

        # Validate phone number
        if not phone_number or len(phone_number) != 10:
            error_message = "Enter a correct 10-digit phone number"
            return render(request, 'signup.html', {'error': error_message})

        # Validate email format
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'signup.html', {'error': "Enter a valid email address"})

        # Check if email or phone number already exists
        if Customer.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': "Email already exists"})
        if Customer.objects.filter(number=phone_number).exists():
            return render(request, 'signup.html', {'error': "Phone number already exists"})

        # Generate a unique username if needed
        username = name
        if User.objects.filter(username=username).exists():
            username = name + get_random_string(5)  # Append random characters

        # Create the user with a unique username
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.save()

        # Create the customer profile
        customer = Customer.objects.create(
            user=user,
            email=email,
            number=phone_number
        )
        customer.save()

        # Redirect to the login page after successful signup
        return redirect('login')

    return render(request, 'signup.html')



def index(request):
        category=Category.objects.filter(jobs__isnull=False).distinct()
        footers=footer.objects.all()
        context={
              'category':category,
              'footers':footers
        }
        return render(request, 'index.html',context)

def job_list(request):
        return render(request,'details.html')

def job_search(request):
    query = request.GET.get('query', '')  # Get the search query from the request
    location_query = request.GET.get('location', '')  # Get the location from the request

    # Filter jobs based on the search query and location
    jobs = Jobs.objects.all().order_by('-created_at') 
    if query:
        jobs = jobs.filter(
            models.Q(job_title__icontains=query) | models.Q(tags__icontains=query)
        )  # Filter by job title or tags

    if location_query:
        jobs = jobs.filter(Location__location__icontains=location_query)  # Search in location

    # Paginate the results
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)
    footers=footer.objects.all()


    context = {
        'jobs': page_obj,
        'query': query,
        'location_query': location_query,
        'footers':footers
    }

    return render(request, 'details.html', context)



def company_list(request):
    query = request.GET.get('q')  # Get the search query from the URL parameters
    location = request.GET.get('city')  # Get the selected city (location) from the URL parameters

    # Filter companies based on query and location
    if query and location:
        companies = Company.objects.filter(company_name__icontains=query, location__iexact=location)
    elif query:
        companies = Company.objects.filter(company_name__icontains=query)  
    elif location:
        companies = Company.objects.filter(Location__location__iexact=location) 
    else:
        companies = Company.objects.all() 

    count = companies.count()  

    # Pagination
    paginator = Paginator(companies, 10)  # Display 10 companies per page
    page_number = request.GET.get('page')
    company_page = paginator.get_page(page_number)
    footers=footer.objects.all()


    context = {
        'company': company_page,
        'count': count,
        'selected_city': location,
        'footers':footers  # Pass the selected city for highlighting purposes
    }
    return render(request, 'companies.html', context)


def company_detail(request,id):
    company=Company.objects.get(id=id)
    referrals = company.referrals.all()
    footers=footer.objects.all()
    context={
        'company':company,
        'referrals': referrals,
        'footers':footers
    }
    return render(request,'company_details.html',context)


def job_details(request, id):
    job = get_object_or_404(Jobs, id=id)
    footers=footer.objects.all()

    context = {
        'job': job,
        'footers':footers
   }
    return render(request, 'job_details.html', context)

def category(request,id):
     category=Category.objects.get(id=id)
     job=Jobs.objects.filter(category=category)
     paginator = Paginator(job, 10)  # Display 10 companies per page
     page_number = request.GET.get('page')
     jobs = paginator.get_page(page_number)
     footers=footer.objects.all()
     context={
          'category':category,
          'jobs':jobs,
          'footers':footers
     }
     return render(request,'category_wise.html',context)

def about(request):
     about=footer.objects.all()
     footers=footer.objects.all()
     user_count = User.objects.count()
     context={
          'about':about,
          'footers':footers,
          'user_count': user_count
     }
     return render(request,'about.html',context)

def privacy(request):
     return render(request,'privacy_policy.html')