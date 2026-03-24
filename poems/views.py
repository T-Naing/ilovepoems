from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Poem, Poet
from django.template import loader
from django.shortcuts import get_object_or_404

def index(request):
    featured_poems = Poem.objects.filter(featured=True).select_related('poet')
    
    context = {"featured_poems": featured_poems}

    # return HttpResponse(template.render(context, request))
    return render(request, "poems/index.html", context)

def poem(request, poem_id):
    poem_obj = get_object_or_404(Poem, pk=poem_id)
    context = {"selected_poem": poem_obj}

    # return HttpResponse(template.render(context, request))
    return render(request, "poems/poem.html", context)

def poet(request, poet_id):
    poet = get_object_or_404(Poet, pk= poet_id)
    poem_list = Poem.objects.filter(poet= poet_id)

    context = {
        "poet": poet,
        "poem_list": poem_list
    }

    return render(request, "poems/poet.html", context)