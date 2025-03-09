from django.urls import path

from .views import index, other_page, FSLoginView, profile, FSLogout, topic_page, lesson_page


app_name = 'main'

urlpatterns = [
    path('accounts/logout/', FSLogout.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', FSLoginView.as_view(), name='login'),
    path('topic/lesson/<int:lesson_id>/', lesson_page, name='lesson'),
    path('<str:page>/', topic_page, name='topic'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]