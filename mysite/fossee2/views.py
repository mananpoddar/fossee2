from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee2.models import Caption,Documents
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

ini =0

# Create your views here.

def index(request):
    return render(request,"fossee2/index.html")


@csrf_exempt
def uploadDocument(request):
    if request.method=="POST":
        ini =0
        if ini == 0:
                caption = Caption(
                title = request.POST.get('title'),
                description = request.POST.get('description')
                )
                caption.save()
                ini =1
        Document = Documents(
            document = request.FILES.get('Document')

        )
        Document.save()
        
    return render(request,"fossee2/uploadDocument.html")

def viewDocument(request):
    print("viewDocument")
    caption = Caption.objects.all()[0]
    Document = Documents.objects.all()
    return render(request,"fossee2/viewDocuments.html",{"caption":caption,"Document":Document})