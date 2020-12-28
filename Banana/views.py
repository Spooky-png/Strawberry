from django.shortcuts import render, HttpResponse
from Banana.models import Contact

def home(request):
    context = {'name': 'Mike', 'course': 'Django'}
    return render(request,'home.html', context)
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')
def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("the data has been saved")
    return render(request, 'contact.html')
def leaguespy(request):
    return render(request, 'leagueSpy.html')
def championlookup(request):
    return render(request, 'championLookup.html')
def W3(request):
    return render(request, 'W3.html')
