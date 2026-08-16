# from django.urls import path
# from crud_app.views import indexPage,student,studentList,deleteStudent,editStudent
# urlpatterns = [
#     path('', indexPage, name="index_page"),
#     path('addStudent', student, name="add_student"),
#     path('studentList',studentList, name="student_list" ),
#     path('deleteStudent/<int:sid>/', deleteStudent, name="delete_student"),
#     path('editStudent/<int:sid>/', editStudent, name="edit_student"),
# ]


# =======================================================================
from django.urls import path
from crud_app.views import index,student_name,studentList,deleteStudent,editStudent

urlpatterns = [
    path('',index, name = "index_page"),
    path('add_student/', student_name, name='add_student'),
    path('studentList/',studentList, name='student_list'),
    path('deleteStudent/<int:sid>/', deleteStudent, name='delete_student'),
    path('editStudent/<int:sid>/',editStudent, name="edit_student")
]