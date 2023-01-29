from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerialzier):
    class Meta:
        model = Blog
        exclude = ['created_at' , 'updated_at']
