from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is Home Page")

def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse("This is About Page")

def contact(request):
    if request.method == "POST":
        print('This is Post')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        print(name, email, phone, content)


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            print('Data has been written to the database')
            messages.success(request, 'Your message has been sent successfully')

        return render(request, 'home/contact.html')

    return render(request, 'home/contact.html')
    # return HttpResponse("This is Contact Page")


def search(request):
    # print("i am in search")
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
        print(allPosts)

    if len(allPosts)==0:
        messages.warning(request, 'No search results found. Please refine your query.')
    # allPosts = Post.objects.all()
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
    # return HttpResponse("This is search")


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputs
        if len(username)>15:
            messages.error(request, "Username must be under 15 characters")
            return redirect('home')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('home')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
        if len(pass1)<3:
            messages.error(request, "Password should be at least 3 characters")
            return redirect('home')
        


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your account has been successfully created')
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')
    

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In')
            return redirect('home')
        
        else:
            messages.error(request, 'Invalid Credentials, Please try again')
            return redirect('home')

    return HttpResponse('404 - Not Found')

def handleLogout(request):
    # if request.method == 'POST':
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('home')


    return HttpResponse('handleLogout')