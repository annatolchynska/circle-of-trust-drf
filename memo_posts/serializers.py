from rest_framework import serializers
from like_memo.models import MemoLikes
from .models import Memo


# the idea was taken for DRF_API walkthrough
class MemoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        '''checks if user is owner'''
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        '''shows user,who liked memo_post,so owner can unlike it'''
        user = self.context['request'].user
        if user.is_authenticated:
            like = MemoLikes.objects.filter(
                owner=user, memo_post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Memo
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_on', 'content', 'like_id', 'attention_of',
            'comments_count',
            'likes_count',
        ]