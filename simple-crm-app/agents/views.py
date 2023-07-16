from typing import Any, Dict
import random
from django.core.mail import send_mail
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import OrganisorAndLoginRequiredMixin
from agents.forms import AgentModelForm
from client_relationship_manager.models import Agent


# Create your views here.
class AgentListView(OrganisorAndLoginRequiredMixin,generic.ListView):
    template_name = "agent_list.html"
    context_object_name = "agents"
    
    #for adding context to the view
    
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     return super().get_context_data(**kwargs)
    
    def get_queryset(self):
        #get the logged in user
        user = self.request.user
        #get data based on agents organisation, which is logged in
        #users userprofile
        queryset = Agent.objects.filter(organisation=user.userprofile)
        return queryset
    
    
class AgentCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    template_name = "agent_create.html"
    form_class = AgentModelForm
    
    #we implement form valid to set user as an agent and not organisor then
    #we create the the agent programatically
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # first we create a user agent then we create the actual agent 
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f'{random.randint(100,2000000)}')
        user.save()
        # create actual agent 
        agent = Agent.objects.create(
            user = user,
            organisation = self.request.user.userprofile #get logged on user userprofile
        )
        # send an email to the new agent 
        send_mail(
            subject = "You are invited to be an Agent",
            message = "You were added to be an agent in Simple CRM. Please visit <a href='https://www.carlhub.com'>www.carlhub.com</a> to start working.",
            from_email = "info@carlhub.com",
            recipient_list= [user.email]
            
        )
        return super(AgentCreateView,self).form_valid(form)
    
    def get_success_url(self) -> str:
        messages.success(self.request,"Agent Created")
        return reverse_lazy('agents:agent')
    
class AgentDetailView(OrganisorAndLoginRequiredMixin,generic.DetailView):
    template_name ="agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self) -> QuerySet[Any]:
       user = self.request.user
       queryset = Agent.objects.filter(organisation=user.userprofile)
       return queryset
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "agent_update.html"
    form_class = AgentModelForm  
    # context_object_name = "agent"

    
    def get_queryset(self) -> QuerySet[Any]:
       user = self.request.user
       queryset = Agent.objects.filter(organisation=user.userprofile)
       return queryset
    
    def get_success_url(self) -> str:
        messages.success(self.request,"Agent Updated")
        return reverse_lazy('agents:agent')
    
class AgentDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name ="agent_delete.html"
    context_object_name = "agent"
    
    def get_queryset(self) -> QuerySet[Any]:
       user = self.request.user
       queryset = Agent.objects.filter(organisation=user.userprofile)
       return queryset
        
    def get_success_url(self) -> str:
        messages.success(self.request,"Agent Deleted")
        return reverse_lazy('agents:agent')
    