# from django.http import HttpResponse
# from django.shortcuts import render
# from . models import Movie

# # Create your views here.
# def index(request):
#     movie=Movie.objects.all()
#     context={
#         'movie_list':movie
#     }
#     return render(request,'index.html',context)

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Detail View part1

# from django.http import HttpResponse
# from django.shortcuts import render
# from . models import Movie

# # Create your views here.
# def index(request):
#     movie=Movie.objects.all()
#     context={
#         'movie_list':movie
#     }
#     return render(request,'index.html',context)
# def detail(request,movie_id):
#     return HttpResponse("this is movie no %s" % movie_id)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Detail View part3

from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from . forms import MovieForm   #Update Part1#

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    return HttpResponse("this is movie no %s" % movie_id)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})
#add data to DB#
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,"add.html")

#Update Part1#
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')  #home page lott return varan
    return render(request,'edit.html',{'form':form,'movie':movie})

#delete#
def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')





