from django.shortcuts import render
from .forms import Equacao2GrauForm

def eq_seg_grau(request):

    # if request.method == 'GET':
        
    #     form = Equacao2GrauForm()

    #     context = {
    #         'form': form,
    #     }

    return render(request, 'calculadora/calculadora.html')