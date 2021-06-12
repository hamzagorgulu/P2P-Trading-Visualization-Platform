import dash  # version 1.13.1       # stacked bar çizdiriyor. Axis isimleri eklenecek.
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
from dash.dependencies import Input, Output, State, MATCH
from plotly.graph_objects import Bar, Figure
import plotly.graph_objects

# workbook1 = load_workbook(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Yusuf1.xlsx")    #Yusuf 1
# sheet1 = workbook1.active
# sheet1 = workbook1["güç dengesi"]
#
# #***************************************************************Yusuf1-1. ev******************
# list_home1=[]
# columns=["Time","Pbuy_t","P_ev_used","P_pv_used","P_bat_used","P_ev_ch","P_bat_ch","P_load_t"]
# for value in sheet1.iter_rows(min_row=87,
#    max_row=96,
#    min_col=2,
#    max_col=97,
#    values_only=True):
#    list_home1.append(value)
#
# from pandas import DataFrame
# df_home1 = DataFrame(list_home1)
#
# df_home1=df_home1.T
#
# df_home1.drop([6,1],axis=1,inplace=True)
#
# df_home1.columns=columns

df=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Toplu Excel\toplu.xlsx",index_col="Time")
df=df.fillna(0)
df1=df.iloc[:, [0,1,2,3,4,5,6]]
df2=df.iloc[:, [7,8,9,10,11,12,13]]
df3=df.iloc[:, [14,15,16,17,18,19,20]]
df4=df.iloc[:, [21,22,23,24,25,26,27]]
df5=df.iloc[:, [28,29,30,31,32,33,34]]
df6=df.iloc[:, [35,36,37,38,39,40,41]]
df7=df.iloc[:, [42,43,44,45,46,47,48]]

df8=df.iloc[:, [49,50,51,52,53,54,55]]
df9=df.iloc[:, [56,57,58,59,60,61,62]]
df10=df.iloc[:, [63,64,65,66,67,68,69]]
df11=df.iloc[:, [70,71,72,73,74,75,76]]
df12=df.iloc[:, [77,78,79,80,81,82,83]]
df13=df.iloc[:, [84,85,86,87,88,89,90]]
df14=df.iloc[:, [91,92,93,94,95,96,97]]
df15=df.iloc[:, [98,99,100,101,102,103,104]]
df16=df.iloc[:, [105,106,107,108,109,110,111]]



#*****

a = df1.index
b = df1.loc[:, "Pbuy_t"]
c = df1.loc[:, "P_ev_used"]
d = df1.loc[:, "P_bat_used"]  ###  1. ev
e = df1.loc[:, "P_ev_ch"]
f = df1.loc[:, "P_bat_ch"]
g = df1.loc[:, "P_pv_used"]
h = df1.loc[:, "P_loadt"]

color1="#FBE5E5"
color2="#F9FBE5"
color3="#F1E5FB"

dfx=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\ealı_1.xlsx")     #tablolar
dfx2=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\ealı_2.xlsx")
dfx3=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\easız_1.xlsx")
dfx4=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\easız_2.xlsx")

dfx5=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\senaryo3_tablo1.xlsx") #her bir senaryo için 2 tablo
dfx6=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\senaryo3_tablo2.xlsx")
dfx7=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\senaryo4_tablo1.xlsx")
dfx8=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Alış Satış Tablo\senaryo4_tablo2.xlsx")


df_fiyat=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Fiyatlandırma2.xlsx",index_col="Time")   #fiyatlandırma

df_evden_eve=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\evden eve\Yusuf1_evden_eve.xlsx",index_col="Time")  #evden eve, toplu
df_evden_eve=df_evden_eve.fillna(0)
#otomatize
a1_2='Household 1 to household 2'
a1_3='Household 1 to household 3'
a1_4='Household 1 to household 4'
a2_1='Household 2 to household 1'
a2_3='Household 2 to household 3'
a2_4='Household 2 to household 4'
a3_1='Household 3 to household 1'
a3_2='Household 3 to household 2'
a3_4='Household 3 to household 4'
a4_1='Household 4 to household 1'
a4_2='Household 4 to household 2'
a4_3='Household 4 to household 3'

name1="Bought energy"    #abdurahmanın senaryosuna göre sıralandı
name2="PV used"
name3="ESS used"
name4="EV used"
name5="ESS CH"
name6="Load"
name7="EV CH"
#yusuf:1-3, abd:2-4 senaryolar

price1="Grid-buy price"
price2="Grid-sell price"
price3="Peer price"

#power balance
power1="Power[kWh]"
power2="Time[15 min]"
#dynamic pricing
label1="Price[TL(₺)/kWh]"
label2="Time[15 min]"

#barmode
barmode1="relative"
barmode2="gridon" #template

#evden eve title
homes1="relative"  #barmode
homes2="gridon"    #template
homes3="Power[kWh]"
homes4="Time[15 min]"

#**********************************************************Pie Chart**********************************************
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df_pie_chart=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Pie Chart\pie_chart.xlsx")

labels = ["PV used", "ESS used", "EV used", "Microgrid", "Utility Company"]
sufficiency1=df_pie_chart.loc[0,:]
consumption1=df_pie_chart.loc[1,:]
sufficiency2=df_pie_chart.loc[2,:]
consumption2=df_pie_chart.loc[3,:]
sufficiency3=df_pie_chart.loc[4,:]
consumption3=df_pie_chart.loc[5,:]
sufficiency4=df_pie_chart.loc[6,:]
consumption4=df_pie_chart.loc[7,:]

