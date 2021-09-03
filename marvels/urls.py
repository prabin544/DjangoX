from django.urls import path
from .views import MarvelsListView, MarvelsDetailView, MarvelsCreateView, MarvelsUpdateView, MarvelsDeleteView

urlpatterns = [
    path('', MarvelsListView.as_view(), name='marvels_list'),
    path('<int:pk>/', MarvelsDetailView.as_view(), name='marvels_detail'),
    path('create/', MarvelsCreateView.as_view(), name='marvels_create'),
    path('<int:pk>/update/', MarvelsUpdateView.as_view(), name='marvels_update'),
    path('<int:pk>/delete/', MarvelsDeleteView.as_view(), name='marvels_delete'),
]