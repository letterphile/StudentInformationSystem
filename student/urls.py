from django.urls import path
from . import views
app_name = 'student'
urlpatterns = [
   path('filter/',views.filter_form,name='filter_form'),
   path('edit/<int:student_id>',views.student_form,name='student_form'),
   path('result/',views.show_result,name='show_result'),
   path('add/',views.student_add,name='student_add'),
   path('delete/<int:student_id>',views.student_delete,name='student_delete'),
]