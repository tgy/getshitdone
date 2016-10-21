from django.shortcuts import render
from django.http import Http404

from todo.models import Board, Task
from todo import status

def tasks(request):

    tasks = Task.objects.all().select_related('board')
    boards = Board.objects.all()

    context = {
        'boards': boards,
        'tasks': tasks,
    }

    return render(request, 'todo/tasks.html', context)

def board(request, slug):

    try:
        board = Board.objects.get(slug=slug)
    except Board.DoesNotExist:
        raise Http404('Board does not exist')

    boards = Board.objects.all()
    tasks = Task.objects.filter(board=board).select_related('board')

    context = {
        'boards': boards,
        'board': board,
        'tasks': tasks,
    }

    return render(request, 'todo/tasks.html', context)
