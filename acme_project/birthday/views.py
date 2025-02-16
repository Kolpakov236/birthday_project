from .forms import BirthdayForms, CongratulationForm
from .models import Birthday
from .utils import calculate_birthday
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied

@login_required
def add_comment(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    form = CongratulationForm(request.POST or None)
    if form.is_valid():
        congratulation = form.save(commit=False)
        congratulation.author = request.user
        congratulation.birthday = birthday
        congratulation.save()
    return redirect('birthday:detail', pk=pk)

@login_required
def simple_view(request):
    return HttpResponse("Страница для залогиненных пользователей")

@login_required
def birthday(request):
    form = BirthdayForms(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('birthday:list')
    context = {'form': form}
    return render(request, 'birthday/birthday_form.html', context)  # Укажите правильный шаблон

class BirthdayListView(ListView):
    model = Birthday
    queryset = Birthday.objects.prefetch_related(
        'tags'
    ).select_related('author')
    ordering = 'id'
    paginate_by = 5

class BirthdayMixin:
    model = Birthday
    success_url = reverse_lazy('birthday:list')

class BirthdayCreateView(CreateView, LoginRequiredMixin):
    model = Birthday
    form_class = BirthdayForms

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BirthdayUpdateView(BirthdayMixin, UpdateView, LoginRequiredMixin):
    form_class = BirthdayForms

    def dispatch(self, request, *args, **kwargs):
        instance = get_object_or_404(Birthday, pk=kwargs['pk'])
        if instance.author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class BirthdayDeleteView(BirthdayMixin, DeleteView, LoginRequiredMixin):
    form_class = BirthdayForms

class BirthdayDetailView(DetailView, LoginRequiredMixin):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday(self.object.birthday)
        context['form'] = CongratulationForm()
        context['congratulations'] = self.object.congratulations.select_related('author')
        return context
