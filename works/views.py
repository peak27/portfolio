from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Work

# Create your views here.
def homepage(request):
    works = Work.objects.all()
    return render(request, 'works/Index.html', {'works': works})

def projects(request):
    dss = Work.objects.filter(category = 'EDA')
    ta = Work.objects.filter(category = 'Text Analytics')
    mls = Work.objects.filter(category = 'Machine Learning')
    dls = Work.objects.filter(category = 'Deep Learning')
    devs = Work.objects.filter(category = 'Application Developnment')
    
    allPro = {'dss': dss, 'ta':ta, 'mls': mls, 'dls':dls, 'devs':devs}
    return render(request, 'works/projects.html', allPro)   


def detail(request, work_id):
    work_detail = get_object_or_404(Work, pk=work_id)
    return render(request, 'works/detail.html',{'work':work_detail})

def ds(request):
    #eda = Work.objects.filter(category = "EDA")
    

    #datasc = {'eda':eda, 'ta':ta }
    dss = Work.objects.filter(category = 'EDA')
    ta = Work.objects.filter(category = 'Text Analytics')
    context = {'dss': dss, 'ta':ta}
    return render(request, 'works/ds.html', context)

def ml(request):
    mls = Work.objects.filter(category = 'Machine Learning')
    dls = Work.objects.filter(category = 'Deep Learning')
    cont = {'mls': mls, 'dls':dls}
    return render(request, 'works/ml.html', cont)

def bd(request):
    return render(request, 'works/bd.html')

def dev(request):
    devs = Work.objects.filter(category = 'Application Developnment')
    return render(request, 'works/dev.html', {'devs':devs})
    
def music(request):
    return render(request, 'works/music.html')



