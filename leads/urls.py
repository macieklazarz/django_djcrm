from django.contrib import admin
from django.urls import path
# from leads.views import lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView
from leads.views import LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView, AssignAgentView, CategoryListView, CategoryDetailView, LeadCategoryUpdateView

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('<int:pk>/',LeadDetailView.as_view(), name="lead-detail"),
    path('<int:pk>/update',LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(), name="lead-delete"),
    path('create/',LeadCreateView.as_view(), name="lead-create"),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name="assign-agent"),
    path('<int:pk>/category/', LeadCategoryUpdateView.as_view(), name="lead-category-update"),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>', CategoryDetailView.as_view(), name='category-detail')


]