from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    mydict = {'key1': 'value1'}
    mylist = {1,2,3,4}
    list_of_dictionaries = [{'user' : '832'}, {'user' : '3238'},{'user' : '30293'}]
    mybool = True
    context = {'name' : 'Jeng', 'mydict' : mydict, 'mylist' : mylist, 'mybool' : mybool, 'list_of_dictionaries' : list_of_dictionaries}
    return render(request, 'examples/index.html' , context)

def profile(request):
    return render(request, 'examples/profile.html')


    
