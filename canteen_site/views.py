from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import SignUpForm,SignInForm
from .models import MenuItem, Order, OrderItem ,UserInfo,CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib import messages
import json



def index(request):
    return render(request,'index.html')

def adminside(request):
    return render(request,'admin-side.html')

def ourvision(request):
    return render(request,'our-vision.html')

def clientside(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'client-side.html', {'menuItems': menu_items})


def userorders(request):
    user_id = request.user
    userinfo = UserInfo.objects.get(username=user_id.username)

    # Retrieve orders for the user and order them by creation date
    user_orders = Order.objects.filter(user=userinfo).order_by('-created_at')
    
    # Retrieve order items for the retrieved orders
    order_items = OrderItem.objects.filter(order__in=user_orders)
    
    # Filter orders based on status
    pending_orders = user_orders.filter(status='Pending')
    delivered_orders = user_orders.filter(status='Delivered')
    
    count = user_orders.count()+1

    return render(request, 'user-orders.html', {
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
        'order_items': order_items,
        'count':count
    })
    

def signout(request):
    logout(request)
    return render(request,'index.html')



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email=form.cleaned_data['email']
            mobile_number=request.POST['mobile_number']
            userinfo = UserInfo(username=username, email=email, mobile_number=mobile_number)
            userinfo.save()
            success_message = f'Account created successfully!'
            messages.success(request, success_message) 
            return redirect(index) 
        else:
            failure_message = f'Invalid credentials'
            return render(request, 'signup.html', {'form': form, 'failure_message': failure_message}) 
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})





def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                success_message = f'Sign in successful!Welcome {username}'
                messages.success(request, success_message)
                return redirect(clientside)  # Redirect to desired URL after successful login
            else:
                # Invalid login
                return render(request, 'signin.html', {'form': form, 'error_message': 'Invalid email or password'})
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})



@login_required
def get_cart_items(request):
    user_id = request.user  # Get the user ID from the request
    try:
        userinfo = UserInfo.objects.get(username=user_id.username)
    except UserInfo.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'UserInfo does not exist'})

    cart_items = CartItem.objects.filter(user=userinfo)
    cart_items_data = []
    total_sum=0
    for item in cart_items:
        cart_items_data.append({
            'item_id':item.item.item_id,
            'title': item.item.title,
            'category': item.item.category,
            'price': item.item.price*item.quantity,
            'imageurl': item.item.image_url,
            'quantity': item.quantity
        })
        total_sum += item.item.price * item.quantity
    return JsonResponse({'success': True, 'cart_items': cart_items_data,'total_sum':total_sum})


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user  # Get the default User model object

        # Retrieve UserInfo object for the user
        try:
            userinfo = UserInfo.objects.get(username=user.username)
        except UserInfo.DoesNotExist:
            # Handle the case where UserInfo doesn't exist for the user
            return JsonResponse({'success': False, 'message': 'UserInfo does not exist'})

        item_id = data['itemId']
        # Check if the item already exists in the user's cart
        existing_item = CartItem.objects.filter(user=userinfo, item_id=item_id).first()
        if existing_item:
            existing_item.quantity += 1
            existing_item.save()
        else:
            # Create a new CartItem object with quantity 1
            new_item = CartItem.objects.create(
                user=userinfo,
                item_id=item_id,
                quantity=1  # Set quantity to 1 for new item
            )
        
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})


def get_cart_status(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            userinfo = UserInfo.objects.get(username=user.username)
        except UserInfo.DoesNotExist:
            # Handle the case where UserInfo doesn't exist for the user
            return JsonResponse({'success': False, 'message': 'UserInfo does not exist'})

        # Get all items in the user's cart
        cart_items = CartItem.objects.filter(user=userinfo)

        # Construct a dictionary to represent the cart status
        cart_status = {item.item_id: True for item in cart_items}

        return JsonResponse(cart_status)
    else:
        # Handle the case where the user is not authenticated
        return JsonResponse({'error': 'User is not authenticated'}, status=403)


def increase_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        item_id = data.get('itemid')

        # Check if the item exists in the cart for the current user
        try:
            user=request.user
            userinfo = UserInfo.objects.get(username=user.username)
            cart_item = CartItem.objects.get(item_id=item_id, user=userinfo)
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found in cart'})

        # Increase the quantity by 1
        cart_item.quantity += 1
        cart_item.save()

        return JsonResponse({'success': True, 'quantity': cart_item.quantity})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

def decrease_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('itemId')

        # Check if the item exists in the cart for the current user
        try:
            user=request.user
            userinfo = UserInfo.objects.get(username=user.username)
            cart_item = CartItem.objects.get(item_id=item_id, user=userinfo)
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found in cart'})

        # Decrease the quantity by 1, if it's greater than 1
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
            return JsonResponse({'success': True, 'quantity': cart_item.quantity})
        else:
            # If the quantity is already 1, remove the item from the cart
            cart_item.delete()
            return JsonResponse({'success': True, 'quantity': 0})  # Quantity is now 0 after removal
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})





@login_required
def clear_cart(request):
    if request.method == 'POST':
        user = request.user
        try:
            userinfo = UserInfo.objects.get(username=user.username)
            cart_items = CartItem.objects.filter(user=userinfo)
            cart_items_data = []
            for item in cart_items:
                cart_items_data.append({
                    'title': item.item.title,
                    'category': item.item.category,
                    'price': item.item.price,
                    'imageurl': item.item.image_url,
                })
            cart_items.delete()  # Delete all cart items
            return JsonResponse({'success': True, 'cleared_items': cart_items_data})
        except UserInfo.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'UserInfo does not exist'})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})




@login_required
def place_order(request):
    user_id = request.user  # Get the user ID from the request
    try:
        userinfo = UserInfo.objects.get(username=user_id.username)
    except UserInfo.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'UserInfo does not exist'})

    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=userinfo)
        if cart_items.exists():
            total_price = sum(item.item.price * item.quantity for item in cart_items)
            # Create the order with status set to "Pending"
            order = Order.objects.create(user=userinfo, total_price=total_price, status='Pending')
            for cart_item in cart_items:
                # Fetch title, price, and image_url directly from CartItem
                item_title = cart_item.item.title
                item_price = cart_item.item.price
                item_image_url = cart_item.item.image_url
                OrderItem.objects.create(order=order, title=item_title, quantity=cart_item.quantity,
                                         price=item_price*cart_item.quantity, image_url=item_image_url)
            cart_items.delete()
            success_message = f'Order Placed Successfully!'
            messages.success(request, success_message) 
            return redirect('userorders')
    return JsonResponse({'success': False})


def profile(request):
    # Retrieve the current user
    user = request.user
    
    try:
        # Attempt to retrieve user information from the UserInfo table based on the current user's username
        userinfo = UserInfo.objects.get(username=user.username)
    except UserInfo.DoesNotExist:
        # Handle the case where user information does not exist for the current user
        userinfo = None

    # Pass user information to the template context
    context = {
        'userinfo': userinfo
    }

    # Render the profile.html template with the user information
    return render(request, 'profile.html', context)


