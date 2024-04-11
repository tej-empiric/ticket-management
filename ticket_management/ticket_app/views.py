from django.shortcuts import render, HttpResponse, redirect
from .models import User1, Ticket, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EmployeeView(ListView):
    model = User1
    template_name = "ticket_app/employees.html"

    def post(self, request, *args, **kwargs):
        user_id = request.POST.get("user_id")
        selected_users = request.POST.get("selected_users")

        if selected_users:
            User1.objects.filter(id__in=selected_users).update(is_active=True)
        else:
            User1.objects.filter(id=user_id).update(is_active=False)

        return redirect("employees")
