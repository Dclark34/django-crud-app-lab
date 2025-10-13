from django.shortcuts import render
from django.http import HttpResponse


#park class

class Park:
    def __init__(self, name, state, description, rating):
        self.name = name
        self.state = state
        self.description = description
        self.rating = rating


parks = [
    Park('Glacier National Park', 'Montana', 'Beautiful scenery and plenty of wildlife!', 10),
    Park('Arches National Park', 'Utah', 'Awesome Geography, but too many lines', 6),
    Park('Arcadia National Park', 'Maine', 'Great hiking. Beautiful in Fall', 8),
    Park('Crater Lake National Park', 'Oregon', 'The crater is super cool!', 9),
]

#homepage
def home(request):
    return render(request, 'home.html')

#about route
def about(request):
    return render(request, 'about.html')

#parks index
def park_index(request):
    return render(request, 'parks/index.html', {'parks': parks})
