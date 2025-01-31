from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login") #solo es accesible para usuarios logueados
def page(request, slug):
    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    })
