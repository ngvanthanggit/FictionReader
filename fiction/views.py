from django.shortcuts import render

from .models import Fiction

# Create your views here.

def fiction_page(request, fiction_id):
    this_fiction = Fiction.objects.get(id=fiction_id)
    chapters_list = this_fiction.chapters.all()
    context={'this_fiction': this_fiction, 'chapters_list': chapters_list}
    return render(request, 'fiction/fiction_page.html', context)

def chapter_page(request, fiction_id, chapter_id):
    this_fiction = Fiction.objects.get(id=fiction_id)
    this_chapter = this_fiction.chapters.get(chapter_number=chapter_id)
    context = {'this_chapter': this_chapter}
    return render(request, 'fiction/chapter_page.html', context)