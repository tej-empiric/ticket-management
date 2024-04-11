from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="ticket_app/home.html"), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("employees/", views.EmployeeView.as_view(), name="employees"),
    path("teams/", views.TeamView.as_view(), name="teams"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit"),
]
