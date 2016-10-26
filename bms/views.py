from django.shortcuts import render

# Create your views here.

def main(request):
	context = "this is main page"
	return render(request, 'bms/main.html', {'context': context})