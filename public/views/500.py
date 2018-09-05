from django.shortcuts import render


def handler500(request):
        return render(request,'public/500.html', status=404)
