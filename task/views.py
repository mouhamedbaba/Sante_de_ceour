from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import *
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def forbiden(request):
    return render(request, 'task/pages/forbiden.html')

def index(request):
    user = request.user
    workspaces = Workspace.objects.filter(user = user.pk)
    context = {
        'workspaces' : workspaces
    }
    if user.username != "precieuxMBL" :
        return redirect('forbiden')
    return render(request, 'task/pages/home.html', context)

def workspace(request, user , pk):
    workspace = get_object_or_404(Workspace, pk = pk)
    columns = WorkspaceColumn.objects.filter(workspace = workspace.pk)
    cards = ColumnCard.objects.all()
    
    context = {
        'workspace' : workspace,
        'columns' : columns,
        'cards' : cards,
    }
    return render(request, 'task/pages/workspace.html', context)

@csrf_exempt
def addCard(request):
    data = {
        "message" : 'Forbiden'
    }
    if request.POST :
        card = ColumnCardForm(request.POST)
        if card.is_valid() :
            card.save()
            data = {
                'success' : True
            }
        else :
            print(card.errors)
            data = {
                'success' : False
            }
    return JsonResponse(data)


@csrf_exempt
def addColumn(request):
    if request.POST :
        column = WorkspaceColumnForm(request.POST)
        workspace_pk = request.POST['workspace']
        workspace = Workspace.objects.get(pk = workspace_pk)
        owner = workspace.user
        if column.is_valid() :
            column.save()
        else :
            print(column.errors)
    return redirect(f'../workspace/{owner}/{workspace_pk}')

# def edit_card(request, pk):
#     if request.POST:
#         card =  ColumnCard.objects.get(pk = pk)

#         pk = card.column.workspace.pk
#         owner = card.column.workspace.user
#         form = ColumnCardForm(request.POST, request.FILES, instance= card)
#         if form.is_valid():
#             form.save()
#         else :
#             print(form.errors)
#     return redirect(f'../workspace/{owner}/{pk}')

@csrf_exempt
def update_card_title(request, card_pk):
    if request.POST :
        card = ColumnCard.objects.filter(pk=card_pk)
        new_title = request.POST['new_title']
        # new_title = "Ce titre a ete modifie"
        card.update(title = new_title)
        data = {
            'success' : True
        }
        status=200
    else :
        data = {
            'success' : False
        }
        status=403
    return JsonResponse(data)

@csrf_exempt
def update_column(request):
    if request.POST:
        class Actions() :
            delete = 'delete'
            update = 'update_title'  
        data={}
        pk = request.POST['pk']
        action = request.POST['action']
        column = WorkspaceColumn.objects.filter(pk=pk)
        if action == Actions.delete :
            column.delete()
            data = {
                'success' : True,
                'action' : action,
            }
        elif action == Actions.update :
            title = request.POST['title']
            
            column.update(title = title)
            data = {
                'success' : True,
                'action' : action,
                'new_title' : title
            }
        else :
            return HttpResponse(status=403)
        return JsonResponse(data)
    else :
        return HttpResponse(status=403)
    