from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag
from .models import BLOGS
from .forms import BLOGForm

def show_blog(request):

    if request.method == "POST":
        form = BLOGForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.owner = request.user
            blog.save()
            form.save_m2m()

    elif request.method == "GET":
        form = BLOGForm()

    return render(request, "my_blogs.html", {"BLOGS": BLOGS.objects.filter(owner=request.user.id),
                                             "tags": Tag.objects.all(),
                                             "form": form})

def get_blog(request, todo_id):
    try:
        todo = BLOGS.objects.get(id=todo_id)
        if request.user.id != todo.owner.id:
            raise PermissionDenied
        return render(request, "detailed_blog.html", {"Blogs": todo})
    except BLOGS.DoesNotExist:
        raise Http404("We don't have any.")

@permission_required('is_superuser')
def show_all_blog(request):
    return render(request, "my_blogs.html", {"BLOGS": BLOGS.objects.all()})

@permission_required('is_superuser')
def show_all_blog_from_user(request, userId):
    return render(request, "my_blogs.html", {"BLOGS": BLOGS.objects.filter(owner=userId)})
