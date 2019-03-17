from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from fossee2.models import Caption,Documents
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import subprocess
import shutil
import ntpath
import os
ntpath.basename("/media/document/")
wdFormatPDF = 17

# Create your views here.

def index(request):
    return render(request,"fossee2/index.html")


@csrf_exempt
def uploadDocument(request):
    
    if request.method=="POST":
        fileUrl = request.FILES.get('Document') 
        
    
        caption = Caption(
        title = request.POST.get('title'),
        description = request.POST.get('description')
        )
        caption.save()
        # conversiontopdf(fileUrl)

        Document = Documents(
            document = request.FILES.get('Document')

        )
        Document.save()
        fileUrl = Document.document.url
        conversiontopdf(fileUrl)
  
    return render(request,"fossee2/uploadDocument.html")

def successfullyUploaded(request):
    return render(request,"fossee2/successfullyUploaded.html")
    return HttpResponseRedirect(reverse("fossee2:viewDocument",) )

def viewDocument(request):
    print("viewDocument")
    caption = Caption.objects.all()[0]
    Document = Documents.objects.all()
    
    #saving pdf path to every object in document to render the pdf's
    for obj in Document:
        head, tail = ntpath.split('./'+str(obj.document) )
        tail = tail.split('.')[0] + '.pdf'
        obj.document = 'document/'+tail
        obj.save()
    return render(request,"fossee2/viewDocuments.html",{"caption":caption,"Document":Document})

def conversiontopdf(fileUrl):
    fileUrl = '.'+fileUrl
    head, tail = ntpath.split(fileUrl)
    tail = tail.split('.')[0] + '.pdf'
    src = tail
    dest = './media/document'
    output = subprocess.check_output(['libreoffice', '--convert-to', 'pdf' ,fileUrl])
    try:
        shutil.move(src,dest)
    except:
        os.remove(src)
    

   
    # ./media/document/hh_jZBuu6t.jpg

