# Create your views here.
from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from gliderlogapp.models import Registration, EntryForm
from django.template import RequestContext
from django import forms
from django.forms.models import modelformset_factory

def index(request):
    overview = Registration.objects.order_by('-flightnumber')
    """overview = get_list_or_404(Registration)"""
    return render_to_response('index.html', {'overview': overview})
	
def entry(request):
    "EntryForm = modelformset_factory(Registration)"
    if request.method == 'POST': # If the form has been submitted...
        formset = EntryForm(request.POST) # A form bound to the POST data
        if formset.is_valid(): # All validation rules pass
			formset.save()
			# Process the data in form.cleaned_data
            # ...
			return HttpResponseRedirect('/gliderlog/') # Redirect after POST
    else:
        formset = EntryForm() # An unbound form

    return render(request, 'entry.html', {
        'formset': formset,
    })