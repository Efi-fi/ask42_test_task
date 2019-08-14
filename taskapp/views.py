from django.shortcuts import render
from .models import Data


def main_page(request):
    return render(request, 'main_page.html')


def input_page(request):
    if request.method == 'POST':
        parameters = {key: value for key, value in request.POST.items() if 'parameter' in key}
        values = {key: value for key, value in request.POST.items() if 'value' in key}
        data = {}
        for parameter_num, par_str in parameters.items():
            par_num = parameter_num.split('_')[1]
            for value_num, val_str in values.items():
                if value_num.split('_')[1] == par_num:
                    data[par_str] = val_str
        Data(data=data).save()
    return render(request, 'input_page.html')


def output_page(request):
    if request.method == 'POST':
        Data.objects.all().delete()
    full_data = list(Data.objects.all())
    return render(request, 'output_page.html', {'full_data': full_data})
