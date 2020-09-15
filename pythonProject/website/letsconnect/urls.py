from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('message/', views.message, name='message'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('faq/', views.faq, name='faq'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login, name='login'),
    path('forgotpassword/', views.forgotpassword, name='forgotpassword'),
    path('setpassword/', views.setpassword, name='setpassword'),
    path('hom3', views.hom3, name='hom3'),
    path('logout/', views.logout, name='logout'),
    path('updateprofile/',views.updateprofile,name= 'updateprofile'),
    path('profilephotoupload/',views.profilephotoupload,name= 'profilephotoupload'),
    path('contactform/',views.contactform,name= 'contactform'),



]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)