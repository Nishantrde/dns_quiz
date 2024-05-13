from django.shortcuts import render
from .models import *

def index(request):
    return render(request, "index.html")

def r1(request):
    
    if request.method == 'GET':
        id = int(request.GET.get("id"))

        if request.GET.get("score"):
            score = request.GET.get("score")
            print(score)
            if int(score) == 1:
                team = Team.objects.get(team_id=id-1)
                team.score+=5
                team.save()
                print(team.team_name, team.score)
        
        quest = Rounds.objects.get(round_id=0)
        team = Team.objects.all()
        ques = quest.quests.all()[id]
        return render(request, "r1.html", {"quest": ques, "id" : id,
                                           "t1" : team[0].score,
                                           "t2" : team[1].score,
                                           "t3" : team[2].score,
                                           "t4" : team[3].score})

def r1_ans(request):
    id = int(request.POST.get("id"))
    quest = Rounds.objects.get(round_id=0)
    ques = quest.quests.all()[id].ans
    print(ques, "r1_ans")
    return render(request, "r1_ans.html", {"quest": ques, "id" : id+1})