pie_name1="Self Sufficiency"
pie_name2="Self Consumption"
hoverinfo="label+percent+name"
textinfo='label+percent'
title_text=""
colors_pie = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen',"blue"]
linecolor_pie='#000000'
width=2
hole=0
x1=0.17
x2=0.84
y1=1.15
y2=1.15




# df_evden_eve2=pd.read_excel(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\evden eve\aaa.xlsx",index_col="Time")  #kullanılmıyor
# df_evden_eve2=df_evden_eve.fillna(0)
#************************************************************Yusuf 1. simülasyon bitti*************************************************
# workbook2 = load_workbook(r"C:\Users\Hamza\Desktop\GAMS OUTPUTS\Abdurahman1.xlsx")  #Abdurrahman 1
# sheet2 = workbook2.active
# sheet2 = workbook2["power_balance"]
# list_home2=[]
# columns2=["Time","Pbuy_t","P_pv_used","P_ess_used","P_ev_used","P_ess_ch","P_load_t","P_ev_ch"]
# for value in sheet2.iter_rows(min_row=3,   #home 1
#    max_row=10,
#    min_col=3,
#    max_col=98,
#    values_only=True):
#    list_home2.append(value)
#
# from pandas import DataFrame
# df_home1_abd = DataFrame(list_home2)
#
# df_home1_abd=df_home1_abd.T
#
# df_home1_abd = df_home1_abd.fillna(value=0)
#
# df_home1_abd.columns=columns2
#
# df_home1_abd
#********************************************************************************Abdurrahman1, 1. ev bitti****************************************
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1("Welcome to the P2P Trading Visualization Platform", style={'text-align': 'center'}),  #app4'den ekledim.  dropdownlar ve bu yazı sonradan eklendi
    html.H5("Please select every asset for each house respectively", style={'text-align': 'left'}),
    html.Div(children=[
        html.Button('Add Chart', id='add-chart', n_clicks=0),   #chart ekleme butonu
    ]),
    html.Div(id='container', children=[]) ,                    #grafik için konteynır
    #html.Div(id='container2', children=[]) ,                    #grafik için konteynır
    # dash_table.DataTable(
    #     id='table',
    #     columns=[{"name": i, "id": i} for i in dfx.columns],
    #     data=dfx.to_dict('records'),
    #
    #     # Overflow into ellipsis
    #     style_cell={
    #         'overflow': 'hidden',
    #         'textOverflow': 'ellipsis',
    #         'maxWidth': 0,
    #     },
    #
    #     tooltip_delay=0, # 1000
    #     tooltip_duration=None, # 2000
    #     # *********************************************************************
    #     # column headers
    #     tooltip_header={
    #         'Gelir': 'Gelir',
    #         'Evler': 'Evler',
    #     })
])


