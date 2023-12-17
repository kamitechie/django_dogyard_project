from django.urls import path
from . import views

urlpatterns = [
    path('dogs/', views.dogs_list, name='dogs_list'),
    path('', views.home, name='home'),
    path('hospital/', views.hospital, name='hospital_dogs'),
    path('borrowed/', views.borrow, name='borrowed_dogs'),
    path('adopted/', views.adopt, name='adopted_dogs'),
    path('puppies/', views.puppies, name='puppies'),
    path('dogs/apool', views.a_pool, name='a_pool'),
    path('dogs/bpool', views.b_pool, name='b_pool'),
    path('dogs/cpool', views.c_pool, name='c_pool'),
    path('dogs/dpool', views.d_pool, name='d_pool'),
    path('dogs/epool', views.e_pool, name='e_pool'),
    path('dogs/racingpool', views.racing_pool, name='racing_pool'),
    path('family/', views.family, name='family'),
    path('schedule/', views.schedule, name='schedule'),
    path('team/', views.team, name='team'),
    path('information/', views.information, name='info'),
    path('add_new_dog/', views.add_dog, name='add_new_dog'),
    path('add_new_puppy/', views.add_puppy, name='add_new_puppy'),
    path('add_hospital_dog/', views.add_hospital_dog, name='add_hospital_dog'),
    path('add_adopted_dog/', views.add_adoption_dog, name='add_adopted_dog'),
    path('add_borrowed_dog/', views.add_borrow_dog, name='add_borrowed_dog'),
    path('edit_dog/<int:dog_id>/', views.edit_dog, name='edit_dog')

]