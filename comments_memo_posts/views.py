from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import MemoComment
from .serializers import MemoCommentSerializer, MemoCommentDetailSerializer


class MemoCommentList(generics.ListCreateAPIView):
    serializer_class = MemoCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = MemoComment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['memo_post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MemoCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MemoCommentDetailSerializer
    queryset = MemoComment.objects.all()
