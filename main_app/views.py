from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Park
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LogForm


#park class

# class Park:
#     def __init__(self, name, state, description, rating):
#         self.name = name
#         self.state = state
#         self.description = description
#         self.rating = rating


# parks = [
#     Park('Glacier National Park', 'Montana', 'Beautiful scenery and plenty of wildlife!', 10),
#     Park('Arches National Park', 'Utah', 'Awesome Geography, but too many lines', 6),
#     Park('Arcadia National Park', 'Maine', 'Great hiking. Beautiful in Fall', 8),
#     Park('Crater Lake National Park', 'Oregon', 'The crater is super cool!', 9),
# ]

#homepage
def home(request):
    return render(request, 'home.html')

#about route
def about(request):
    return render(request, 'about.html')

#parks index
def park_index(request):
    parks = Park.objects.all()
    return render(request, 'parks/index.html', {'parks': parks})

#park details 
def park_detail(request, park_id):
    park = Park.objects.get(id=park_id)
    log_form = LogForm()
    return render(request, 'parks/detail.html', {'park': park, 'log_form' : log_form})

#create cbv

class ParkCreate(CreateView):
    model = Park
    fields = '__all__'

#update
class ParkUpdate(UpdateView):
    model = Park
    fields = ['description', 'rating']


#delete
class ParkDelete(DeleteView):
    model = Park
    success_url = '/parks/'

#add log
def add_log(request, park_id):
    form = LogForm(request.POST)
    if form.is_valid():
        new_log = form.save(commit=False)
        new_log.park_id = park_id
        new_log.save()
    return redirect('park-detail', park_id=park_id)


