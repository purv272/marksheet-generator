
from django.urls import path
from . import views

urlpatterns = [
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('teacher/', views.teacher, name='teacher'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/marksheet-file/', views.view_marksheet_file, name='view_marksheet_file'),
    path('teacher/marksheet-file/delete/<int:entry_index>/', views.delete_marksheet_entry, name='delete_marksheet_entry'),
    path('teacher/marksheet-file/edit/<int:entry_index>/', views.edit_marksheet_entry, name='edit_marksheet_entry'),
    # path('contact/',views.contact),  # Removed because contact view does not exist
]

