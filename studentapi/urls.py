from django.urls import path
from . import views


urlpatterns = [
    path('students',views.all_students_view),
    path('students/<int:id>',views.get_edit_or_delete_student),
]