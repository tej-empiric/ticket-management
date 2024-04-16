from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import User1, Ticket, Comment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, View
from .forms import (
    CustomUserCreationForm,
    UserRoleForm,
    AssignPMForm,
    AssignTLForm,
    TicketForm,
)
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


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
                context["form1"] = form
                return render(request, self.template_name, context)

        elif "pm-form" in request.POST:
            form = AssignPMForm(request.POST)
            if form.is_valid():
                user_id = request.POST.get("user_id")
                assigned_pm = form.cleaned_data["pm"]
                user = User1.objects.get(id=user_id)
                user.assigned_PM = assigned_pm
                user.save()
            else:
                context = self.get_context_data()
                context["form2"] = form
                return render(request, self.template_name, context)

        elif "tl-form" in request.POST:
            form = AssignTLForm(request.POST)
            if form.is_valid():
                user_id = request.POST.get("user_id")
                assigned_tl = form.cleaned_data["tl"]
                user = User1.objects.get(id=user_id)
                user.assigned_TL = assigned_tl
                user.save()
            else:
                context = self.get_context_data()
                context["form3"] = form
                return render(request, self.template_name, context)

        return HttpResponseRedirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form1"] = UserRoleForm()
        context["form2"] = AssignPMForm()
        context["form3"] = AssignTLForm()
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


def edit_role(request, id):
    if request.method == "POST":
        try:
            user = User1.objects.get(id=id)
            user.role = None
            user.save()
        except Exception as e:
            print(f"Error editing user role {str(e)}")
    return redirect("/employees")


def edit_pm(request, id):
    if request.method == "POST":
        try:
            user = User1.objects.get(id=id)
            user.assigned_PM = None
            user.save()
        except Exception as e:
            print(f"Error editing user's PM {str(e)}")
    return redirect("/employees")


def edit_tl(request, id):
    if request.method == "POST":
        try:
            user = User1.objects.get(id=id)
            user.assigned_TL = None
            user.save()
        except Exception as e:
            print(f"Error editing user's TL {str(e)} ")
    return redirect("/employees")


def teams(request):
    pms = User1.objects.filter(role="PM")

    ptd_mapping = {}

    for pm in pms:
        tls = User1.objects.filter(
            Q(role="Python-TL") | Q(role="JS-TL"), assigned_PM=pm
        )

        td_mapping = {}

        for tl in tls:
            developers = User1.objects.filter(
                Q(role="Python Developer") | Q(role="JS Developer"), assigned_TL=tl
            )

            td_mapping[tl] = developers

        ptd_mapping[pm] = td_mapping

    context = {"ptd_mapping": ptd_mapping}
    return render(request, "ticket_app/teams.html", context)


def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST, user=request.user)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.created_by = request.user
            ticket.save()
            messages.success(request, "Ticket created successfully")
            return redirect("ticket")
    else:
        form = TicketForm(user=request.user)
    return render(request, "ticket_app/ticket.html", {"form": form})
