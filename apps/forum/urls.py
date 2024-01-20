from django.urls import path
from apps.forum.views import (
    ForumCreateView,
    ForumUpdateView,
    ForumDeleteView,
    ForumDetailView,
    ForumListView,
)

app_name = "forum"

urlpatterns = [
    path("", ForumListView.as_view(), name="forum_list"),
    path("create/", ForumCreateView.as_view(), name="forum_create"),
    path("<int:pk>/", ForumDetailView.as_view(), name="forum_detail"),
    path("<int:pk>/update/", ForumUpdateView.as_view(), name="forum_update"),
    path("<int:pk>/delete/", ForumDeleteView.as_view(), name="forum_delete"),
]
