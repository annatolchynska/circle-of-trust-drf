from django.urls import path
from like_memo import views


urlpatterns = [
    path('like_memo/', views.MemoLikesList.as_view()),
    path('like_memo/<int:pk>/', views.MemoLikesDetail.as_view()),
]
