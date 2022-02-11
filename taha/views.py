from django.shortcuts import render

def home(request):
	from taha.name import name
	return render(request, 'home.html', {"name" : name})
def about(request):
	first_n = "Taha"
	last_n = "Babazadeh"
	return render(request, 'about.html', {"first":first_n , "last":last_n})
