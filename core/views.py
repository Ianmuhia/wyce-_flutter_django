# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment


class PostView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()


class CommentListView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)
