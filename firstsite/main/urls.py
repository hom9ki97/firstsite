from django.urls import path

from .views import index, other_page, FSLoginView, profile, FSLogout, topic_page, lesson_page, upload_code
from .views import lesson_add, add_hw, del_exemple_code, home_work_page, upload_code_hw, add_topic, del_topic, del_lesson


app_name = 'main'

urlpatterns = [
    path('accounts/logout/', FSLogout.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', FSLoginView.as_view(), name='login'),
    path('upload_hw/', upload_code_hw, name='upload_code_hw'),
    path('upload/', upload_code, name='upload_code'),
    path('topic/lesson/homework/<int:home_work_id>/', home_work_page, name='home_work_page'),
    path('topic/lesson/del/<int:code_example_id>/', del_exemple_code, name='del_exemple_code'),
    path('topic/lesson/add_lesson/', lesson_add, name='lesson_add'),
    path('topic/lesson/<int:lesson_id>/', lesson_page, name='lesson'),
    path('topic/lesson/<int:lesson_id>/add_hw/', add_hw, name='add_hw'),
    path('<int:lesson_id>//del_lesson/', del_lesson, name='del_lesson'),
    path('<int:language_id>/add_topic/', add_topic, name='add_topic'),
    path('<int:topic_id>/del_topic/', del_topic, name='del_topic'),
    path('<int:language_id>/', topic_page, name='topic'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]