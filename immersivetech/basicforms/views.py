from django.shortcuts import render
from . import forms
from first_app.models import Stat, User
from basicforms.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'basicforms/index.html')

def form_name_view(request):
    form = forms.FormName()

    if (request.method == "POST"):
        form = forms.FormName(request.POST)
        if (form.is_valid()):
            #Do something
            print("VALIDATION SUCCESS")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'basicforms/form_page.html', {'form':form})

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR form not valid')
    return render(request, 'basicforms/users.html', {'form':form})
