from rest_framework import serializers

from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'ongoing_chapters', 'finished_fictions', 'favorite_fictions']