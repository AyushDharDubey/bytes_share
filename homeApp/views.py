from django.shortcuts import render
from .models import File
from .forms import UploadForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'files': File.objects.all(),
    }
    return render(request, 'home/index.html', context=context)

# @login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if request.FILES:
            print('ksajh')
        if form.is_valid():
            print('load')
            form.save()
            return HttpResponse("/success/url/")
    else:
        form = UploadForm()
    return render(request, "home/upload.html", {"form": form})