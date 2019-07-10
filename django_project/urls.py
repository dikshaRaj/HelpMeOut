"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/",user_views.register,name='register'),
    path("profile/",user_views.profile,name='profile'),
    path("login/",auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    #path("quizpage/",user_views.quizpage,name='quiz'),
    path("index/",user_views.index,name='index'),
    path("game/",user_views.game,name='game'),
    path("highscores/",user_views.highscores,name='highscores'),
    path("game/end/",user_views.end,name='end'),
    path("quizzing/",user_views.quizzing,name='quizzing'),
    path("plag/",user_views.plag,name='plag'),
    path("materialpage/",user_views.materialpage,name='materials'),
    path("",include('blog.urls')),
    path("upload/",user_views.upload,name='upload'),
    path("doubts/",user_views.doubts,name='doubts'),
    path("quizfiles/",user_views.quizfiles,name='quizfiles')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)