@app.callback(
    Output('container', 'children'),   #changes to input value triggers callback, changes to state value does not trigger callback
    # Output('container2', 'children'),
    [Input('add-chart', 'n_clicks')],   #Tıklama sayısına(n'e) göre tetiklenir
    [State('container', 'children')]    #?
)
def display_graphs(n_clicks, div_children):
    new_child = html.Div(
        style={'width': '95%', 'display': 'inline-block', 'outline': 'thin lightgrey solid', 'padding': 10},  #tüm html için
        children=[

            html.H5("1. Household", style={'text-align': 'left'}),
            dcc.Dropdown(  # Komponent seçimleri callback fonk içinde çalıştı.
                id={
                    'type': 'selected1',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['PV', 'EV', 'ESS', 'NOT EXIST']],
                optionHeight=35,
                value=None,
                style={'width': "100%"},
                placeholder='Please select...',
                searchable=True,
                multi=True
            ),
            html.H5("2. Household", style={'text-align': 'left'}),
            dcc.Dropdown(
                id={
                    'type': 'selected2',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['PV', 'EV', 'ESS', 'NOT EXIST']],
                value=None,
                style={'width': "100%"},
                placeholder='Please select...',
                searchable=True,
                multi=True
            ),
            html.H5("3. Household", style={'text-align': 'left'}),
            dcc.Dropdown(
                id={
                    'type': 'selected3',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['PV', 'EV', 'ESS', 'NOT EXIST']],
                value=None,
                style={'width': "100%"},
                placeholder='Please select...',
                searchable=True,
                multi=True
            ),
            html.H5("4. Household", style={'text-align': 'left'}),
            dcc.Dropdown(
                id={
                    'type': 'selected4',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['PV', 'EV', 'ESS', 'NOT EXIST']],
                value=None,
                style={'width': "100%"},
                placeholder='Please select...',
                searchable=True,
                multi=True
            ),
            html.H5("Select Household", style={'text-align': 'left'}),
            dcc.Dropdown(
                id={
                    'type': 'selected5',
                    'index': n_clicks
                },
                options=[{'label': n, 'value': n} for n in ['House1', 'House2', 'House3', 'House4']],
                value=None,
                style={'width': "100%"},
                placeholder='Please select...',
                searchable=True,
                multi=True,
            ),

            dcc.Graph(    #pie chart
                id={
                    'type': 'dynamic-graph0',  # dinamik grafik türü
                    'index': n_clicks
                },
                figure={}  # component property
            ),
            # html.H5("Power Balance", style={'text-align': 'center'}),
            dcc.Graph(
                id={
                    'type': 'dynamic-graph',    #dinamik grafik türü
                    'index': n_clicks
                },
                figure={}   #component property
            ),
            dcc.Graph(
                id={
                    'type': 'dynamic-graph2',  # dinamik grafik türü
                    'index': n_clicks
                },
                figure={}  # component property
            ),
            dcc.Graph(
                id={
                    'type': 'dynamic-graph3',  # dinamik grafik türü
                    'index': n_clicks
                },
                figure={}  # component property
            ),
            dcc.Graph(
                id={
                    'type': 'dynamic-graph4',  # dinamik grafik türü
                    'index': n_clicks
                },
                figure={}  # component property
            ),

            dcc.RadioItems(  #radiobuttons   #grafik tipi seçimi
                id={
                    'type': 'dynamic-choice',
                    'index': n_clicks
                },
                options=[{'label': 'Bar Chart', 'value': 'bar'},
                         {'label': 'Line Chart', 'value': 'line'},
                         {'label': 'Pie Chart', 'value': 'pie'}],
                value='bar',  #default seçtik
            ),
            # dcc.Dropdown(
            #     id={
            #         'type': 'dynamic-dpn-s',
            #         'index': n_clicks
            #     },
            #     options=[{'label': s, 'value': s} for s in np.sort(df_home1.columns.unique())],
            #     multi=True,
            #     value=["Pbuy_t", "P_ev_used"],   #default seçtik.
            # )

            # dcc.Dropdown(
            #     id={
            #         'type': 'dynamic-dpn-ctg',
            #         'index': n_clicks
            #     },
            #     options=[{'label': c, 'value': c} for c in df_home1["Time"]],
            #     value=None,
            #     clearable=False
            # )
            html.H5("Table Results ", style={'text-align': 'center'}),
            dash_table.DataTable(
                id={
                    'type': 'table',
                    'index': n_clicks
                },
                # liste=["a","b","c","d","a","b","c"],
                #  columns=[{"name": [liste[a],i], "id": i} for i,a in dfx.columns],
                # columns=[{"name": i, "id": i} for i in dfx2.columns],
                columns=[
                    {"name": ["", "Type"], "id": "tip"},    #first table arrangements are done
                    {"name": ["Bought", "Energy(kWh)"], "id": "enerji_alis"},
                    {"name": ["Bought", "Paid(₺)"], "id": "maliyet_alis"},
                    {"name": ["Sold", "Energy(kWh)"], "id": "enerji_satis"},
                    {"name": ["Sold", "Revenue(₺)"], "id": "gelir_satis"},
                    {"name": ["Total", "Energy(kWh)"], "id": "enerji_toplam"},
                    {"name": ["Total", "Balance(₺)"], "id": "maliyet_toplam"},
                ],
                style_data_conditional=[
                    {
                        'if': {
                            # 'filter_query': '{maliyet_toplam} = "0"'
                            # 'row_index': 5,  # number | 'odd' | 'even'
                            'column_id': 'tip'
                        },

                        'backgroundColor': '#1FFDFB',
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_alis'
                        },

                        'backgroundColor': color1,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'maliyet_alis'
                        },

                        'backgroundColor': color1,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_satis'
                        },

                        'backgroundColor': color2,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'gelir_satis'
                        },

                        'backgroundColor': color2,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_toplam'
                        },

                        'backgroundColor': color3,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'maliyet_toplam'
                        },

                        'backgroundColor': color3,
                        'color': 'black'
                    },

                ],

                merge_duplicate_headers=True,
                data=[],

                style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0,
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'text_align': 'center',
                    'border': '1px solid grey'
                },
                style_header={ 'border': '2px solid black' },
                tooltip_delay=0, # 1000
                tooltip_duration=None, # 2000
            ),

            html.H5("Table Results For Each Home", style={'text-align': 'center'}),
            dash_table.DataTable(
                id={
                    'type': 'table2',
                    'index': n_clicks
                },
                # columns=[{"name": i, "id": i} for i in dfx.columns],
                columns=[
                    {"name": ["", "Type"], "id": "tip"},  # first table arrangements are done
                    {"name": ["Bought", "Energy(kWh)"], "id": "enerji_alis"},
                    {"name": ["Bought", "Paid(₺)"], "id": "maliyet_alis"},
                    {"name": ["Sold", "Energy(kWh)"], "id": "enerji_satis"},
                    {"name": ["Sold", "Revenue(₺)"], "id": "gelir_satis"},
                    {"name": ["Total", "Energy(kWh)"], "id": "enerji_toplam"},
                    {"name": ["Total", "Balance(₺)"], "id": "maliyet_toplam"},
                ],
                style_data_conditional=[
                    {
                        'if': {
                            # 'filter_query': '{maliyet_toplam} = "0"'
                            # 'row_index': 5,  # number | 'odd' | 'even'
                            'column_id': 'tip'
                        },

                        'backgroundColor': '#1FFDFB',
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_alis'
                        },

                        'backgroundColor': color1,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'maliyet_alis'
                        },

                        'backgroundColor': color1,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_satis'
                        },

                        'backgroundColor': color2,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'gelir_satis'
                        },

                        'backgroundColor': color2,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'enerji_toplam'
                        },

                        'backgroundColor': color3,
                        'color': 'black'
                    },
                    {
                        'if': {
                            'column_id': 'maliyet_toplam'
                        },

                        'backgroundColor': color3,
                        'color': 'black'
                    },

                ],
                merge_duplicate_headers=True,
                data=[],

                style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0,
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'text_align': 'center',
                    'border': '1px solid grey'

                },
                style_header={'border': '2px solid black'},
                tooltip_delay=0,  # 1000
                tooltip_duration=None,  # 2000
            )


        ]
    )
    div_children.append(new_child)
    return div_children

