import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from ads.models import Category
from ads.models import Ad


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@csrf_exempt
def get_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.pk,
                "name": category.name,
            })
        return JsonResponse(response, status=200, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        category = Category.objects.create(name=data["name"])
        return JsonResponse({
            "id": category.pk,
            "name": category.name,
        }, status=200, safe=False)


def get_category(request, cid):
    if request.method == "GET":
        category = Category.objects.get(pk=cid)
        return JsonResponse({
            "id": category.pk,
            "name": category.name},
            status=200, safe=False
        )


@csrf_exempt
def get_ads(request):
    if request.method == "GET":
        ads = Ad.objects.all()
        response = []
        for ad in ads:
            response.append({
                "id": ad.pk,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            })
        return JsonResponse(response, status=200, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        ad = Ad.objects.create(name=data["name"],
                               author=data["author"],
                               price=data["price"],
                               description=data["description"],
                               address=data["address"],
                               is_published=data["is_published"])
        return JsonResponse({
                "id": ad.pk,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published
            }, status=200, safe=False)


def get_ad(request, aid):
        ad = Ad.objects.get(pk=aid)
        return JsonResponse({
            "id": ad.pk,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published},
            status=200, safe=False
        )
