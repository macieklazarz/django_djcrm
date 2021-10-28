from django.contrib import admin
from django.urls import path
from .views import AgentListView, AgentCreateView, AgentDetailView

app_name = 'agents'

urlpatterns= [
	path('', AgentListView.as_view(), name='agent-list'),
	path('<int:pk>/',AgentDetailView.as_view(), name='agent-detail'),
	path('create/',AgentCreateView.as_view(), name='agent-create'),
    # path('<int:pk>/update',AgentDetailView.as_view(), name="agent-update"),
    # path('<int:pk>/delete/',AgentDetailView.as_view(), name="agent-delete"),


]