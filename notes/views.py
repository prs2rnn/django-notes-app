from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods

from .forms import NoteForm
from .models import Note


@login_required
def notes_list(request):
    notes = Note.objects.filter(author=request.user)

    return render(request, 'notes/index.html', {'notes': notes})


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id, author=request.user)

    return render(request, 'notes/detail.html', {'note': note})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm()
    return render(request, 'notes/form.html', {'form': form, 'title': 'Create note'})


@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id, author=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(instance=note)

    return render(
        request, 'notes/form.html', {'form': form, 'note': note, 'title': 'Edit note'}
    )


@require_http_methods(['GET', 'POST'])
@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id, author=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')

    return render(request, 'notes/confirm_delete.html', {'note': note})
