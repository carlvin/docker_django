from django.urls import path
from .views import AgentListView,AgentCreateView,AgentDetailView,AgentUpdateView,AgentDeleteView

app_name = 'agents'

urlpatterns = [
    path('',AgentListView.as_view(),name='agent'),
    path('create_agent/',AgentCreateView.as_view(),name='create-agent'),
    path('<int:pk>/detail/',AgentDetailView.as_view(),name='detail-agent'),
    path('<int:pk>/update/',AgentUpdateView.as_view(),name='update-agent'),
    path('<int:pk>/delete/',AgentDeleteView.as_view(),name='delete-agent'),
    
]