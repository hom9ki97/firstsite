from django.urls import path

from .views import index, other_page, FSLoginView, profile, FSLogout


app_name = 'main'

urlpatterns = [
    path('accounts/logout/', FSLogout.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', FSLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index')
]