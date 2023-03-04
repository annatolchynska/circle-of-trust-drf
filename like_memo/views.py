from django.shortcuts import render

from rest_framework import generics, permissions
from p5_drf_api.permissions import IsOwnerOrReadOnly
from like_memo.models import MemoLikes
from like_memo.serializers import MemoLikesSerializer


class MemoLikesList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = MemoLikesSerializer
    queryset = MemoLikes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MemoLikesDetail(generics.RetrieveDestroyAPIView):
    '''deletes like if owned by user'''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoLikesSerializer
    queryset = MemoLikes.objects.all()
