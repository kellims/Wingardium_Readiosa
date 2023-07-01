from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from .models import Author, Book

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    # def get(self, request):
    #     return HttpResponse("Welcome to Wingardium Readiosa 🧹🪄 📖 ")
    

class About(TemplateView):
     template_name = "about.html"

    # def get(self, request):
    #     return HttpResponse("About Wingardium Readiosa")    


# class Authors:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio



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
    # success_url = "/authors/"

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})

class AuthorDetail(DetailView):
    model = Author
    template_name = "author_detail.html"

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name', 'image', 'bio']
    template_name = "author_update.html"
    success_url = "/authors/"  

    def get_success_url(self):
        return reverse('author_detail', kwargs={'pk': self.object.pk})  
    
class AuthorDelete(DeleteView):
    model = Author
    template_name = "author_delete_confirmation.html"
    success_url = "/authors/"    


class BookCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.POST.get("image")
        author = Author.objects.get(pk=pk)
        Book.objects.create(title=title, description=description, image=image, author=author)
        return redirect('author_detail', pk=pk)
    
class BookList(TemplateView):
    template_name = "book_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Book.objects.all()
        return context


class BookDetail(DetailView):
    model = Book
    template_name = "book_detail.html" 


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'image', 'description', 'author']
    template_name = "book_update.html"
    success_url = "/books/"  

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.pk})      