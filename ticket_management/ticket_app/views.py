from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import User1, Ticket, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from .forms import CustomUserCreationForm, UserRoleForm
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class EmployeeView(ListView):
    model = User1
    template_name = "ticket_app/employees.html"

    def post(self, request, *args, **kwargs):
        if "active-form" in request.POST:
            user_id = request.POST.get("user_id")
            selected_users = request.POST.get("selected_users")

            if selected_users:
                User1.objects.filter(id__in=selected_users).update(is_active=True)
            else:
                User1.objects.filter(id=user_id).update(is_active=False)

        elif "role-form" in request.POST:
            form = UserRoleForm(request.POST)
            if form.is_valid():
                user_id = request.POST.get("user_id")
                user_role = form.cleaned_data["user_role"]
                user = User1.objects.get(id=user_id)
                user.role = user_role
                user.save()
                return redirect("employees")
            else:
                context = self.get_context_data()
                context["form"] = form
                return render(request, self.template_name, context)

        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = UserRoleForm()
        return context

    def get_queryset(self):
        return User1.objects.all()


def delete(request, id):
    try:
        user = User1.objects.get(pk=id)
        user.delete()
    except Exception as e:
        print(f"Error deleting blog {str(e)}")

    return redirect("/employees")


def edit(request, id):
    if request.method == "POST":
        try:
            user = User1.objects.get(id=id)
            user.role = None
            user.save()
        except Exception as e:
            print(f"Error editing user role {str(e)}")
    return redirect("/employees")


class TeamView(View):
    pass
