from .models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    home = serializers.SlugRelatedField(many=False,
                                        read_only=True,
                                        slug_field='name')
    away = serializers.SlugRelatedField(many=False,
                                        read_only=True,
                                        slug_field='name')

    class Meta:
        model = Game
        fields = ['season', 'week', 'gametype', 'home', 'away', 'date']


class WeeksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['week', 'gametype', 'season']
