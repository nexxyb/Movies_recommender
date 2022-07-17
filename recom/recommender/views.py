from django.shortcuts import render
from .models import *
from django.views import generic
#from django.contrib.auth.mixins import LoginRequiredMixin
from recommender.mmr3 import get_movie
from recommender.forms import SearchForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    """View function for home page of site.""" 
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form =  SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data                                                                                = form.cleaned_data['movie']
            result= get_movie([data])
            # redirect to a new URL:
            #return HttpResponseRedirect(request.path.info)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        result= get_movie(form.data)
    
    context = {
        'result': result,
        'form':form
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'recommender/index.html', context=context)
class AboutView(generic.TemplateView):
    template_name= 'recommender/about.html'
    
class ContactView(generic.FormView):
    template_name= 'recommender/contact.html'
    #form_class= 