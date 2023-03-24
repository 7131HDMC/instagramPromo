from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from instaPrometer.forms import InstagramReporterForm
from instagramPromoter.tasks import run_insta_comments_task
# Create your views here.

# @login_required
def home_view(request):    
    context ={
        "running": False
    }
    context['form'] = InstagramReporterForm()
    return render(request, "home.html", context)

# @login_required
def run_insta_comments(request):
    if request.method == "POST":  
        form = InstagramReporterForm(request.POST) 
        # data = form.cleaned_data
        if form.is_valid():  
            try:  
                run_insta_comments_task(form.cleaned_data)
            except Exception as ex:  
                print("Exception: ")
                print(ex)
                print(form.cleaned_data)
                return HttpResponse("error 2")  

    return HttpResponse(form.errors) 