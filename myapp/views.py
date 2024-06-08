from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import Registration
from .models import CourseEnrollment

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        status = 'student'  # Assuming all new registrations are students by default

        if password != repassword:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if Registration.objects.filter(mobile=mobile).exists():
            messages.error(request, 'Mobile number already registered')
            return redirect('register')

        if Registration.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        try:
            # Save the user in the custom registration model
            registration = Registration.objects.create(email=email, name=name, mobile=mobile, password=password, status=status)
            registration.save()


            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('register')

    return render(request, 'register.html')

  # Importing login function with an alias

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user-type')
        print(email, password, user_type)
        # user = authenticate(request, email=email, password=password, status=user_type)
        user = Registration.objects.get(email=email, password=password, status = user_type)
        print(user.email, user.mobile, user.name)
        if user is not None:
            request.session['name'] = user.name
            request.session['user_type'] = user.status
            request.session['email'] = user.email
            request.session['mobile'] = user.mobile
            auth_login(request, user)  # Using alias auth_login instead of login
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid email or password or user type')

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    # Clear session variables
    request.session.flush()
    return redirect('home')

def check_database(request):
    engine = connection.settings_dict['ENGINE']
    return HttpResponse(f"Database engine: {engine}")


def notifications(request):
    return render(request, 'notifications.html')

def manage_members(request):
    return render(request, 'members.html')

def manage_courses(request):
    return render(request, 'courses.html')

# def testimonials(request):
#     return render(request, 'testimonials.html')
def testimonials(request):
    testimonials = CourseEnrollment.objects.filter(course_completion='1', testimonial__isnull=False, testimonial_status__isnull=True)
    return render(request, 'testimonials.html', {'testimonials': testimonials})
def approve_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(CourseEnrollment, id=testimonial_id)
    testimonial.testimonial_status = 'A'  # Assuming 'A' stands for approved
    testimonial.save()
    return redirect('testimonials')

def reject_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(CourseEnrollment, id=testimonial_id)
    testimonial.testimonial_status = 'R'  # Assuming 'R' stands for rejected
    testimonial.save()
    return redirect('testimonials')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')