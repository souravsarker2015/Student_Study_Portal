from django.urls import path

from dashboard import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    # path('notes_details/<int:pk>', views.Notes_Details.as_view(), name='notes_details'),
    path('notes_details/<int:pk>/', views.note_detail, name='notes_details'),
    path('homework/', views.homework, name='homework'),
    path('update_homework/<int:pk>/', views.update_homework, name='update_homework'),
    path('delete_homework/<int:pk>/', views.delete_homework, name='delete_homework'),
    path('youtube/', views.youtube_view, name='youtube'),
    path('todo/', views.todo_view, name='todo'),
    path('update_todo/<int:pk>/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('books/', views.book, name='books'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('wiki/', views.wiki, name='wiki'),
    path('conversion/', views.conversion, name='conversion'),


]
