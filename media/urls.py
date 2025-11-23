
from django.urls import path,include
from .views import Home,Login,signup,LoGout,PostHome,upload_post,profile,save,specificpost,chatpage
urlpatterns = [
    path("",Home,name="home"),
    path("login",Login,name="loginp"),
    path("signup",signup),
    path("logout",LoGout),
    path("posts",PostHome,name="posts"),
    path("uploadpost",upload_post),
    path("profile/<str:user>",profile,name= "profile-user"),
    path("save/post/<int:id>",save),
    path("post/<int:id>",specificpost),
    path("chat/",chatpage)
]