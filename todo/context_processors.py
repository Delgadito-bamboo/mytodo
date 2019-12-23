from .models import Todo
from .forms import TodoCreateForm
from .views import TodoCreateView
from django.http import HttpResponse

def common(request):
    context = {
        'todo_form': TodoCreateForm()
    }
    return context
