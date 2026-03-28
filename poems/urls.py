from django.urls import path
from . import views

app_name = "poems"
urlpatterns = [
    path('',views.index, name = "index"),
    path('poems/', views.poems, name='poems'),
    path('poets/', views.poets, name='poets'),
    path('<int:poem_id>/', views.poem, name='poem'),
    path('poet/<int:poet_id>/', views.poet, name='poet'), 
     
]   

