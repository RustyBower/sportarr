import requests
import xml.etree.ElementTree as ET

from datetime import datetime
import pytz
from django.utils import timezone
from schedule.models import Game, Team


for year in range(2019, 1960, -1):
    print(year)
    # Postseason
    for week in range(22, 16, -1):
        r = requests.get('http://www.nfl.com/ajax/scorestrip?season={}&seasonType=POST&week={}'.format(year, week))
        root = ET.fromstring(r.text)
        # Check if gms key exists
        if root.find('gms'):
            for g in root.iter('g'):
                # Home
                t1 = Team.objects.filter(short_name=g.get('h')).first()
                if not t1:
                    t1 = Team(short_name=g.get('h'))
                    t1.save()

                # Away
                t2 = Team.objects.filter(short_name=g.get('v')).first()
                if not t2:
                    t2 = Team(short_name=g.get('v'))
                    t2.save()

                hour = int(g.get('t').split(':')[0])
                if hour != 12:
                    hour = int(g.get('t').split(':')[0]) + 12

                d = timezone.make_aware(datetime(int(str(g.get('eid'))[0:4]),
                                                 int(str(g.get('eid'))[4:6]),
                                                 int(str(g.get('eid'))[6:8]),
                                                 hour,
                                                 int(g.get('t').split(':')[1])),
                                        timezone=pytz.timezone('US/Eastern'))

                if g.get('gt') == 'SB':
                    week_num = 4
                elif g.get('gt') == 'CON':
                    week_num = 3
                elif g.get('gt') == 'DIV':
                    week_num = 2
                elif g.get('gt') == 'WC':
                    week_num = 1
                else:
                    print('This broke.')

                w = Game.objects.filter(week=week_num, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                if not w:
                    w = Game(week=week_num, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                    w.save()

    # Regular Season
    for week in range(17, 0, -1):
        r = requests.get('http://www.nfl.com/ajax/scorestrip?season={}&seasonType=REG&week={}'.format(year, week))
        root = ET.fromstring(r.text)
        # Check if gms key exists
        if root.find('gms'):
            for g in root.iter('g'):
                # Home
                t1 = Team.objects.filter(short_name=g.get('h')).first()
                if not t1:
                    t1 = Team(short_name=g.get('h'))
                    t1.save()

                # Away
                t2 = Team.objects.filter(short_name=g.get('v')).first()
                if not t2:
                    t2 = Team(short_name=g.get('v'))
                    t2.save()

                hour = int(g.get('t').split(':')[0])
                if hour != 12:
                    hour = int(g.get('t').split(':')[0]) + 12

                d = timezone.make_aware(datetime(int(str(g.get('eid'))[0:4]),
                                                 int(str(g.get('eid'))[4:6]),
                                                 int(str(g.get('eid'))[6:8]),
                                                 hour,
                                                 int(g.get('t').split(':')[1])),
                                        timezone=pytz.timezone('US/Eastern'))

                w = Game.objects.filter(week=week, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                if not w:
                    w = Game(week=week, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                    w.save()

    # Preseason
    for week in range(4, -1, -1):
        r = requests.get('http://www.nfl.com/ajax/scorestrip?season={}&seasonType=PRE&week={}'.format(year, week))
        root = ET.fromstring(r.text)
        # Check if gms key exists
        if root.find('gms'):
            for g in root.iter('g'):
                # Home
                t1 = Team.objects.filter(short_name=g.get('h')).first()
                if not t1:
                    t1 = Team(short_name=g.get('h'))
                    t1.save()

                # Away
                t2 = Team.objects.filter(short_name=g.get('v')).first()
                if not t2:
                    t2 = Team(short_name=g.get('v'))
                    t2.save()

                hour = int(g.get('t').split(':')[0])
                if hour != 12:
                    hour = int(g.get('t').split(':')[0]) + 12

                d = timezone.make_aware(datetime(int(str(g.get('eid'))[0:4]),
                                                 int(str(g.get('eid'))[4:6]),
                                                 int(str(g.get('eid'))[6:8]),
                                                 hour,
                                                 int(g.get('t').split(':')[1])),
                                        timezone=pytz.timezone('US/Eastern'))

                w = Game.objects.filter(week=week, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                if not w:
                    w = Game(week=week, home=t1, away=t2, date=d, gametype=g.get('gt'), season=year)
                    w.save()

'''
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

        w = Game.objects.filter(week=game.schedule['week'], home=t1, away=t2, date=d, kind=KIND, season=YEAR)
        if not w:
            w = Game(week=game.schedule['week'], home=t1, away=t2, date=d, kind=KIND, season=YEAR)
            w.save()
'''