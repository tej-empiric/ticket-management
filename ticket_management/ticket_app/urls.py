from django.urls import path
from . import views


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("employees/", views.EmployeeView.as_view(), name="employees"),
    path("teams/", views.teams, name="teams"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit_role/<int:id>/", views.edit_role, name="edit_role"),
    path("edit_pm/<int:id>/", views.edit_pm, name="edit_pm"),
    path("edit_tl/<int:id>/", views.edit_tl, name="edit_tl"),
    path("edit_assignee/<int:id>/", views.edit_assignee, name="edit_assignee"),
    path("edit_status/<int:id>/", views.edit_status, name="edit_status"),
    path("create_ticket/", views.create_ticket, name="create-ticket"),
    path("ticket/<int:id>/", views.ticket, name="ticket"),
    path("edit_ticket/<int:id>/", views.edit_ticket, name="edit_ticket"),
    path("delete_ticket/<int:id>/", views.delete_ticket, name="delete_ticket"),
]
