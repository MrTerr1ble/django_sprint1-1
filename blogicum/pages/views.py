from django.shortcuts import render


def about(request):
    temlate = 'pages/about.html'
    return render(request, temlate)


def rules(request):
    temlate = 'pages/rules.html'
    return render(request, temlate)