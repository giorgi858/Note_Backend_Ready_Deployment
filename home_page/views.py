from django.shortcuts import render

def home_page_veiw(request):
    return render(request, 'home.html')