import nflgame

from datetime import timezone, datetime, timedelta
import pytz
from django.utils import timezone
from schedule.models import Team, Week

YEAR = 2019
KIND = 'PRE'
games = nflgame.games(YEAR, kind=KIND)

if games:
    for game in games:
        print(game.schedule)
        # Home
        t1 = Team.objects.filter(short_name=game.schedule['home']).first()
        if not t1:
            t1 = Team(short_name=game.schedule['home'])
            t1.save()

        # Away
        t2 = Team.objects.filter(short_name=game.schedule['away']).first()
        if not t2:
            t2 = Team(short_name=game.schedule['away'])
            t2.save()

        if game.schedule['meridiem'] == 'PM':
            hour = int(game.schedule['time'].split(':')[0]) + 12
        else:
            hour = int(game.schedule['time'].split(':')[0])

        # eastern = timezone('US/Eastern')
        d = timezone.make_aware(datetime(game.schedule['year'],
                                         game.schedule['month'],
                                         game.schedule['day'],
                                         hour,
                                         int(game.schedule['time'].split(':')[1])),
                                timezone=pytz.timezone('US/Eastern'))
        print(d)

        w = Week.objects.filter(week=game.schedule['week'], home=t1, away=t2, date=d, kind=KIND, season=YEAR)
        if not w:
            w = Week(week=game.schedule['week'], home=t1, away=t2, date=d, kind=KIND, season=YEAR)
            w.save()
        print('-'*10)
