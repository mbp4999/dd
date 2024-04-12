from rest_framework import serializers
from .models import *


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booksmodel
        fields = '__all__'
        
    
    