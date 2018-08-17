from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {"text": "hello", "number":100}
    return render(request, 'relative_urls/index.html', context_dict)

def other(request):
    return render(request, 'relative_urls/other.html')

def relative(request):
    return render(request, 'relative_urls/relative_url_template.html')
