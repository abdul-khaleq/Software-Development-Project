from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    data = {'author': 'Abdul Khaleq', 'age': 9, 'list':['Python', 'is', 'best'], 'birthday': datetime.datetime.now(), 'date': ' ', 'num': 10, 'val': 'Hello world!', 'courses':[
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000,
        },
        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 6000,
        },
        {
            'id' : 3,
            'name' : 'HTML',
            'fee' : 7000,
        },
        {
            'id' : 4,
            'name' : 'CSS',
            'fee' : 8000,
        },
    ]}
    # return render(request, 'home.html', context=data)
    return render(request, 'home.html', data)