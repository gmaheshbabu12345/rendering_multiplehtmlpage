from django.shortcuts import render

# Create your views here.
def dasara(request):
    return render(request,'dasara.html')

def diwali(request):
    return render(request,'diwali.html')
def sankranthi(request):
    return render(request,'sankranthi.html')
def xmas(request):
    return render(request,'xmas.html')
