from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request, 'admin_dashboard/index.html')

def view_customer(request):
    return render(request, 'admin_dashboard/view_customer.html')


def view_scheme(request):
    return render(request, 'admin_dashboard/view_scheme.html')

def add_location(request):
    return render(request, 'admin_dashboard/add_location.html')

def view_file(request):
    return render(request, 'admin_dashboard/view_file.html')

def file_transfer(request):
    return render(request, 'admin_dashboard/file_transfer.html')

def file_sale(request):
    return render(request, 'admin_dashboard/file_sale.html')

def view_property(request):
    return render(request, 'admin_dashboard/view_property.html')

def property_type(request):
    return render(request, 'admin_dashboard/property_type.html')

def view_user(request):
    return render(request, 'admin_dashboard/view_user.html')

