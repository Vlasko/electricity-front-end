from django.shortcuts import render
from plotly.offline import plot
import plotly.graph_objs as go

# Create your views here.
def homepage(request):
    return render(request, 'smart_plug/homepage.html')

def display(request):
    template_name='smart_plug/display.html'

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