@app.callback(
    Output({'type': 'dynamic-graph0', 'index': MATCH}, 'figure'),
    Output({'type': 'dynamic-graph', 'index': MATCH}, 'figure'),
    Output({'type': 'dynamic-graph2', 'index': MATCH}, 'figure'),
    Output({'type': 'dynamic-graph3', 'index': MATCH}, 'figure'),
    Output({'type': 'dynamic-graph4', 'index': MATCH}, 'figure'),
    Output({'type': 'table', 'index': MATCH}, 'data'),
    Output({'type': 'table2', 'index': MATCH}, 'data'),
    [#Input(component_id={'type': 'dynamic-dpn-s', 'index': MATCH}, component_property='value'),  #for match, there is all and allsmaller
     #Input(component_id={'type': 'dynamic-dpn-num', 'index': MATCH}, component_property='value'),
     Input({'type': 'dynamic-choice', 'index': MATCH}, 'value'),
     Input(component_id={'type': 'selected1', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'selected2', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'selected3', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'selected4', 'index': MATCH}, component_property='value'),
     Input(component_id={'type': 'selected5', 'index': MATCH}, component_property='value')
    ])
def update_graph(chart_choice,selected1,selected2,selected3,selected4,selected5):  #respectively above(in inputs)
    #print(s_value)
    #dff = df[df['state'].isin(s_value)]

    print(selected1)
    print(selected2)
    print(selected3)
    print(selected4)
    print(selected5)

    if chart_choice == 'bar':
        if selected1 == ["PV","EV","ESS"] and  selected2 == ["PV","EV"] and selected3 == ["EV","ESS"] and selected4 == ["EV"] and selected5 == ["House1"]:
                import plotly.graph_objects as go
                fig0 = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
                fig0.add_trace(go.Pie(labels=labels, values=sufficiency1, name=pie_name1), 1, 1)
                fig0.add_trace(go.Pie(labels=labels, values=consumption1, name=pie_name2), 1, 2)

                fig0.update_traces(hole=hole, hoverinfo=hoverinfo, textinfo=textinfo,marker=dict(colors=colors_pie, line=dict(color=linecolor_pie, width=width)))
                fig0.update_layout(
                   title_text=title_text,
                annotations=[dict(text=pie_name1, x=x1, y=y1, font_size=20, showarrow=False),
                             dict(text=pie_name2, x=x2, y=y2, font_size=20, showarrow=False)])

                a = df1.index
                b = df1.loc[:, "Pbuy_t"]
                c = df1.loc[:, "P_ev_used"]
                d = df1.loc[:, "P_bat_used"]                                                       ###  1. ev
                e = df1.loc[:, "P_ev_ch"]
                f = df1.loc[:, "P_bat_ch"]
                g = df1.loc[:, "P_pv_used"]
                h = df1.loc[:, "P_loadt"]
                fig = Figure(data=[  # home1
                    Bar(name=name1, x=a, y=b),
                    Bar(name=name4, x=a, y=c),
                    Bar(name=name3, x=a, y=d),
                    Bar(name=name7, x=a, y=e),
                    Bar(name=name5, x=a, y=f),
                    Bar(name=name2, x=a, y=g),
                    Bar(name=name6, x=a, y=h)])
                # Change the bar mode
                fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)

                import plotly.graph_objects as go
                a2 = df_fiyat.index
                b2 = df_fiyat.loc[:, "x_buy_g"]
                c2 = df_fiyat.loc[:, "X_sell_g"]
                d2 = df_fiyat.loc[:, "x_buy_p1"]
                fig2 = Figure()
                fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
                fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
                fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
                fig2.update_layout(barmode='overlay',template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)   #2. grafik

                a3 = df_evden_eve.index
                b3 = df_evden_eve.loc[:, "1->2"]  #sell değerleri!, buy için name değerini tam tersi yap.
                c3 = df_evden_eve.loc[:, "1->3"]
                d3 = df_evden_eve.loc[:, "1->4"]

                b4 = df_evden_eve.loc[:, "2->1"]   #bought

                # fig3 = Figure(data=[  # home1 abdurrahman
                #     Bar(name=a1_2, x=a3, y=b3),
                #     Bar(name=a1_3, x=a3, y=c3),
                #     Bar(name=a1_4, x=a3, y=d3)])
                # fig3.update_layout(barmode=homes1,title="The Amount of Energy Sold by the 1. House", template=homes2, yaxis_title=homes3,xaxis_title=homes4)

                fig3 = Figure()
                fig3.add_trace(go.Scatter(x=a3, y=b3,mode='lines',name=a1_2))
                fig3.add_trace(go.Scatter(x=a3, y=c3,mode='lines',name=a1_3))
                fig3.add_trace(go.Scatter(x=a3, y=d3,mode='lines', name=a1_4))
                fig3.update_layout(template='gridon',title="The Amount of Energy Sold by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                fig4 = Figure()
                fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a2_1))
                fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a2_1))
                fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                # fig4 = Figure(data=[  # home1 abdurrahman
                #     Bar(name=a2_1, x=a3, y=b4)])
                # fig4.update_layout(barmode=homes1,title="The Amount of Energy Sold by the 1. House", template=homes2, yaxis_title=homes3,xaxis_title=homes4)
                #
                data=dfx.to_dict('records')
                data2 = dfx2.to_dict('records')
                return fig0,fig, fig2, fig3, fig4, data,data2
        elif selected1 == ["PV","EV","ESS"] and  selected2 == ["PV","EV"] and selected3 == ["EV","ESS"] and selected4 == ["EV"] and selected5 == ["House2"]:
                # dff = dff.groupby([ctg_value], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
                a = df2.index
                b = df2.loc[:, "Pbuy_t.1"]
                c = df2.loc[:, "P_ev_used.1"]
                #d = df2.loc[:, "P_bat_used.1"]                                                       ###  2. ev
                e = df2.loc[:, "P_ev_ch.1"]
                #f = df2.loc[:, "P_bat_ch.1"]
                g = df2.loc[:, "P_pv_used.1"]
                h = df2.loc[:, "P_loadt.1"]
                fig = Figure(data=[  # home1
                    Bar(name=name1, x=a, y=b),
                    Bar(name=name4, x=a, y=c),
                    #Bar(name=name3, x=a, y=d),
                    Bar(name=name7, x=a, y=e),
                    #Bar(name=name5, x=a, y=f),
                    Bar(name=name2, x=a, y=g),
                    Bar(name=name6, x=a, y=h)])
                # Change the bar mode
                fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)
                import plotly.graph_objects as go
                a2 = df_fiyat.index
                b2 = df_fiyat.loc[:, "x_buy_g"]
                c2 = df_fiyat.loc[:, "X_sell_g"]
                d2 = df_fiyat.loc[:, "x_buy_p1"]
                fig2 = Figure()
                fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
                fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
                fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
                fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

                a3 = df_evden_eve.index
                b3 = df_evden_eve.loc[:, "2->1"]  # sell değerleri!, buy için name değerini tam tersi yap.
                c3 = df_evden_eve.loc[:, "2->3"]
                d3 = df_evden_eve.loc[:, "2->4"]

                b4 = df_evden_eve.loc[:, "1->2"]  # bought
                c4 = df_evden_eve.loc[:, "4->2"]  # bought

                fig3 = Figure()
                fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a2_1))
                fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a2_3))
                fig3.add_trace(go.Scatter(x=a3, y=d3, mode='lines', name=a2_4))
                fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                fig4 = Figure()
                fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_2))
                fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a4_2))
                fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                data = dfx.to_dict('records')
                data2 = dfx2.to_dict('records')
                return fig,fig2,fig3,fig4,data,data2
        elif selected1 == ["PV","EV","ESS"] and  selected2 == ["PV","EV"] and selected3 == ["EV","ESS"] and selected4 == ["EV"] and selected5 == ["House3"]:
                # dff = dff.groupby([ctg_value], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
                a = df3.index
                b = df3.loc[:, "Pbuy_t.2"]
                c = df3.loc[:, "P_ev_used.2"]
                d = df3.loc[:, "P_bat_used.2"]                                                       ###  3. ev
                e = df3.loc[:, "P_ev_ch.2"]
                f = df3.loc[:, "P_bat_ch.2"]
                #g = df3.loc[:, "P_pv_used.2"]
                h = df3.loc[:, "P_loadt.2"]
                fig = Figure(data=[  # home1
                    Bar(name=name1, x=a, y=b),
                    Bar(name=name4, x=a, y=c),
                    Bar(name=name3, x=a, y=d),
                    Bar(name=name7, x=a, y=e),
                    Bar(name=name5, x=a, y=f),
                    #Bar(name=name2, x=a, y=g),
                    Bar(name=name6, x=a, y=h)])
                # Change the bar mode
                fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)
                import plotly.graph_objects as go
                a2 = df_fiyat.index
                b2 = df_fiyat.loc[:, "x_buy_g"]
                c2 = df_fiyat.loc[:, "X_sell_g"]
                d2 = df_fiyat.loc[:, "x_buy_p1"]

                fig2 = Figure()
                fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
                fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
                fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
                fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

                a3 = df_evden_eve.index
                b3=[]
                b4 = df_evden_eve.loc[:, "1->3"]  # bought
                c4 = df_evden_eve.loc[:, "2->3"]  # bought
                d4 = df_evden_eve.loc[:, "4->3"]  # bought

                fig3 = Figure()
                fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name='empty'))
                fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                fig4 = Figure()
                fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_3))
                fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_3))
                fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_3))
                fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                data = dfx.to_dict('records')
                data2 = dfx2.to_dict('records')
                return fig, fig2,fig3,fig4,data,data2
        elif selected1 == ["PV","EV","ESS"] and  selected2 == ["PV","EV"] and selected3 == ["EV","ESS"] and selected4 == ["EV"] and selected5 == ["House4"]:
                # dff = dff.groupby([ctg_value], as_index=False)[['detenues', 'under trial', 'convicts', 'others']].sum()
                a = df4.index
                b = df4.loc[:, "Pbuy_t.3"]
                c = df4.loc[:, "P_ev_used.3"]
                #d = df4.loc[:, "P_bat_used.3"]                                                       ###  4. ev
                e = df4.loc[:, "P_ev_ch.3"]
                #f = df4.loc[:, "P_bat_ch.3"]
                #g = df4.loc[:, "P_pv_used.3"]
                h = df4.loc[:, "P_loadt.3"]
                fig = Figure(data=[  # home1
                    Bar(name=name1, x=a, y=b),
                    Bar(name=name4, x=a, y=c),
                    #Bar(name=name3, x=a, y=d),
                    Bar(name=name7, x=a, y=e),
                    #Bar(name=name5, x=a, y=f),
                    #Bar(name=name2, x=a, y=g),
                    Bar(name=name6, x=a, y=h)])
                # Change the bar mode
                fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)

                import plotly.graph_objects as go
                a2 = df_fiyat.index
                b2 = df_fiyat.loc[:, "x_buy_g"]
                c2 = df_fiyat.loc[:, "X_sell_g"]
                d2 = df_fiyat.loc[:, "x_buy_p1"]

                fig2 = Figure()
                fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name='Buy from grid'))
                fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name='Sell to grid'))
                fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name='Buy from peer'))
                fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

                a3 = df_evden_eve.index
                b3 = df_evden_eve.loc[:, "4->2"]  # sell değerleri!, buy için name değerini tam tersi yap.
                c3 = df_evden_eve.loc[:, "4->3"]


                b4 = df_evden_eve.loc[:, "1->4"]  # bought
                c4 = df_evden_eve.loc[:, "2->4"]  # bought

                fig3 = Figure()
                fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a4_2))
                fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a4_3))
                fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                fig4 = Figure()
                fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_4))
                fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_4))
                fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

                data = dfx.to_dict('records')
                data2 = dfx2.to_dict('records')
                return fig, fig2, fig3, fig4, data, data2
        elif selected1 == ["PV","ESS"] and  selected2 == ["PV"] and selected3 == ["ESS"] and selected4 == ["NOT EXIST"] and selected5==["House1"]:
            #columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df5.index
            b = df5.loc[:, "Pbuy_t.4"]
            c = df5.loc[:, "P_pv_used.4"]
            d = df5.loc[:, "P_bat_used.4"]  ###                                                         5. ev
            #e = df5.loc[:, "P_ev_used.4"]
            f = df5.loc[:, "P_bat_ch.4"]
            g = df5.loc[:, "P_loadt.4"]
            #h = df5.loc[:, "P_ev_ch.4"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            # Change the bar mode
            fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance", yaxis_title=power1,xaxis_title=power2)

            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p2"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd_1->2"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "abd_1->2"]

            b4 = df_evden_eve.loc[:, "abd_2->1"]  # bought
            c4 = df_evden_eve.loc[:, "abd_3->1"]  # bought   #2->1 i kabul ederken diğerlerini kabul etmiyor.
            d4 = df_evden_eve.loc[:, "abd_4->1"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a1_2))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a1_2))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a2_1))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a3_1))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_1))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx3.to_dict('records')
            data2 = dfx4.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2
        elif selected1 == ["PV","ESS"] and  selected2 == ["PV"] and selected3 == ["ESS"] and selected4 == ["NOT EXIST"] and selected5==["House2"]:
            #columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df6.index
            b = df6.loc[:, "Pbuy_t.5"]
            c = df6.loc[:, "P_pv_used.5"]
            #d = df6.loc[:, "P_bat_used.5"]  ###                                                         6. ev
            #e = df6.loc[:, "P_ev_used.5"]
            #f = df6.loc[:, "P_bat_ch.5"]
            g = df6.loc[:, "P_loadt.5"]
            #h = df6.loc[:, "P_ev_ch.5"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                #Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                #Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])

            # Change the bar mode
            fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)

            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p2"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd_2->1"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "abd_2->1"]

            b4 = df_evden_eve.loc[:, "abd_1->2"]  # bought
            c4 = df_evden_eve.loc[:, "abd_3->2"]  # bought   #2->1 i kabul ederken diğerlerini kabul etmiyor.
            d4 = df_evden_eve.loc[:, "abd_4->2"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a2_1))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a2_1))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_2))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a3_2))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_2))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx3.to_dict('records')
            data2 = dfx4.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2
        elif selected1 == ["PV","ESS"] and  selected2 == ["PV"] and selected3 == ["ESS"] and selected4 == ["NOT EXIST"] and selected5==["House3"]:
            #columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df7.index
            b = df7.loc[:, "Pbuy_t.6"]
            #c = df7.loc[:, "P_pv_used.6"]
            d = df7.loc[:, "P_bat_used.6"]  ###                                                         7. ev
            #e = df7.loc[:, "P_ev_used.6"]
            f = df7.loc[:, "P_bat_ch.6"]
            g = df7.loc[:, "P_loadt.6"]
            #h = df7.loc[:, "P_ev_ch.6"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                #Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1,template=barmode2,title="Power Balance",yaxis_title=power1,xaxis_title=power2)

            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p2"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd_3->1"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "abd_3->2"]

            b4 = []

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a3_1))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a3_2))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name='empty'))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx3.to_dict('records')
            data2 = dfx4.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2
        elif selected1 == ["PV", "ESS"] and selected2 == ["PV"] and selected3 == ["ESS"] and selected4 == ["NOT EXIST"] and selected5 == ["House4"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df8.index
            b = df8.loc[:, "Pbuy_t.7"]
            # c = df8.loc[:, "P_pv_used.7"]
            # d = df8.loc[:, "P_bat_used.7"]  ###                                                          8. ev
            # e = df8.loc[:, "P_ev_used.7"]
            # f = df8.loc[:, "P_bat_ch.7"]
            g = df8.loc[:, "P_loadt.7"]
            #h = df8.loc[:, "P_ev_ch.7"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                # Bar(name=name2, x=a, y=c),
                # Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                # Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                # Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p2"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd_4->1"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "abd_4->2"]

            b4 = []

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name='4 to 1'))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name='4 to 2'))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name='empty'))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx3.to_dict('records')
            data2 = dfx4.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2

        #*****************senaryo3*********************Yusuf****************************************************

        elif selected1 == ["PV","ESS"] and selected2 == ["PV","ESS"] and selected3 == ["NOT EXIST"] and selected4 == ["NOT EXIST"] and selected5 == ["House1"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df9.index
            b = df9.loc[:, "Pbuy_t.8"]
            c = df9.loc[:, "P_pv_used.8"]
            d = df9.loc[:, "P_bat_used.8"]  ###                                                          8. ev
            #e = df9.loc[:, "P_ev_used.8"]
            f = df9.loc[:, "P_bat_ch.8"]
            g = df9.loc[:, "P_loadt.8"]
            #h = df9.loc[:, "P_ev_ch.8"]

            fig = Figure(data=[  # home1
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p3"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "ysf2_1->3"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "ysf2_1->4"]

            b4 = []

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a1_3))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a1_4))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name='empty'))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx5.to_dict('records')
            data2 = dfx6.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2


        elif selected1 == ["PV", "ESS"] and selected2 == ["PV", "ESS"] and selected3 == ["NOT EXIST"] and selected4 == ["NOT EXIST"] and selected5 == ["House2"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df10.index
            b = df10.loc[:, "Pbuy_t.9"]
            c = df10.loc[:, "P_pv_used.9"]
            d = df10.loc[:, "P_bat_used.9"]  ###                                                          8. ev
            #e = df10.loc[:, "P_ev_used.9"]
            f = df10.loc[:, "P_bat_ch.9"]
            g = df10.loc[:, "P_loadt.9"]
            #h = df10.loc[:, "P_ev_ch.9"]

            fig = Figure(data=[  # home1
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p3"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "ysf2_2->3"]  # sell değerleri!, buy için name değerini tam tersi yap.
            c3 = df_evden_eve.loc[:, "ysf2_2->4"]

            b4 = []

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a2_3))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a2_4))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name='empty'))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx5.to_dict('records')
            data2 = dfx6.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2


        elif selected1 == ["PV", "ESS"] and selected2 == ["PV", "ESS"] and selected3 == ["NOT EXIST"] and selected4 == ["NOT EXIST"] and selected5 == ["House3"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df11.index
            b = df11.loc[:, "Pbuy_t.10"]
            # c = df11.loc[:, "P_pv_used.10"]
            # d = df11.loc[:, "P_bat_used.10"]  ###                                                          8. ev
            # e = df11.loc[:, "P_ev_used.10"]
            # f = df11.loc[:, "P_bat_ch.10"]
            g = df11.loc[:, "P_loadt.10"]
            #h = df11.loc[:, "P_ev_ch.10"]

            fig = Figure(data=[  # home1
                Bar(name=name1, x=a, y=b),
                # Bar(name=name2, x=a, y=c),
                # Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                # Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                # Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p3"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = []

            b4 = df_evden_eve.loc[:, "ysf2_1->3"]
            c4 = df_evden_eve.loc[:, "ysf2_2->3"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name='empty'))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_3))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_3))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx5.to_dict('records')
            data2 = dfx6.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2


        elif selected1 == ["PV", "ESS"] and selected2 == ["PV", "ESS"] and selected3 == ["NOT EXIST"] and selected4 == ["NOT EXIST"] and selected5 == ["House4"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df12.index
            b = df12.loc[:, "Pbuy_t.11"]
            # c = df12.loc[:, "P_pv_used.11"]
            # d = df12.loc[:, "P_bat_used.11"]  ###                                                          8. ev
            # e = df12.loc[:, "P_ev_used.11"]
            # f = df12.loc[:, "P_bat_ch.11"]
            g = df12.loc[:, "P_loadt.11"]
            #h = df12.loc[:, "P_ev_ch.11"]

            fig = Figure(data=[
                Bar(name=name1, x=a, y=b),
                # Bar(name=name2, x=a, y=c),
                # Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                # Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p3"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = []

            b4 = df_evden_eve.loc[:, "ysf2_1->4"]
            c4 = df_evden_eve.loc[:, "ysf2_2->4"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name='empty'))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_4))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_4))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx5.to_dict('records')
            data2 = dfx6.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2

        #**********************senaryo4****************Abdurahman*******************************************************************

        elif selected1 == ["PV","ESS"] and selected2 == ["PV","ESS"] and selected3 == ["PV","ESS"] and selected4 == ["PV","ESS"] and selected5 == ["House1"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df13.index
            b = df13.loc[:, "Pbuy_t.12"]
            c = df13.loc[:, "P_pv_used.12"]
            d = df13.loc[:, "P_bat_used.12"]  ###                                                          8. ev
            #e = df13.loc[:, "P_ev_used.12"]
            f = df13.loc[:, "P_bat_ch.12"]
            g = df13.loc[:, "P_loadt.12"]
            #h = df13.loc[:, "P_ev_ch.12"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                #Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
                #Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p4"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd2_1->2"]
            c3 = df_evden_eve.loc[:, "abd2_1->3"]
            d3 = df_evden_eve.loc[:, "abd2_1->4"]

            b4 = df_evden_eve.loc[:, "abd2_2->1"]
            c4 = df_evden_eve.loc[:, "abd2_3->1"]
            d4 = df_evden_eve.loc[:, "abd2_4->1"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a1_2))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a1_3))
            fig3.add_trace(go.Scatter(x=a3, y=d3, mode='lines', name=a1_4))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a2_1))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a3_1))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_1))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 1. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx7.to_dict('records')
            data2 = dfx8.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2

        elif selected1 == ["PV","ESS"] and selected2 == ["PV","ESS"] and selected3 == ["PV","ESS"] and selected4 == ["PV","ESS"] and selected5 == ["House2"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df14.index
            b = df14.loc[:, "Pbuy_t.13"]
            c = df14.loc[:, "P_pv_used.13"]
            d = df14.loc[:, "P_bat_used.13"]  ###                                                          8. ev
            #e = df14.loc[:, "P_ev_used.13"]
            f = df14.loc[:, "P_bat_ch.13"]
            g = df14.loc[:, "P_loadt.13"]
            #h = df14.loc[:, "P_ev_ch.13"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
            # Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p4"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd2_2->1"]
            c3 = df_evden_eve.loc[:, "abd2_2->3"]
            d3 = df_evden_eve.loc[:, "abd2_2->4"]

            b4 = df_evden_eve.loc[:, "abd2_1->2"]
            c4 = df_evden_eve.loc[:, "abd2_3->2"]
            d4 = df_evden_eve.loc[:, "abd2_4->2"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a2_1))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a2_3))
            fig3.add_trace(go.Scatter(x=a3, y=d3, mode='lines', name=a2_4))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_2))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a3_2))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_2))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 2. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx7.to_dict('records')
            data2 = dfx8.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2
        elif selected1 == ["PV","ESS"] and selected2 == ["PV","ESS"] and selected3 == ["PV","ESS"] and selected4 == ["PV","ESS"] and selected5 == ["House3"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df15.index
            b = df15.loc[:, "Pbuy_t.14"]
            c = df15.loc[:, "P_pv_used.14"]
            d = df15.loc[:, "P_bat_used.14"]  ###                                                          8. ev
            #e = df15.loc[:, "P_ev_used.14"]
            f = df15.loc[:, "P_bat_ch.14"]
            g = df15.loc[:, "P_loadt.14"]
            #h = df15.loc[:, "P_ev_ch.14"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
            # Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p4"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd2_3->1"]
            c3 = df_evden_eve.loc[:, "abd2_3->2"]
            d3 = df_evden_eve.loc[:, "abd2_3->4"]

            b4 = df_evden_eve.loc[:, "abd2_1->3"]
            c4 = df_evden_eve.loc[:, "abd2_2->3"]
            d4 = df_evden_eve.loc[:, "abd2_4->3"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a3_1))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a3_2))
            fig3.add_trace(go.Scatter(x=a3, y=d3, mode='lines', name=a3_4))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_3))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_3))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a4_3))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 3. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx7.to_dict('records')
            data2 = dfx8.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2

        elif selected1 == ["PV","ESS"] and selected2 == ["PV","ESS"] and selected3 == ["PV","ESS"] and selected4 == ["PV","ESS"] and selected5 == ["House4"]:
            # columns = ["Time", "Pbuy_t", "P_pv_used", "P_ess_used", "P_ev_used", "P_ess_ch", "P_load_t", "P_ev_ch"]
            a = df16.index
            b = df16.loc[:, "Pbuy_t.15"]
            c = df16.loc[:, "P_pv_used.15"]
            d = df16.loc[:, "P_bat_used.15"]  ###                                                          8. ev
            #e = df16.loc[:, "P_ev_used.15"]
            f = df16.loc[:, "P_bat_ch.15"]
            g = df16.loc[:, "P_loadt.15"]
            #h = df16.loc[:, "P_ev_ch.15"]

            fig = Figure(data=[  # home1 abdurrahman
                Bar(name=name1, x=a, y=b),
                Bar(name=name2, x=a, y=c),
                Bar(name=name3, x=a, y=d),
                # Bar(name=name4, x=a, y=e),
                Bar(name=name5, x=a, y=f),
                Bar(name=name6, x=a, y=g)])
            # Bar(name=name7, x=a, y=h)])
            fig.update_layout(barmode=barmode1, template=barmode2, title="Power Balance",yaxis_title=power1, xaxis_title=power2)
            import plotly.graph_objects as go
            a2 = df_fiyat.index
            b2 = df_fiyat.loc[:, "x_buy_g"]
            c2 = df_fiyat.loc[:, "X_sell_g"]
            d2 = df_fiyat.loc[:, "x_buy_p4"]
            fig2 = Figure()
            fig2.add_trace(go.Scatter(x=a2, y=b2, mode='lines', name=price1))
            fig2.add_trace(go.Scatter(x=a2, y=c2, mode='lines', name=price2))
            fig2.add_trace(go.Scatter(x=a2, y=d2, mode='lines', name=price3))
            fig2.update_layout(template='gridon', title="Dynamic Price", yaxis_title=label1,xaxis_title=label2)  # 2. grafik

            a3 = df_evden_eve.index
            b3 = df_evden_eve.loc[:, "abd2_4->1"]
            c3 = df_evden_eve.loc[:, "abd2_4->2"]
            d3 = df_evden_eve.loc[:, "abd2_4->3"]

            b4 = df_evden_eve.loc[:, "abd2_1->4"]
            c4 = df_evden_eve.loc[:, "abd2_2->4"]
            d4 = df_evden_eve.loc[:, "abd2_3->4"]

            fig3 = Figure()
            fig3.add_trace(go.Scatter(x=a3, y=b3, mode='lines', name=a4_1))
            fig3.add_trace(go.Scatter(x=a3, y=c3, mode='lines', name=a4_2))
            fig3.add_trace(go.Scatter(x=a3, y=d3, mode='lines', name=a4_3))
            fig3.update_layout(template='gridon', title="The Amount of Energy Sold by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            fig4 = Figure()
            fig4.add_trace(go.Scatter(x=a3, y=b4, mode='lines', name=a1_4))
            fig4.add_trace(go.Scatter(x=a3, y=c4, mode='lines', name=a2_4))
            fig4.add_trace(go.Scatter(x=a3, y=d4, mode='lines', name=a3_4))
            fig4.update_layout(template='gridon', title="The Amount of Energy Bought by the 4. House",yaxis_title="Power(kWh)", xaxis_title="Time(15 min)")

            data = dfx7.to_dict('records')
            data2 = dfx8.to_dict('records')
            return fig,fig2,fig3,fig4, data,data2


        else:
            return {},{},{},{},{},[],[]
    # elif chart_choice == 'line':
    #     if len(s_value) == 0:
    #         return {}
    #     else:
    #         dff = dff.groupby([ctg_value, 'year'], as_index=False)
    #         [['detenues', 'under trial', 'convicts', 'others']].sum()
    #         fig = px.line(dff, x='year', y=num_value, color=ctg_value)
    #         return fig
    # elif chart_choice == 'pie':
    #     fig = px.pie(dff, names=ctg_value, values=num_value)
    #     return fig


if __name__ == '__main__':
    app.run_server(debug=True,port=8052,use_reloader=False)



# https://youtu.be/4gDwKYaA6ww