from django.shortcuts import render
from .forms import BulkSmsForm
# Create your views here.
def index(request):
    return render(request, 'index.html')

def bulker(request):
    if request.method == 'POST':
        form = BulkSmsForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BulkSmsForm()
    return render(request, 'forms.html' {'form':form})