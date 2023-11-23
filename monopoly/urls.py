from django.contrib import admin
from django.urls import path

from game.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('rules/', RulesView.as_view(), name='rules'),
    path('topic/<int:topic_id>/', TopicDetailView.as_view(), name='topic_detail'),
    path('random_number/', RandomNumberView.as_view(), name='random_number'),

]
