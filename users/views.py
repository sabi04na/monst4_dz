from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from .forms import ResumeForm

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'users/resume_list.html', {'resumes': resumes})

def resume_create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'users/resume_form.html', {'form': form})

def resume_update(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            form.save()
            return redirect('resume_list')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'users/resume_form.html', {'form': form})

def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    return render(request, 'users/resume_delete.html', {'resume': resume})
