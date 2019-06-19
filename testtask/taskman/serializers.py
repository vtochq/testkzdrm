from rest_framework import serializers
from .models import *

class TaskSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name')


class TaskSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'tag', 'descr', 'create_date')
        # if you want get not only tag ID set depth=1
        #depth = 1


class TaskSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'tag', 'descr')
    
    def create(self, validated_data):
        tags = validated_data.pop('tag', None)
        instance = Task.objects.create(**validated_data)
        if tags is not None:
            instance.tag.set(tags)
            return instance

class TagSerializerList(serializers.ModelSerializer):    
    class Meta: 
        model = Tag
        fields = ('id', 'name')


class TagSerializerDetail(serializers.ModelSerializer):
    # if you want get not only task ID uncomment line below or write serializer with needed fields
    #tasks = TaskSerializerList(read_only=True, many=True)
    class Meta:
        model = Tag
        fields = ('name', 'tasks')

class TagSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

