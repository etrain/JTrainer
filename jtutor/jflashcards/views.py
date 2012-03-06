from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from jflashcards.models import Clue, Response
from datetime import datetime
from django.http import HttpResponse

def index(request):
    return show_clue(request, get_next_clue())

def clue(request, clue_id):
    c = get_object_or_404(Clue, pk=clue_id)
    return show_clue(request, c)
    
def show_clue(request, c):
    return render_to_response("jflashcards/clue.html", {'clue': c}, 
                              RequestContext(request))
    
def respond(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    c = 'correct' in request.POST
    k = request.POST.get('knew')
    h = request.POST.get('heardof')
    
    res = Response(clue=clue, correct=c, knew=k, heardof=h, response_time=datetime.utcnow())
    res.save()
    
    return show_clue(request, get_next_clue())

def get_next_clue():
    #Gets next clue based on some model. Currently the model is "random"
    return Clue.objects.order_by('?')[0]