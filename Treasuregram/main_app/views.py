from django.shortcuts import render
# from django.http import HttpResponse # No longer used
from .models import Treasure

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})

#  class Treasure:
#  def __init__(self, name, value, material, location, img_url):
#        self.name = name
#        self.value = value
#        self.material = material
#        self.location = location
#        self.img_url = img_url
#
# treasures = [
#    Treasure('Gold Nugget', 500.00, 'gold', 'Cholera Creek, NM', '/Treasuregram/main_app/static/images/treasure-image.png'),
#    Treasure("Fool's Gold", 0.00, 'pyrite', "Dumbass's Holler, AZ", '/Treasuregram/main_app/static/images/treasure-image.png'),
#    Treasure('Used Johnny Pot', 20.00, 'porcelain', "Whore Town, MT", '/Treasuregram/main_app/static/images/treasure-image.png')
#]