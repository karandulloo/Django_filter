from django.shortcuts import render
from django.db import connection
from embl.filter import EmblFilter
from embl.models import Embl
import psycopg2

def MultipleSearch(request):

    completedata = Embl.objects.all()
    myFilter = EmblFilter(request.GET, queryset=completedata)
    completedata = myFilter.qs
    context = {'myFilter':myFilter, "Embl": completedata}

    # return render(request, 'Index.html', context)
    return render(request, 'Index.html', context)