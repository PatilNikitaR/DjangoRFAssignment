from django.urls import path
from . import views


urlpatterns = [
   
    path('',views.UserList.as_view()),
    path('<int:pk>/',views.UserDetail.as_view()),
    path('bookapi/<int:pk>/',views.BookList.as_view()),  #if user is present of gien id then only we can get book list 
    path('bookapii/<int:pk>/',views.BookDetail.as_view()),  # book from its id
    path('login/',views.LogInAPIView.as_view())
]