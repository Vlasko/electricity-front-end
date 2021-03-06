from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter, Layout
from plotly.subplots import make_subplots
from smart_plug.models import Instance

# Create your views here.
def homepage(request):
    return render(request, 'smart_plug/homepage.html')

def display(request):
    #Try to get data from db.dqlite3 in the graph below
    data = Instance.objects.values_list('timestamp',
                                        'demand',
                                        'price',
                                        'unit_price')
    index_values_list = []
    demand_values_list = []
    unit_price_values_list = []
    for values in data:
        index_values_list.append(values[0])
        demand_values_list.append(values[1])
        unit_price_values_list.append(values[3]) #check why this is 2 not 3

    layout = Layout(paper_bgcolor='rgba(0,0,0,0)',
                   plot_bgcolor='rgba(0,0,0,0)')

    fig = make_subplots(specs=[[{"secondary_y": True}]],
                        subplot_titles=['Demand and Price Data'])
    # add demand data to plot
    fig.add_trace(Scatter(x=index_values_list,
                              y=demand_values_list,
                              name='Demand (W)',
                              marker={'color':'red'},
                              hovertext=demand_values_list),
                              secondary_y=False)
    # add price data to plot
    fig.add_trace(Scatter(x=index_values_list,
                              y=unit_price_values_list,
                              name='Price (p/kWh)',
                              marker={'color':'blue'},
                              hovertext=unit_price_values_list),
                              secondary_y=True)
    # add axis titles & labels
    fig.update_layout(layout)
    fig.update_xaxes(title_text="Datetime")
    fig.update_yaxes(title_text="<b>Demand (W)</b>",
                     secondary_y=False)
    fig.update_yaxes(title_text="<b>Price (p/kWh)</b>",
                     secondary_y=True)
    fig['layout']['yaxis2']['showgrid']=False
    div = plot(fig, output_type='div')
    graph_dict = {'graph':div}
    return render(request, 'smart_plug/display.html', context=graph_dict)

def detail(request):
    inst = Instance.objects.all()
    inst_dict = {'instances':inst}
    return render(request, 'smart_plug/detail.html', context=inst_dict)

def about(request):
    return render(request, 'smart_plug/about.html')
