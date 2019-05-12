from django.shortcuts import render


def getTopPage(request):
    return render(request, 'top.html', locals())