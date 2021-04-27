from django.shortcuts import render


def index(request):
    context = {}
    return render(request, "index.html", context=context)


def html(request, filename):
    context = {}
    return render(request, f"{filename}.html", context=context)
