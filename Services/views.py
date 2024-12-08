from django.shortcuts import render,redirect
from Services.models import Url
from django.contrib import messages
import random,string
import datetime
from django.contrib.sites.shortcuts import get_current_site
# from django.http import JsonResponse

def getAlias():
    return "".join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8)])

# Create your views here.
def dashboard(request):
    if request.method == "POST":
        URL = request.POST["URL"]
        alias = request.POST.get("alias",None)
        if not alias:
            alias = getAlias()
        try:
            Url.objects.create(user=request.user,target_url=URL,alias=alias).save()
            messages.success(request,"success")
            return redirect("dashboard")
        except:
            messages.error(request,"alias already under use")
            return render(request,"dashboard.html",{"url":URL,"alias":alias})
    
    site = get_current_site(request)
    return render(request,"dashboard.html",{"domain":site})


def redirect_to_target_page(request,alias):
    obj = Url.objects.get(alias=alias)
    URL = obj.target_url
    obj.clicks += 1
    obj.clicks_per_day += 1
    obj.clicks_per_month += 1
    obj.save()
    return redirect(URL)

def delete_url(request,url_id):
    if request.method == "POST":
        try:
            url = Url.objects.get(id=url_id,user=request.user)
            url.delete()
        except Url.DoesNotExist:        
            pass
    return redirect('dashboard')

def analysis(request, alias):
    # Get the URL object for the given alias
    obj = Url.objects.get(alias=alias)

    # Get the clicks for the URL
    clicks = obj.clicks

    # Generate a random date for the graph
    date = datetime.date(random.randint(2020, 2024), random.randint(1, 12), random.randint(1, 28))

    # Render the graph template with the URL and clicks
    return render(request, "analysis.html", {"url": obj.target_url, "clicks": clicks, "date": date})
