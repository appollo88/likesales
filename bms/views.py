from django.shortcuts import render

# Create your views here.

def main(request):
<<<<<<< HEAD
	context = "you are looking at main page."
=======
	context = "this is main page"
>>>>>>> d6dbea47faa10f70e2030fb8f64b4d3241f4c055
	return render(request, 'bms/main.html', {'context': context})