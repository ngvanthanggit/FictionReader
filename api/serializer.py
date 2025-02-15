from rest_framework import serializers

from accounts.models import User
from fiction.models import Fiction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'ongoing_chapters', 'finished_fictions', 'favorite_fictions']
        
class FictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiction
        fields = '__all__'