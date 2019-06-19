#from django.shortcuts import render
#from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# First I try viewsets variant but can't find how to redefine list and detail view fileds

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all().order_by('create_date')
#     serializer_class = TaskSerializer

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = TagSerializer(queryset, many=True)
#         return Response(serializer.data)


class task_root(APIView):
    def get(self, request):
        task = Task.objects.all()
        serialized = TaskSerializerList(task, many=True)
        return Response(serialized.data)
    
    def post(self, request):
        serialized = TaskSerializerCreate(data=request.data)
        if serialized.is_valid(raise_exception=True):
            article_saved = serialized.save()
            return Response({"success": "true"})


class task_detail(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serialized = TaskSerializerDetail(task)
            return Response(serialized.data)
        except Task.DoesNotExist:
            return Response({"error": "object not found"})


class tag_root(APIView):
    def get(self, request):
        tag = Tag.objects.all()
        serialized = TagSerializerList(tag, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = TagSerializerCreate(data=request.data)
        if serialized.is_valid(raise_exception=True):
            article_saved = serialized.save()
            return Response({"success": "true"})


class tag_detail(APIView):
    def get(self, request, pk):
        try:
            tag = Tag.objects.get(pk=pk)
            serialized = TagSerializerDetail(tag)
            return Response(serialized.data)
        except Tag.DoesNotExist:
            return Response({"error": "object not found"})
        