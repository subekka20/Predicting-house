from django.shortcuts import render, redirect, get_object_or_404
from .models import User, House, Booking
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            if user.type == 'admin':
                return redirect('admin_dashboard')
            elif user.type == 'customer':
                home_url = f'/{user.id}/home/'
                return redirect(home_url)
        except User.DoesNotExist:
            # Handle invalid login
            pass
    return render(request, 'users/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        contact_no = request.POST['contact_no']
        type = 'customer'  # Default to customer type for signup
        User.objects.create(username=username, password=password, email=email, contact_no=contact_no, type=type)
        return redirect('login')
    return render(request, 'users/signup.html')

def admin_dashboard(request):
    bookings = Booking.objects.all()
    return render(request, 'users/admin_dashboard.html',{'bookings':bookings})

# def delete_booking_admin(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     booking.delete()
#     messages.success(request, 'Booking deleted successfully.')
#     bookings = Booking.objects.all()
#     return render(request, 'users/admin_dashboard.html',{'bookings':bookings})

def home(request, user_id):
    houses = House.objects.all()
    user = User.objects.get(id=user_id)
    return render(request, 'users/home.html', {'houses': houses, 'user': user})

def houses(request):
    houses = House.objects.all()
    return render(request, 'users/houses.html', {'houses': houses})

def new_house(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        price = request.POST['price']
        image_url = request.POST['image_url']
        description = request.POST['description']

        House.objects.create(name=name, location=location, price=price, image_url=image_url, description=description)
        return redirect('houses')

    return render(request, 'users/new_house.html')

def booking(request, house_id):
    house = House.objects.get(id=house_id)

    if request.method == 'POST':
        u = request.POST['user']
        reply = request.POST['reply']
        user =  User.objects.get(id=u)

        Booking.objects.create(user=user, house=house, reply=reply)
        
        home_url = f'/{user.id}/home/'
        return redirect(home_url)

    return render(request, 'users/booking.html', {'house': house})

def profile(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        # Update user details
        user.username = request.POST['username']
        user.password = request.POST['password']
        user.email = request.POST['email']
        user.contact_no = request.POST['contact_no']
        user.save()

    bookings = Booking.objects.filter(user_id=user_id)
    
    return render(request, 'users/profile.html', {'user': user, 'bookings': bookings})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    user_id = booking.user.id 
    booking.delete()
    messages.success(request, 'Booking deleted successfully.')
    prof_url = f'/{user_id}/profile/'
    return redirect(prof_url)

def filtered_page(request, user_id):
    # Retrieve filter parameters from GET request
    location = request.GET.get('location', '')
    price = request.GET.get('price', '')

    # Query houses based on filters
    filtered_houses = House.objects.filter(location__icontains=location, price__lte=price)

    return render(request, 'users/filtered_page.html', {'user_id': user_id, 'filtered_houses': filtered_houses})

# def reply_booking(request, booking_id):
#     if request.method == 'POST':
#         # Assuming you have a form to handle replies
#         reply_text = request.POST.get('reply_text')
        
#         # Update the booking with the reply
#         booking = Booking.objects.get(id=booking_id)
#         booking.reply = reply_text
#         booking.save()

#         messages.success(request, 'Reply saved successfully.')

#     # Redirect to the admin dashboard or wherever appropriate
#     return redirect('admin_dashboard')

# def mark_as_sold(request, booking_id):
#     # Get the Booking object
#     booking = get_object_or_404(Booking, id=booking_id)

#     # Check if the associated house is not already sold
#     if not booking.house.sold:
#         # Mark the house as sold
#         booking.house.sold = True
#         booking.house.save()

#         # You can add additional logic or messages if needed
#         messages.success(request, f"The house {booking.house.name} has been marked as sold.")
#     else:
#         messages.warning(request, f"The house {booking.house.name} is already marked as sold.")

#     # Redirect back to the admin dashboard or any other page you prefer
#     return redirect('users:admin_dashboard')