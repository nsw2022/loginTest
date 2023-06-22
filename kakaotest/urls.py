from django.urls import path, include

from kakaotest import views

app_name = 'kakaotest'

urlpatterns = [
    # path('',views.index, name='index'),
    path('',include('poll.urls')),
]