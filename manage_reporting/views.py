from django.shortcuts import render

# Create your views here.

def ReportingView(request):
    return render(request,"manage_reporting/ReportingView.html",locals())