from django.shortcuts import render


def getMainPage(request):
    devname = "presly4"
    return render(request, 'main.html', locals())