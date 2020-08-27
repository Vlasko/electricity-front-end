from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go
from smart_plug.models import Instance

# Create your views here.
def homepage(request):
    return render(request, 'smart_plug/homepage.html')

def display(request):
    #Try to get data from db.dqlite3 in the graph below
    x_values_list=[1,2,3,4]
    y_values_list=[1,4,9,16]

    fig = go.Figure()
    scatter=go.Scatter(x=x_values_list,
                        y=y_values_list,
                        marker={'color':'red'},
                        hovertext=y_values_list)
    fig.add_trace(scatter)
    div = plot(fig, output_type='div')

    graph_dict = {'graph':div}

    return render(request, 'smart_plug/display.html', context=graph_dict)

def detail(request):
    inst = Instance.objects.all()
    inst_dict = {'instances':inst}
    return render(request, 'smart_plug/detail.html', context=inst_dict)
