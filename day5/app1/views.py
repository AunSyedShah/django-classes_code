from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm


# Create your views here.
def home(request):
    context = {

    }
    if request.method == "GET":
        teachers = Teacher.objects.all()
        context["teachers"] = teachers
        form = TeacherForm()
        context["form"] = form
        return render(request, "home.html", context)
    if request.method == "POST":
        if 'delete-btn' in request.POST:
            teacher_id_form = request.POST.get("teacher_id")
            Teacher.objects.filter(teacher_id=teacher_id_form).delete()
            return redirect(request.path)
        if 'save-btn' in request.POST:
            form = TeacherForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(request.path)
        if 'search-btn' in request.POST:
            teacher_id_form = request.POST.get("teacher_id")
            teachers = Teacher.objects.filter(teacher_id=teacher_id_form)
            context["teachers"] = teachers
            form = TeacherForm()
            context["form"] = form
            return render(request, "home.html", context)
