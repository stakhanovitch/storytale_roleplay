from django.shortcuts import render


def handler500(request):
        data = {}
        return render(request,'public/500.html', data)
