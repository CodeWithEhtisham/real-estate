from django.shortcuts import render

def add_customer(request):
    return render(request, 'admin_dashboard/add_customer.html')

def add_scheme(request):
    return render(request, 'admin_dashboard/add_scheme.html')

def add_file(request):
    return render(request, 'admin_dashboard/add_file.html')

def add_property(request):
    return render(request, 'admin_dashboard/add_property.html')

def add_user(request):
    return render(request, 'admin_dashboard/add_user.html')

# Compare this snippet from apps\admin_dashboard\urls.py:
