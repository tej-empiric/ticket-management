from django.urls import path
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="ticket_app/home.html"), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("employees/", views.EmployeeView.as_view(), name="employees"),
    path("teams/", views.teams, name="teams"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit_role/<int:id>/", views.edit_role, name="edit_role"),
    path("edit_pm/<int:id>/", views.edit_pm, name="edit_pm"),
    path("edit_tl/<int:id>/", views.edit_tl, name="edit_tl"),
    path("ticket/", views.ticket, name="ticket"),
]
