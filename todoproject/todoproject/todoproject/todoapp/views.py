from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import Task
from . forms import TodoForm
from django.views.generic import ListView       # Listview
from django.views.generic.detail import DetailView       # detailview
from django.views.generic.edit import UpdateView,DeleteView       # updateview,deleteview

# Listview(class view)
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task1'       #variable_name

# detailview(class view)
class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'       

# updateview(class view)
class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date') 
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwrags={'pk':self.object.id})
    
# deleteview(class view)
class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy ('cbvhome')    


# Create your views here.(function view)
def add(request):
    task1=Task.objects.all()  #details code
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')        #Add date field
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request, "home.html",{'task1':task1})

# def details(request):
#     task=Task.objects.all()
#     return render(request,'detail.html',{'task':task})

def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
    
def update(request,id):
    task=Task.objects.get(id=id)
    f=TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})




