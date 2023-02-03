from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
# from rest_framework.views import APIView
from .models import User,Book
from .serializers import UserSerializer,BookSerializer,LogInSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView 
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed




# class UserList(genaricAPIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Book.objects.all()
#         serializer = UserSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserList(GenericAPIView):
    serializer_class=UserSerializer
    def post(self,request):
        serializer= UserSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            print(request.data)
            serializer.save()
            return Response({"message":"successfully registered","success": True},status=status.HTTP_201_CREATED)
        return Response({"message":"abc","success":False},status=status.HTTP_208_ALREADY_REPORTED) 


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserSerializer 

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer
 
    def get(self,request,pk,**kwargs):
        print(pk)
        user = User.objects.filter(id=pk)   
        print(user)
        if len(user) ==1:
            queryset = Book.objects.all()
            serial_ = BookSerializer(queryset, many = True)            
            return Response({"message":serial_.data})
        return Response("User not found")
 
 
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer


class LogInAPIView(GenericAPIView):
    
    serializer_class = LogInSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request):
       
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
       
        if user is None:

           return Response({"message":"user not found","success": True},status=status.HTTP_404_NOT_FOUND)  
        if user.password == password: 
            print(user.password+"nik")  
            return Response({"message":"successfully logged in","success": True},status=status.HTTP_200_OK)  
        else:
             return Response({"message":"Incorrect pass","success": False},status=status.HTTP_401_UNAUTHORIZED)
    

 