from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "index"),
    path('<int:poem_id>/', views.poem, name='poem'),
    path('poet/<int:poet_id>/', views.poet, name='poet'), 
]   

