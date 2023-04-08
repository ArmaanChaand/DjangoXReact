from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from User.models import CustomUser
from .models import Note
from .forms import CreateNote
import json
# Create your views here.

def getAllNotes(request):
    user = request.user
    notes = Note.objects.all()
    all_notes = []
    for note in notes:
        obj = {}
        obj['id'] = note.id
        obj['title'] = note.title
        obj['body'] = note.body
        obj['maker'] = note.maker.username
        all_notes.append(obj)
    data = {
        'all_notes': all_notes
    }
    return JsonResponse(data)

def RegisterView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "register.html")

def LoginView(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "login.html")

@login_required(login_url="login-view")
def NoteView(request, pk):
    try:
        the_note = Note.objects.get(id=pk)
        if request.user == the_note.maker:
            context = {
                "the_note" : the_note
            }
            return render(request, "note_view.html", context)
        else:
            return render(request, "NotAllowed.html", {})
    except ObjectDoesNotExist:
        return redirect("/")

@login_required(login_url="login-view")
def NewNoteApi(request):
    if request.method == "POST":
        form = CreateNote(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.maker = request.user
            new_note.save()
            pk = new_note.pk
            data = {
                "success": True,
                "redirect_to": f"/note/{pk}/"
            }
            return JsonResponse(data)
        else:
            data = {
                "success": False,
                "error":True,
                "errors":form.errors
            }
            return JsonResponse(data)

@login_required(login_url="login-view")
def deleteNoteApi(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            the_note = Note.objects.get(id=data['the_note_id'])
            if request.user == the_note.maker:
                the_note.delete()
                data = {
                    "success": True,
                    "redirect_to": '/'
                }
            else:
                data = {
                    "success": False,
                    "error": 'User Not Allowed'
                }
        except ObjectDoesNotExist:
            data = {
                "success": False,
                "error": 'Object Does Not Exist'
            }
        return JsonResponse(data)


