from django.shortcuts import render_to_response, get_list_or_404, get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from gliderlogapp.models import Registration, EntryForm
from django.template import RequestContext
from django import forms
from django.forms.models import modelformset_factory
import datetime
from django.db.models import Sum

def index(request):
    overview = Registration.objects.order_by('-id').filter(start_time__gte=datetime.date.today())
    # Registration.objects.filter(start_time__gte=datetime.date.today()).aggregate(Sum('id'))
    overview.now = datetime.date.today()
    if request.method == 'POST' and "start" in request.POST: # If the form has been submitted...
        formset = EntryForm(request.POST) # A form bound to the POST data
        if formset.is_valid(): # All validation rules pass
			flightnumber = formset.cleaned_data['flightnumber']
			start_method = formset.cleaned_data['start_method']
			glider_registration = formset.cleaned_data['glider_registration']
			captain = formset.cleaned_data['captain']
			passenger = formset.cleaned_data['passenger']
			start_time = datetime.datetime.now()
			remarks = formset.cleaned_data['remarks']
			savetodb = Registration(flightnumber=flightnumber, start_method=start_method, glider_registration=glider_registration,captain=captain, passenger=passenger, start_time=start_time, remarks=remarks)
			savetodb.save()
			return HttpResponseRedirect('/gliderlog/') # Redirect after POST
    elif request.method == 'POST' and "land" in request.POST: 
        landing_time = datetime.datetime.now()
        savelanding = get_object_or_404(Registration, pk=request.POST['land'])
        # make pk variable!!!
        savelanding.landing_time = landing_time
        savelanding.save()
    	return HttpResponseRedirect('/gliderlog/') # Redirect after POST
    else:
        formset = EntryForm() # An unbound form
    return render_to_response('index.html', {
        'overview': overview,
        'formset': formset,
	}, context_instance=RequestContext(request))
	
"""def entry(request):
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
    })"""