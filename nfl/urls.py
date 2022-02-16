from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/games', views.Games.as_view()),
    path('api/v1/games/<int:year>', views.Season.as_view()),
    path('api/v1/games/<int:year>/weeks', views.Weeks.as_view()),
    path('api/v1/games/<int:year>/<str:gametype>', views.GameType.as_view()),
    path('api/v1/games/<int:year>/<str:gametype>/<int:week>', views.Week.as_view()),
]
