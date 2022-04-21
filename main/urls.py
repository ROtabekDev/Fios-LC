from django.urls import  path
from .views import home_page, about_page, courses_page, contact_page, appeal_page

urlpatterns = [
    path('', home_page, name="home_page"),
    path('about/', about_page, name='about_page'),
    path('courses/', courses_page, name='courses_page'),
    path('contact/', contact_page, name='contact_page'),
    path('appeal/', appeal_page, name='appeal_page'),
]