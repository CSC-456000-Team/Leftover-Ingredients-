from django.shortcuts import render
from .models import Post
# Create your views here.

# dummy data which wiil replace by database
posts = [
    {
        'author' : 'David',
        'title' : ' Avocado Toast',
        'content': 'First recipe content',
        'date_posted': 'October 31, 2021'    
    },
    {
        'author' : 'Jinho',
        'title' : 'Pumpkin Pie',
        'content': 'Second recipe content',
        'date_posted': 'November 1, 2021'    
    },
]

def recipe(request):
    context = {
        'posts': posts
        # Post.objects.all()
    }
    return render(request, 'main/recipe.html', context)

# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})
