from django.shortcuts import render


def index(request):
    return render(request, "test_app/test.html")
