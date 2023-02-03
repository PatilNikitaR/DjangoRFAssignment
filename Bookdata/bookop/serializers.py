from rest_framework import serializers
from .models import User,Book

class UserSerializer(serializers.ModelSerializer):
      class Meta():
          model =  User
          fields = ['id','first_name','last_name','email','phone','password']
          
class BookSerializer(serializers.ModelSerializer):
      class Meta():
          model= Book
          fields = ['id','book_name','description','Author','Price','created_by']

class LogInSerializer(serializers.ModelSerializer):
      class Meta():
        model = User
        fields =['email', 'password']