from django.shortcuts import render


def handler404(request):
        data = {}
        return render(request,'public/404.html', data)
