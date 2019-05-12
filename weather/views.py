from django.shortcuts import render


def getWeatherPage(request):
    return render(request, 'weather.html', locals())