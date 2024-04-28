from django.shortcuts import render

def index(request):
    """Main page"""
    return render(request, 'page/index.html')
