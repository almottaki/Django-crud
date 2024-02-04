from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import TODO


def index(request):
    context = {"todos": TODO.objects.order_by("-create_at")}
    template = loader.get_template("polls/index.html")
    return HttpResponse(template.render(context, request))


def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            todo = TODO(text=text)
            todo.save()
            return redirect('index')  # Redirect to the to-do list page
    else:
        form = TodoForm()

    return render(request, 'polls/add_todo.html', {'form': form})

def update_todo(request, id):
    todo = TODO.objects.get(id=id)
    return HttpResponse("Hello, world. You're at the polls update_todo.")


def delete_todo(request, id):
    try:
        todo = TODO.objects.get(id=id)
        todo.delete()
    except TODO.DoesNotExist:
        return HttpResponse("Not Found !!")
    return redirect('index')


def details_todo(request, id):
    todo = TODO.objects.get(id=id)
    context = {"todo":todo}
    template = loader.get_template("polls/details.html")
    return HttpResponse(template.render(context, request))