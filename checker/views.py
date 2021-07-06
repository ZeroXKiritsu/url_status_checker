from django.contrib.admin.views.decorators import staff_member_required
import json
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import URL
import requests

# Create your views here.
@staff_member_required
def index(request):
    urls = URL.objects.all()
    context = [
        {
        "is_paused": 1 if url.is_paused == True else 0,
        "check_interval": url.check_interval,
        "id": url.id,
        "url": url.url,
        "status": url.status
        }
        for url in urls
    ]
    print(context)
    return render(request, "checker/index.html", context={'urls': context})

def check_url(request):
    id = int(request.POST["url_id"][0])
    try:
        url = URL.objects.get(id=id)
    except URL.DoesNotExist:
        return JsonResponse(data={
            "is_deleted": 1,
            "url_id": id,
        })
    if not url.is_paused:
        try:
            status = requests.head(url.url).status_code
        except requests.ConnectionError:
            status = 404
        url.status = status
        url.save()
    return HttpResponse(json.dumps({
        "is_deleted": 0,
        "url_id": id,
        "status": url.status,
        "check_interval": url.check_interval,
        "is_paused": 1 if url.is_paused == True else 0
    }), content_type="application/json")


def update_url(request):
    id = request.POST["url_id"][0]
    try:
        url = URL.objects.get(id=id)
        url.is_paused = not url.is_paused
        url.save()
    except URL.DoesNotExist:
        return JsonResponse(data={
            "is_deleted": 1,
            "url_id": id,
        })
    return HttpResponse(
        json.dumps({
            "status": "resume" if url.is_paused else "pause",
            "url_id": id,
        }),
        content_type="application/json"
    )


