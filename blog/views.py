from django.shortcuts import render

# Vistas

def post_list(request):
    return render(request, 'blog/post_list.html', {})
