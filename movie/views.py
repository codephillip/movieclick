from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def download(request, pk):
    return render(request, 'download.html', {
        'pk': pk
    })