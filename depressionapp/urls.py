from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('healing/',views.healing, name='healing'),
    path('about/',views.about, name='about'),
    path('login/',views.login, name='login'),
    path('survey/',views.survey, name='survey'),
    path('ContactUs/',views.ContactUs, name='contactus'),
    path('session1/',views.session1, name='session1'),
    path('session2/',views.session2, name='session2'),
    path('session3/',views.session3, name='session3'),
    path('signup/',views.signup, name='signup'),
]

