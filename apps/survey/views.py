from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html", request.session)

def info(request):
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['name'] = request.POST['name']
    request.session['comment'] = request.POST['comment']
    if request.session['number'] != int:
        request.session['number'] == 0
        request.session['number'] += 1
    return redirect("/result")






