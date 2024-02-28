from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Admission
from .forms import StudentForm, AdmissionForm

def home(request):
    return render(request, 'home.html')

@login_required
def admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admission_success')
    else:
        form = AdmissionForm()
    return render(request, 'admission.html', {'form': form})

@login_required
def admission_success(request):
    return render(request, 'admission_success.html')