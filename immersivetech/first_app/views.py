mfrom django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Stat, User

# Create your views here.
def index(request):
    stats_list = Stat.objects.order_by('tag')
    stats_dict = {'stats': stats_list}
    # helpDict = {'insert_me': 'HELP PAGE'}
    return render(request, 'first_app/index.html', context=stats_dict)

def help(request):
    helpDict = {'insert_me': 'HELP PAGE'}
    return render(request, 'first_app/help.html', context=helpDict)

def users(request):
    users_list = User.objects.order_by('id')
    user_dict = {'users': users_list}
    return render(request, 'first_app/users.html', context=user_dict)
