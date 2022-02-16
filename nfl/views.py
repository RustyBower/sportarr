import nflgame

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics


from .models import File, Team, Game
from .serializers import GameSerializer, WeeksSerializer


def index(request):
    data = Game.objects.values_list('season', flat=True).order_by('-season').distinct()
    template = loader.get_template('schedule/index.html')
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))


class Games(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class Season(APIView):
    def get(self, request, year):
        games = Game.objects.filter(season=year).all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class GameType(APIView):
    def get(self, request, year, gametype):
        if gametype.upper() == 'POST':
            games = Game.objects.filter(season=year).filter(gametype__in=['WC', 'DIV', 'CON', 'SB']).all()
        else:
            games = Game.objects.filter(season=year).filter(gametype=gametype.upper()).all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class Week(APIView):
    def get(self, request, year, gametype, week):
        if gametype.upper() == 'POST':
            games = Game.objects.filter(season=year).filter(gametype__in=['WC', 'DIV', 'CON', 'SB']).filter(week=week).all()
        else:
            games = Game.objects.filter(season=year).filter(gametype=gametype.upper()).filter(week=week).all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)


class Weeks(APIView):
    def get(self, request, year):
        weeks = Game.objects.filter(season=year).values('gametype', 'week', 'season').distinct()
        serializer = WeeksSerializer(weeks, many=True)
        return Response(serializer.data)

