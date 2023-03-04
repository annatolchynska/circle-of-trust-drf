from rest_framework import serializers
from .models import MemoComment


class MemoCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        '''checks if owner is the user'''
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = MemoComment
        fields = [
            'id', 'owner', 'memo_post', 'created_on', 'content',
            'is_owner', 'profile_id', 'profile_image',
        ]


class MemoCommentDetailSerializer(MemoCommentSerializer):
    memo_post = serializers.ReadOnlyField(source='memo_post.id')
