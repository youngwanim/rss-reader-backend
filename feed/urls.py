from django.urls import path

from . import views

urlpatterns = [
    path('<feed_id>/', views.read_feed_detail, name='detail'),
    path('', views.FeedListView.as_view(), name='index'),
]

