
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control


# Create your views here.

def home(request):
    if request.session.has_key('user_login'):  
        return render(request, "index.html")
    else:
        return redirect(signin)
@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def index(request):
    if request.session.has_key('user_login'):  
        return render(request, "index.html")
    else:
        return redirect(signin)

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']           
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, "Your Account has been succesfully created.")
            return redirect('home')
    return render(request, "signup.html")


@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def adminsignin(request):
      if request.session.has_key('admin_login'):
        list = User.objects.all()
        return render(request, 'list.html',{'ls':list})
      else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['pass1']
            admin = authenticate(username=username, password=password)
            
            if admin is not None:
                if admin.is_superuser:
                
                    login(request, admin)
                    messages.info(request, "You logged in succesfully")
                    request.session['admin_login'] = True
                    list = User.objects.all()
                    return render(request, 'list.html', {'ls':list})
            else:
                    
                    messages.info(request, "Invalid  username or password.")
                    return render(request, 'adminsignin.html',{"login_error":"invalid credentials"})
        else:
        
                return render(request, 'adminsignin.html')

def search_list(request):
   
    if request.method == "POST":
        query_name = request.POST.get('name')
        
        if query_name:
            
            results = User.objects.filter(first_name__icontains=query_name)
            return render(request, 'list.html', {"ls":results})

        return render(request, 'list.html')
    


def edit(request,id):
    print(id)
    object=User.objects.get(id=id)
    return render(request, 'list_edit.html',{'object':object})
def update(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
            
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            pass1 = request.POST['pass1']
            pass2 = request.POST['pass2']

            if pass1 == pass2:
                user.username=username
                user.first_name=fname
                user.last_name=lname
                user.email=email
                user.set_password(pass1)
                user.save()
                messages.success(request, "Your Update is succesful")
                list = User.objects.all()
                return render(request, 'list.html', {'ls':list})
            return render(request, "list_edit.html")
def delete(request,pk):   
        user = User.objects.get(pk=pk)
       
        user.delete()
        list = User.objects.all()
        return render(request,'list.html',{'ls':list})




@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def signin(request):
    if request.session.has_key('user_login'):
        return render(request, 'index.html')
    else:    
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['pass1']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                request.session['user_login'] = True
                return redirect(index)
            else:
                messages.info(request, "Invalid  username or password.")
                return render(request, 'signin.html',{"login_error":"invalid credentials"})

        else:
       
            return render(request, 'signin.html')

@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def signout(request):
    logout(request)
    try:
        del request.session['user_login']
    except:
        pass
    messages.success(request, "Logged Out Succesfully")
    return redirect(home)
@cache_control(no_cache=True, must_revalidated=True, no_store=True)
def adminlogout(request):
    try:
        del request.session['admin_login']
    except:
        pass
    logout(request)
    messages.success(request, "Logged Out Succesfully")
    return redirect(adminsignin)