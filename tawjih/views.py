from django.shortcuts import render

def homepage(request):
	title = "tawjih %s" %(request.user)
	context = {"title":title}
	return render(request, 'base_layout.html', context)