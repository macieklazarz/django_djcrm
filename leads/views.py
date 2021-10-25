from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

def lead_list(request):
	lead = Lead.objects.all()
	# return HttpResponse("hello world")
	context = {
		"leads": lead
	}
	return render(request, "leads/lead_list.html", context)

def lead_detail(request, pk):
	print(pk)
	lead = Lead.objects.get(id=pk)
	print(lead)
	return HttpResponse("here is the detail view")
# Create your views here.
