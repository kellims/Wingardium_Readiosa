from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView

from .models import Author

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    # def get(self, request):
    #     return HttpResponse("Welcome to Wingardium Readiosa 🧹🪄 📖 ")
    

class About(TemplateView):
     template_name = "about.html"

    # def get(self, request):
    #     return HttpResponse("About Wingardium Readiosa")    


class Authors:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio



class AuthorList(TemplateView):
    template_name = "author_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["authors"] = Author.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:     
            context["authors"] = Author.objects.all()
            # context["header"] = "Authors"
        return context
    
class AuthorCreate(CreateView):
    model = Author
    fields = ['name', 'image', 'bio']
    template_name = "author_create.html"
    success_url = "/authors/"

class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'image', 'bio']
    template_name = "author_update.html"
    success_url = "/authors/"    