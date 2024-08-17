from django.views import generic
from .models import Post, AddRooms
from .models import Signup
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.shortcuts import render
import random
from .models import Post, Category,Information


def catering_conference(request):
    return render(request, 'catering_confrence.html')

def resturant_dining(request):
    return render(request, 'resturantanddining.html')

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['roomss'] = AddRooms.objects.all()
        return context

def about(request):
    return render(request, "about.html")   

class PostDetail(generic.DetailView):
    rooms = AddRooms.objects.all()  
    template_name = 'post_detail.html'

def home(request):
    return render(request, 'base.html')    

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='1')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context


# this is a signup
def sign_up(request):
    if request.method == 'POST':
        signup_username = request.POST.get('username')
        signup_email = request.POST.get('email')
        signup_password = request.POST.get('password')
        signup_confirm_password = request.POST.get('confirm_password')


         # Check if the required fields are filled in
        if not signup_username or not signup_email or not signup_password or not signup_confirm_password:
            return render(request, 'signup.html', {'error_message': 'Please fill in all the required fields.'})
        # Check if the account already exists
        existing_signup = Signup.objects.filter(username=signup_username, email=signup_email)
        if existing_signup:
            return render(request, 'signup.html', {'error_message': 'Your usernam already exists.'})
        
        elif signup_password != signup_confirm_password:
            return render(request, 'signup.html', {'error_message': 'Your password do not match. Please make sure they match to continue'})
        
        elif len(signup_password) < 5 or len(signup_confirm_password) < 5:
            return render(request, 'signup.html', {'error_message': 'Passwords should be at least 5 characters long'})
        
        else:
            new_signup = Signup(username=signup_username, email=signup_email, password=signup_password, confirm_password=signup_confirm_password)
            new_signup.save()
            return render(request, 'admin_dashboard/hotel/create_hotel.html', {'error_message': 'Your account is created successfully.'})

    return render(request, 'signup.html')

# end of signup



# begining of login
def login_page(request):
    if request.method == 'POST':
        login_email = request.POST.get('email')
        login_password = request.POST.get('password')
        
        existing_signup = Signup.objects.filter(email=login_email, password=login_password)
        if existing_signup:
            return render(request, 'admin_dashboard/hotel/create_hotel.html', {'error_message': 'Login successfully.'})

        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password. Please try again'})
    
    return render(request, 'login.html')

# end of login


def feature(request):
    return render(request, 'feature.html')

def rooms_display(request): 
    rooms = AddRooms.objects.all()  
    return render(request, 'rooms.html', {'rooms': rooms})

def admin_dashboard(request):
    return render(request, 'admin_dashboard/admin.html')

def admins_success(request):
    return render(request, 'admin_dashboard/hotel/sucess_admin.html')

def view_users(request):
    signups = Signup.objects.all() 
    return render(request, 'admin_dashboard/hotel/usersall.html', {'signups': signups})

def hotel_section1(request):
    rooms2 = AddRooms.objects.all()  
    return render(request, 'admin_dashboard/hotel/hotel.html', {'rooms': rooms2})

def user_views(request):
    informations = Information.objects.all()
    return render(request, 'admin_dashboard/hotel/users_admin.html', {'informations': informations})

def delete_information(request, information_id):
    information = get_object_or_404(Information, id=information_id)
    information.delete()
    return redirect('userviews')


def delete_signup(request, signup_id):
    signup = get_object_or_404(Signup, id=signup_id)
    signup.delete()
    return redirect('userview')

def delete_hotel(request, hotel_id):
    hotel = AddRooms.objects.get(id=hotel_id)
    hotel.delete()
    return redirect('hotel1')

def add_hotel(request):
    if request.method == 'POST':
        hostel_name = request.POST.get('name')
        hostel_price = request.POST.get('price')
        hostel_bed = request.POST.get('bed')
        hostel_bathroom = request.POST.get('bathroom')
        hostel_details = request.POST.get('details')
        hostel_roomleft = request.POST.get('roomsleft')
        hostel_image1 = request.FILES.get('image1')
        
        if not hostel_image1:
            return render(request, 'admin_dashboard/hotel/create_hotel.html', {'error_message': 'Please select an image.'})

        # check if the room already exists
        insert_room = AddRooms.objects.filter(name=hostel_name, price=hostel_price, bed=hostel_bed, bathroom=hostel_bathroom, details=hostel_details, roomsleft=hostel_roomleft, image1=hostel_image1)
        if insert_room:
            return render(request, 'admin_dashboard/hotel/create_hotel.html', {'error_message': 'This room has already been created.'})

        else:
            new_room = AddRooms(name=hostel_name, price=hostel_price, bed=hostel_bed, bathroom=hostel_bathroom, details=hostel_details, roomsleft=hostel_roomleft, image1=hostel_image1)
            new_room.save()
            return render(request, 'admin_dashboard/hotel/create_hotel.html', {'error_message': 'Your new room has been saved successfully.'})

    return render(request, 'admin_dashboard/hotel/create_hotel.html')
     

def base_dashboard(request):
    return render(request, 'admin_dashboard/admin_base.html')

def base_sidebarr(request):
    return render(request, 'admin_sidebar.html')


def check_out(request):
    if request.method == 'POST':
        info_fullname = request.POST.get('fullname')
        info_email = request.POST.get('email_info')
        info_address = request.POST.get('address_info')
        info_city = request.POST.get('city_info')
        info_zip = request.POST.get('zip_info')
        info_state = request.POST.get('state_info')

         # check if the measurement already exists
        insert_information = Information.objects.filter(fullname=info_fullname, email_info=info_email, address_info=info_address, city_info=info_city, zip_info=info_zip, state_info=info_state)
        if insert_information:
            return render(request, 'payment_options.html', {'error_message': 'Your information is updated.'})

        else:
            insert_information2 = Information(fullname=info_fullname, email_info=info_email, address_info=info_address, city_info=info_city, zip_info=info_zip, state_info=info_state)
            insert_information2.save()
            return render(request, 'payment_options.html', {'error_message': 'Your information is saved.'})

    return render(request, 'checkout.html')



def card_payment(request):
    return render(request, 'credit_card.html')


def success_message(request):
    return render(request, 'successinfo.html')

def payment_option(request):
    return render(request, 'payment_options.html')