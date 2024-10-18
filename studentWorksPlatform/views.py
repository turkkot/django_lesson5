from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Work, User
from django.urls import reverse_lazy
from django_filters.views import FilterView
from studentWorksPlatform import filters



# Create your views here.
class WorkListView(FilterView):
    model = Work
    template_name = 'studentWorksPlatform/work_list.html'
    context_object_name = 'works'
    ordering = ['-created_at']
    filterset_class = filters.Work


class WorkDetailView(DetailView):
    model = Work
    template_name = 'studentWorksPlatform/work_detail.html'
    context_object_name = 'work'


class WorkCreateView(CreateView):
    model = Work
    template_name = 'studentWorksPlatform/work_form.html'
    fields = ['title', 'description', 'subject', 'file', 'image', 'price', 'author', 'university', 'professor', 'is_unique']
    success_url = reverse_lazy('work_list')

class WorkUpdateView(UpdateView):
    model = Work
    template_name = 'studentWorksPlatform/work_edit.html'
    fields = ['title', 'description', 'subject', 'file', 'image', 'price', 'university', 'professor', 'is_unique']
    success_url = reverse_lazy('work_list')

class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'studentWorksPlatform/work_confirm_delete.html'
    success_url = reverse_lazy('work_list')

class UserListView(FilterView):
    model = User
    template_name = 'studentWorksPlatform/user_list.html'
    context_object_name = 'users'
    ordering = ['-created_at']
    filterset_class = filters.UserFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список пользователей'
        return context
