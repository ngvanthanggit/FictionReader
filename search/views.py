from django.shortcuts import render
from .forms import SearchForm
from fiction.models import Fiction

def search_view(request):
    form = SearchForm()
    results = []
    query = ""
    searched = False
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Fiction.objects.filter(title__icontains=query)
            searched = True
    
    context = {'form': form, 'results': results, 'query': query, 'searched': searched}
    return render(request, 'search/search_results.html', context)
