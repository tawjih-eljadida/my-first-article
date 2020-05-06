from django.shortcuts import render

# Create views here.
def homepage(request):
		return render(request, 'articles/page_articles.html', )
