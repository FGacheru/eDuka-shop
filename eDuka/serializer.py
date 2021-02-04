from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import Product

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = ['content', 'author']