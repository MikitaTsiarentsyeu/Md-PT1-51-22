"""Defines URL patterns for notebook_project."""

from django.urls import path

from . import views

app_name = 'notebook_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for changing topic name
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),
    # Page for adding a new note
    path('new_note/<int:topic_id>/', views.new_note, name='new_note'),
    # Page for editing a note.
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    # Delete note
    path('topic/<int:note_id>/<int:topic_id>/', views.delete_note, name='delete_note'),
    # Detail page for a single note.
    path('view_note/<int:note_id>/<int:topic_id>/', views.view_note, name='view_note'),
    # View to delete topic.
    path('delete_topic/<int:topic_id>/', views.delete_topic, name='delete_topic'),
]