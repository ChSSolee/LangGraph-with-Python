from IPython.display import Image, display

def visualize_graph(graph):
    
    return display(Image(graph.get_graph().draw_mermaid_png()))