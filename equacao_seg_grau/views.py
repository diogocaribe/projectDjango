from django.http import HttpResponse
from django.shortcuts import render


def eq_seg_grau(request):
    return render(request, 'index.html',)