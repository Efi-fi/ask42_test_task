from django.shortcuts import render
from .models import Data


def main_page(request):
    return render(request, 'main_page.html')


def input_page(request):
    if request.method == 'POST':
        data = {}
        for key, value in request.POST.items():
            if 'value' in key or 'parameter' in key:
                data[key] = value
        Data(data=data).save()
    return render(request, 'input_page.html')


def output_page(request):
    full_data = list(Data.objects.all())
    return render(request, 'output_page.html', {'full_data': full_data})
