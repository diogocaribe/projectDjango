from django.shortcuts import render

def eq_seg_grau(request):

    # if request.method == 'GET':
        
    #     form = Equacao2GrauForm()

    #     context = {
    #         'form': form,
    #     }

    return render(request, 'calculadora/calculadora.html')