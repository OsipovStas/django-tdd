from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['movie_name'])
		return redirect('/')

	movies = Item.objects.all()
	return render(request, 'home.html', {'movies': movies})
