from django.shortcuts import render, get_object_or_404
from .models import Todo, TodoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


# Create your views here.

class IndexView(ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.order_by('-todo_date')[:5]


class DetailView(DetailView):
    model = Todo
    template_name = 'todos/detail.html'


class AddView(CreateView):
    model = Todo
    template_name = 'todos/add.html'
    form_class = TodoForm
    success_url = reverse_lazy('todos:index')


class RemoveView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todos:index')
    template_name = 'todos/remove.html'


class UpdateView(UpdateView):
    model = Todo
    template_name = 'todos/update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todos:index')

#
# # 일정목록보기
# def index(request):
#     todo_list = Todo.objects.all().order_by('-todo_date')
#     context = {'todo_list': todo_list}
#     return render(request, 'todos/index.html', context)
#
#
# # 일정 등록
# def add(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.todo_date = timezone.now()
#             post.save()
#             return HttpResponseRedirect(reverse('todos:index'))
#     else:
#         form = TodoForm()
#         return render(request, 'todos/add.html', {'form': form})
#
#
# # 일정 상세보기
# def detail(request, todo_id):
#     todo = get_object_or_404(Todo, pk=todo_id)
#     context = {'todo': todo}
#     return render(request, 'todos/detail.html', context)
#
#
# # 일정 삭제
# def delete(request, todo_id):
#     todo = Todo.objects.get(pk=todo_id)
#     if request.method == 'POST':
#         todo.delete()
#         return HttpResponseRedirect(reverse('todos:index'))
#     return render(request, 'todos/remove.html', {'todo': todo})
#
#
# # 일정 수정
# def update(request, todo_id):
#     todo = get_object_or_404(Todo, id=todo_id)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance= todo)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.todo_date = timezone.now()
#             post.save()
#             return HttpResponseRedirect(reverse('todos:index'))
#     else:
#         form = TodoForm(instance= todo)
#         return render(request, 'todos/update.html', {'form': form})
