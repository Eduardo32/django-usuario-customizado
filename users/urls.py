from django.urls import path

from users.views import SignUpCreateView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpCreateView.as_view(), name='signup'),
]
