from typing import Any, Dict
from django.views import View
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,ListView,CreateView,DeleteView,DetailView,UpdateView
)
from client_relationship_manager.forms import CreateClientForm, CustomUserCreationForm, UpdateClientForm

from client_relationship_manager.models import Client, Device

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self) -> str:
        messages.success(self.request,"User Created")
        return reverse_lazy("login")      


# Create your views here.
class HomeView(LoginRequiredMixin,ListView):
    template_name = "index.html"
    context_object_name = "clients"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        user = self.request.user
        queryset = Client.objects.filter(organisation=user.userprofile)
        return queryset

class SearchResultView(LoginRequiredMixin,ListView):
    
    template_name = "search_results.html" 
    context_object_name = "results"

    def get_queryset(self) :
        user=self.request.user

        query = self.request.GET.get("q") or None

        if query:
            results = Client.objects.filter(
                Q(name__icontains=query)
                | Q(pk__icontains=query)
                | Q(phone__icontains=query)
                | Q(address__icontains=query)
                | Q(email__icontains=query),organisation =self.userprofile
            )
        else:
            results = Client.objects.all()

        return results

class CreateClientView(LoginRequiredMixin,CreateView):
    template_name ="create_client.html" 
    form_class = CreateClientForm

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Created")
        return reverse_lazy("crm:index")

class DetailClientView(LoginRequiredMixin,DetailView):
    template_name = "detail_client.html"
    context_object_name = "client"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Client.objects.all()
        return queryset

class UpdateClientView(LoginRequiredMixin,UpdateView):
    template_name = "update_client.html"
    form_class = UpdateClientForm 

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Client.objects.all()
        return queryset

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Updated")
        return reverse_lazy("crm:detail_client")


class DeleteClientView(LoginRequiredMixin,DeleteView):
    template_name = "delete_client.html" 

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Client.objects.all()
        return queryset

    def get_success_url(self) -> str:
        messages.success(self.request,"Client Deleted.")
        return reverse_lazy("crm:index")

class RtnDeviceView(LoginRequiredMixin,ListView):
    template_name="rtnDevice/returned_device.html"
    context_object_name="rtndevices"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        return super().get_context_data(**kwargs)
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset= Device.objects.all()
        return queryset
    
class RtnDeviceDetail(LoginRequiredMixin,DetailView):
    template_name = "rtnDevice/returned_detail_device.html"
    context_object_name = "rtndevices"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Device.objects.all()
        return queryset