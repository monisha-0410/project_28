from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
from app.models import *
def insert_topic(request):
    ENTO=Topicform()
    d={'ENTO':ENTO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['Topic_name']
            TO=Topic.objects.get_or_create(Topic_name=tn)[0]
            TO.save()
        
            return HttpResponse('Entered data successfully')
    return render(request,'insert_topic.html',d)


def insert_webform(request):
    ENWO=WebPageform()
    d={'ENWO':ENWO}
    if request.method=='POST':
        WFDO=WebPageform(request.POST)
        if WFDO.is_valid():
            n=WFDO.cleaned_data['name']
            tn=WFDO.cleaned_data['Topic_name']
            to=Topic.objects.get(Topic_name=tn)
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['Email']
            re=WFDO.cleaned_data['Recreateemail']
            wo=WebPage.objects.get_or_create(name=n,Topic_name=to,url=u,Email=e,Recreateemail=re)[0]
            wo.save()
            return HttpResponse('Entered data successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_webform.html',d)
    