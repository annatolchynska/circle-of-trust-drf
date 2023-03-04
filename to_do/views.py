from rest_framework import generics, permissions, filters
from p5_drf_api.permissions import IsOwnerOrReadOnly
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'task_title',
        'due_date',
    ]

    def perform_create(self, serializer):
        '''makes sure user is connected to the task'''
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    '''edit or delete if owned by user'''
    serializer_class = TodoSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Todo.objects.all()
