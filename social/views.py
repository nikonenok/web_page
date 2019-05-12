from django.shortcuts import render


def getSocialPage(request):
    devname = "presly4"
    return render(request, 'social.html', locals())