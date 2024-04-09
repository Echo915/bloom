from django.shortcuts import render

# Create your views here.
# Dashboard Page
def dashboard(request):
    return render(request, "home.html", {
        "first_name": "Fortune",
        "last_name": "Klabi",
        "nickname": "Echo",
    })