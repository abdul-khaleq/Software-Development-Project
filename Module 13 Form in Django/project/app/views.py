from django.shortcuts import render
from . forms import contactForm, StudentData, passwordValidationProject

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'about.html', {'name': name,'email':email,'select':select})
    else:
        return render(request, 'about.html')

def form(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     return render(request, 'form.html', {'name': name,'email':email})
    # else:
        return render(request, 'form.html')

def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
         file = form.cleaned_data['file']
         with open('./app/upload/' + file.name, 'wb+') as destination:
             for chunk in file.chunks():
                 destination.write(chunk)
        print(form.cleaned_data)
        return render(request, 'django_form.html', {'form':form})
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form':form})

def studentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentData()
    return render(request, './django_form.html', {'form':form})

def passwordValidation(request):
    if request.method == 'POST':
        form = passwordValidationProject(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = passwordValidationProject()
    return render(request, './django_form.html', {'form':form})