from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contacts.models import Contact

#views.py-accounts
def register(request):
    if request.method == 'POST':
        #register user-get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
       #check if pw's match 
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken, please choose another')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email already exists on a user account')
                    return redirect('register')
                else:
                    #looks ok
                    user = User.objects.create_user(username=username, password=password, 
                    email=email, first_name=first_name, last_name=last_name )
                    #login once registered
                    # auth.login(request, user)
                    # messages.success(request, 'Welcome, you are now registerd and currently logged in')
                    # return redirect('/')
                    user.save()
                    messages.success(request, 'Welcome to BTRE, please log in.')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials, please try again')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')
    


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Logout successful!')
        return redirect('index')


@login_required(login_url='login')
def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts
    }

    return render(request, 'accounts/dashboard.html', context)
