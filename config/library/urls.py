from django.urls import path
from library import views
urlpatterns = [
    
   path('home/', views.home,name='home'),
   path('book/', views.book,name='book'),
   path('book/<str:id>/detail/', views.detail,name='detail')
   
    
]