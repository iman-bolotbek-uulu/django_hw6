from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    membership = models.Membership.objects.all()
    context = {
        'membership': membership,
    }
    return render(request,'index.html', context)


def detail(request, id):
    membership = get_object_or_404(models.Membership, id=id)
    context = {
        'membership': membership,
    }
    return render(request, 'detail.html', context)