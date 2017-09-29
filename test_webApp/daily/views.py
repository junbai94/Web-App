# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
import sqlite3
import pandas as pd
from .forms import NameForm, SpotForm, FutForm, UploadForm

def index(request):
    return render(request, 'daily/index.html', {})

def spot_price(request):
    valid = False
    if request.method == 'POST':
        form = SpotForm(request.POST)
        if form.is_valid():
            valid = True
            conn = sqlite3.connect('C:/Users/j291414/Desktop/market_data.db')
            spotID = form.cleaned_data['spotID']
            date = form.cleaned_data['date']
            sql = "SELECT * FROM spot_daily WHERE spotID = '{}' and date like '{}%'".format(spotID, date)
            data = pd.read_sql_query(sql, conn)
        
        
            conn.close()
            
            return render(request, 'daily/spot_price.html',{'data':data,
                                                            'form':form,
                                                            'valid':valid,
                                                            })
#            return HttpResponse(date)
    else:
        form = SpotForm()
        return render(request, 'daily/spot_price.html', {'form':form,
                                                         'valid':valid,
                                                         })
    
def fut_curve(request):
    valid = False
    if request.method == 'POST':
        form = FutForm(request.POST)
        if form.is_valid():
            valid = True
            conn = sqlite3.connect('C:/Users/j291414/Desktop/market_data.db')
            instID = form.cleaned_data['instID']
            date = form.cleaned_data['date']
            sql = "SELECT instID, exch, date, close FROM fut_daily WHERE instID like '{}____' and date like '{}%'".format(instID, date)
            data = pd.read_sql_query(sql, conn)
            conn.close()
            return render(request, 'daily/fut_curve.html',{'data':data,
                                                            'form':form,
                                                            'valid':valid,
                                                            })
    else:
        form = FutForm()
        return render(request, 'daily/fut_curve.html', {'form':form,
                                                         'valid':valid,
                                                         })
    





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#                           Test Functions
##++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def test_upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            ID = form.cleaned_data['ID']
            misc = form.cleaned_data['misc']
            conn = sqlite3.connect('P:/test_webApp/db.sqlite3')
            c = conn.cursor()
            c.execute("INSERT INTO test_table VALUES (?, ?)", (ID, misc))
            conn.commit()
            conn.close()
            form2 = UploadForm()
            return render(request, 'daily/test_upload.html', {'form':form2})
    else:
        form = UploadForm()
    
        return render(request, 'daily/test_upload.html', {'form':form})






def df_to_dict(df):
    out = {}
    out['fields'] = list(df.columns)
    for field in df:
        out[field] = list(df[field])
    return out

# file charts.py
def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

# form to get names
def get_name(request):
#    valid = False
#    if request.method == 'POST':
#        form = NameForm(request.POST)
#        if form.is_valid():
#            valid = True
#            return render(request, 'daily/get_name.html', {'form':form, 'valid':valid})
#        else:
#            return HttpResponse('Your input is not valid')
#    else:
#        form = NameForm()
#    return render(request, 'daily/get_name.html', {'form':form, 'valid':valid})
    name = None
    date = None
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
    else:
        pass
    return render(request, 'daily/get_name.html', {'name':name,
                                                   'date':date})     