from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post , Comment , Save ,ChatPost

# Create your views here.
from hashlib import sha512
def password_encoder(password:str):
    return sha512(password.encode()).hexdigest()

def Home(request):
    autherized = request.user.is_anonymous
    return render(request,"Home.html", {"autherized":not autherized})

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password = password_encoder(password)
        user = User.objects.filter(username = username,password = password).first()        
        login(request,user)
        return redirect("home")
    return render(request,"login.html",)

def signup(request):
    if request.method == "POST":
        print("tryed to signup")
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = password_encoder(password)
        user = User.objects.create(username = username,password = password,first_name = firstname,last_name = lastname,email = email)
        login(request,user)
        return redirect("home")
    return render(request,"Signup.html")

def LoGout(request):
    if not request.user.is_anonymous:
        logout(request)
        return redirect("home")
    return HttpResponse("You Are Not Autherized")

def PostHome(request):
    if request.user.is_anonymous:
        return redirect("loginp")
    posts = Post.objects.all().order_by("-creat_at")
    saved_posts = Save.objects.filter(saver = request.user).values_list("post_id", flat=True)
    return render(request,"Post-home.html", {"posts":posts, "saved_posts": saved_posts})

def upload_post(request):
    if request.user.is_anonymous:
        return redirect("loginp")
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("Image")

        post = Post.objects.create(
            Creature=request.user,
            title=title,
            Image=image
        )
        return redirect("home")
    return render(request , "uploadpost.html")

def profile(request,user):
    user = User.objects.filter(username = user).first()
    posts = Post.objects.filter(Creature = user).all()
    if user == request.user:
        saves = Save.objects.filter(saver = request.user).all()
        return render(request , "profile.html",{"user":user,"posts":posts , "saves":saves})
    else:
        return render(request , "profile.html",{"user":user,"posts":posts })

def save(request,id):
    
    if request.user.is_anonymous:
        return redirect("loginp")
    post = Post.objects.filter(id = id ).first()
    Save.objects.create(saver = request.user , post = post)
    return redirect("posts")

def specificpost(request , id):
    if request.user.is_anonymous:
        return redirect("loginp")
    post = Post.objects.filter(id = id).first()
    comments = Comment.objects.filter(post = post).order_by("-commented_at")
    if request.method == "POST":
        comment = request.POST.get("comment")
        Comment.objects.create(post= post,commenter = request.user , commenting = comment)
        return render(request , "post.html",{"post":post,"comments":comments})
    saved_posts = Save.objects.filter(saver = request.user).values_list("post_id", flat=True)
    return render(request , "post.html",{"post":post,"comments":comments,"saved_posts": saved_posts})

def chatpage(request):
    if request.user.is_anonymous:
        return redirect("loginp")
    if request.method == "POST":
        text = request.POST.get("text")
        ChatPost.objects.create(poster = request.user,Chat = text)
    chat = ChatPost.objects.all()
    return render(request , "chatpage.html",{"chats":chat})