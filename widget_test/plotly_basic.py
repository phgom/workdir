import plotly
from plotly.graph_objs import Scatter, Layout

list_x=[1,3,5,7]
list_y=[1,-1,2,-2]
plotly.offline.plot({

    "data": [Scatter(x=list_x, y=list_y)],

    "layout": Layout(title="hello world")

})

