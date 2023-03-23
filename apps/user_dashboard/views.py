from django.shortcuts import render

# Create your views here.
def user_dashboard(request):
    return render(request, 'user_dashboard/index.html')

def gallery(request):
    return render(request, 'user_dashboard/gallery.html')

def contact(request):
    return render(request, 'user_dashboard/contact.html')

def properties_details(request):
    return render(request, 'user_dashboard/properties-detail.html')

def properties(request):
    return render(request, 'user_dashboard/properties.html')

def blog_archive(request):
    return render(request, 'user_dashboard/blog-archive.html')

def blog_single(request):
    return render(request, 'user_dashboard/blog-single.html')