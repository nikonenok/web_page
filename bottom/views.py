from django.shortcuts import render


def getBottomPage(request):
    devname = "presly4"
    return render(request, 'bottom.html', locals())