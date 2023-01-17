from django.shortcuts import render, redirect
from .models import Topic, Note
from .forms import TopicForm, NoteForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.

def index(request):
    """The home page for Notebook app"""
    viewed_notes = request.session.get("viewed_notes", [])
    notes = []
    for viewed_note in viewed_notes:
        if Note.objects.filter(id=viewed_note).count() > 0:
            note = Note.objects.get(id=viewed_note)
            notes.append(note)
    viewed_notes = notes
    return render(request, 'notebook_app/index.html', {'viewed_notes': viewed_notes}, )


@login_required
def topics(request):
    """Shows topic list"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'notebook_app/topics.html', context)


@login_required
def topic(request, topic_id):
    """shows topic info"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    notes = topic.note_set.order_by('-date_added')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'notebook_app/topic.html', context)


@login_required
def new_topic(request):
    """defines new topic"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, owner=request.user)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('notebook_app:topics')
    context = {'form': form}
    return render(request, 'notebook_app/new_topic.html', context)

@login_required
def edit_topic(request, topic_id):
    """edits topic name"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TopicForm(owner=request.user, instance=topic)
    else:
        form = TopicForm(request.POST, owner=request.user, instance=topic)
    if form.is_valid():
        new_topic = form.save(commit=False)
        new_topic.owner = request.user
        new_topic.save()
        return redirect('notebook_app:topics')
    context = {'topic': topic, 'form': form}
    return render(request, 'notebook_app/edit_topic.html', context)


@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        topic.delete()
    return redirect('notebook_app:topics')


@login_required
def new_note(request, topic_id):
    """adds new note for exact topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = NoteForm(user=request.user)
    else:
        form = NoteForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('notebook_app:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'notebook_app/new_note.html', context)


@login_required
def edit_note(request, note_id):
    """Edits note"""
    note = Note.objects.get(id=note_id)
    topic = note.topic
    # topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = NoteForm(user=request.user, instance=note)
    else:
        form = NoteForm(request.POST, request.FILES, user=request.user, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notebook_app:topic', topic_id=topic.id)
    context = {'note': note, 'topic': topic, 'topics': topics, 'form': form}
    return render(request, 'notebook_app/edit_note.html', context)


@login_required
def delete_note(request, note_id, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method == 'POST':
        note = Note.objects.get(id=note_id)
        note.delete()
    return redirect('notebook_app:topic', topic_id=topic.id)


@login_required
def view_note(request, note_id, topic_id):
    """shows note info"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    else:
        viewed_notes = request.session.get("viewed_notes", [])
        if note_id not in viewed_notes:
            viewed_notes.append(note_id)
        request.session["viewed_notes"] = viewed_notes
        if request.method == 'GET':
            note = Note.objects.get(id=note_id)
        context = {'topic': topic, 'note': note}
        return render(request, 'notebook_app/view_note.html', context)


# Not implemented
# def upload_images(request):
#     if request.method == "POST":
#         images = request.FILES.getlist('images')
#         for image in images:
#             MultipleImage.objects.create(images=image)
#     images = MultipleImage.objects.all()
#     return render(request, 'imdex.html', {'images': images})
#
