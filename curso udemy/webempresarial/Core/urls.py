from django.urls import path
from Core import views as coreviews


urlpatterns = [
    path('', coreviews.home, name='home'),
    path('about/', coreviews.about, name='about'),
    path('contact/', coreviews.contact, name='contact'),
    path('store/', coreviews.store, name='store'),
    path('blog/', coreviews.blog, name='blog'),
    path('sample/', coreviews.sample, name='sample'),
    path('services/', coreviews.services, name='services'),
]
