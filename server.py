from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from Model import Market,Seller,Customer

width = 20
height = 20

def market_portrayal(agent):
    if agent is None:
        return

    portrayal = {"Shape": "rect", "Filled": "true", "w": 1, "h": 1, "Layer": 0}

    if type(agent) is Seller:
        portrayal["Color"] = "cornflowerblue"

    elif type(agent) is Customer:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "tomato"
        portrayal["r"] = 1
        portrayal["Layer"] = 1

    return portrayal

customer = {"Label": "Customer", "Color": "cornflowerblue"}
seller = {"Label": "Seller", "Color": "blueviolet"}
canvas = CanvasGrid(market_portrayal, width, height)
chart_count = ChartModule([customer, seller])
server = ModularServer(Market, [canvas,chart_count], name="Market simulation")
server.launch()