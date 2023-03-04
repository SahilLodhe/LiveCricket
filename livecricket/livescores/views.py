from django.shortcuts import render
import requests
from livecricket.settings import URL,APIKEY
from django import http
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from livescores import models
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
import pycricbuzz
from pycricbuzz import *
from pycricbuzz import Cricbuzz
import json
import math
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# session.get(url)

# Create your views here.

class home(TemplateView):
    template_name = 'home.html'

def trial(request):
    url = 'https://cricbuzz-cricket.p.rapidapi.com/stats/v1/rankings/batsmen'

    headers = {
        "X-RapidAPI-Key": APIKEY,
        "X-RapidAPI-Host": URL
    }

    response = requests.request("GET", url, headers=headers).json()
    players = response
    # print(response.text)
    context = {}
    context['trial'] = response
    context['players'] = []
    
    return render(request,'home.html',context)

# def trial(request):
#     from pycricbuzz import Cricbuzz
#     import json
#     c = Cricbuzz()
#     matches = c.matches()
#     data = {}
#     data['data'] = (json.dumps(matches,indent=4)) #for pretty prinitng
#     return render(request,'home.html')

# def trial(request):
#     cBuzz = Cricbuzz()
#     matches = cBuzz.matches()
#     metaData = {}
#     data = {}
#     for match in matches:
#         if match.get('mchstate') == 'preview':
#             data['venue'] = match.get('venue_name')
#             data['team1'] = match.get('team1').get('name')
#             data['team2'] = match.get('team2').get('name')
#             return render(request,'home.html',data)
    
#         elif match.get('mchstate') == 'complete' or match.get('mchstate') == 'innings break' or match.get('mchstate') == 'inprogress':
#             metaData['matchId'] = match.get('id')
#             metaData['venue'] = match.get('venue_name')
#             metaData['team1'] = match.get('team1').get('name')
#             metaData['team2'] = match.get('team2').get('name')
#             data = getScore(cBuzz,metaData)
#             return render(request,'home.html',data)
#     return HttpResponse("no matches now!")

# def getScore(cBuzz,metaData):
#     data = {}
#     livescore = cBuzz.livescore(metaData.get('matchId'))
#     # the current bowler
#     bowler = livescore.get('bowling').get('bowler')[0]
#     bowler = calculate_economy(bowler)

#     bow_score = 'nil'
#     for target in livescore.get('batting').get('batsman'):
#         bow_score = int(target.get('runs')) + 1
#     batsmen_details = retrieve_batter_det(livescore)
    
#     data['team2'] = metaData.get('team2')
#     data['team1'] = metaData.get('team1')
#     data['venue'] = metaData.get('venue')
#     data['score'] = livescore.get('batting').get('score')[0].get('runs')
#     data['wickets'] = livescore.get('batting').get('score')[0].get('wickets')
#     data['overs'] = livescore.get('batting').get('score')[0].get('overs')
#     data['target'] = bow_score
#     data['bowler'] = livescore.get('bowling').get('bowler')[0]
#     data['bat'] = batsmen_details
#     data['c_rr'],data['r_rr'] = calculate_runrate(data.get('score'),data.get('target'),data.get('overs'))
#     return data

# # retrieving the batsmen details 
# def retrieve_batter_det(livescore):
#     batsmen_details = []
#     for batsmen in livescore.get('batting').get('batsman'):
#         runs = int(batsmen.get('runs'))
#         balls = int(batsmen.get('balls'))
#         if balls == 0:
#             sr = 0
#         else:
#             sr = round((runs/balls)*100,2)
#         batsmen['sr'] = sr
#         batsmen_details.append(batsmen)
#     return batsmen_details

# def calculate_runrate(score,target,currentOvers):
#     runs = int(score)
#     overs = float(currentOvers)
#     balls = int(overs) * 6
#     extraBalls = int(overs*10)%10
#     balls = extraBalls + balls
#     currentRR = round((runs * 6)/balls,2)
#     requiredRR = 'nil'

#     if target != 'nil' and balls != 120:
#         remainingRuns = int(target) - runs
#         remainingBalls = 120 - balls
#         requiredRR = round((remainingRuns * 6)/remainingBalls,2)
#     return currentRR,requiredRR

# def calculate_economy(bowler):
#     runs = int(bowler.get('runs'))
#     overs = float(bowler.get('overs'))
#     balls = int(overs) * 6
#     extraBalls = int(overs*10)%10
#     balls = extraBalls + balls
#     eco = runs/balls
#     bowler['eco'] = eco
#     return bowler 


