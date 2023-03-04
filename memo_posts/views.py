from django.shortcuts import render

from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Memo
from .serializers import MemoSerializer


# idea was taken from DRF_API walkthrough
class MemoList(generics.ListCreateAPIView):
    serializer_class = MemoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Memo.objects.annotate(
        comments_count=Count('memocomment', distinct=True),
        likes_count=Count('like_memo', distinct=True)
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'like_memo__owner__profile',
        'owner__profile',
        'owner__followed__owner__profile',
    ]
    search_fields = [
        'owner__username',
        'content',
        'attention_of',
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoSerializer
    queryset = Memo.objects.annotate(
        comments_count=Count('memocomment', distinct=True),
        likes_count=Count('like_memo', distinct=True)
    ).order_by('-created_on')
