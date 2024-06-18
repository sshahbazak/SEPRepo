# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# from graphviz import Digraph

# # Create a new directed graph
# dot = Digraph()

# # Add nodes and edges
# dot.node('G1', '<Goal G1>\nWhen needed the kill switch stops the motors on the targeted drone.', shape='record', fillcolor='gray80', style='filled')
# dot.node('S1', '<Strategy>\nArgue that the RPIC can kill motors on the targeted drone when needed.', margin='0', width='4', height='.6', shape='polygon', fixedsize='true', skew='0.2', fillcolor='gray96', style='filled')
# dot.node('O1', '<Solution O1>\nHiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', shape='circle', margin='0', height='1.9', fixedsize='true', style='filled')
# dot.edge('G1', 'S1')
# dot.edge('S1', 'O1')

# # Render the graph to a PNG file
# graph_image_path = 'output_graph.png'
# dot.render(graph_image_path, format='png', cleanup=True)

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Graph Visualization")

# # Load the image using PIL
# image = Image.open(graph_image_path)
# photo = ImageTk.PhotoImage(image)

# # Create a label to display the image
# label = ttk.Label(root, image=photo)
# label.image = photo  # Keep a reference to the image
# label.pack()

# # Start the Tkinter main loop
# root.mainloop()




# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk
# from graphviz import Digraph

# # Create a new directed graph
# dot = Digraph()

# # Add nodes and edges
# dot.node('G1', '<Goal G1>\nWhen needed the kill switch stops the motors on the targeted drone.', shape='record', fillcolor='gray80', style='filled')
# dot.node('S1', '<Strategy>\nArgue that the RPIC can kill motors on the targeted drone when needed.', margin='0', width='4', height='.6', shape='polygon', skew='0.2', fillcolor='gray96', style='filled')
# dot.node('O1', '<Solution O1>\nHiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', shape='circle', margin='0', height='1.9', style='filled')
# dot.edge('G1', 'S1')
# dot.edge('S1', 'O1')

# # Render the graph to a PNG file
# graph_image_path = 'output_graph.png'
# dot.render(graph_image_path, format='png')

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Graph Visualization")

# # Load the image using PIL
# image = Image.open(graph_image_path + '.png')  # Add the .png extension
# photo = ImageTk.PhotoImage(image)

# # Create a label to display the image
# label = ttk.Label(root, image=photo)
# label.image = photo  # Keep a reference to the image
# label.pack()

# # Start the Tkinter main loop
# root.mainloop()



# DESIGN IDEA 3:

# from graphviz import Digraph

# # Create a new directed graph
# dot = Digraph()

# # Add nodes with word wrapping
# dot.node('G1', '<Goal G1>\nWhen needed the kill switch stops the motors on the targeted drone.', shape='record', fillcolor='gray80', style='filled')
# dot.node('S1', '<Strategy>\nArgue that the RPIC can kill motors on the targeted drone\nwhen needed.', margin='0', width='4', height='.6', shape='polygon', skew='0.2', fillcolor='gray96', style='filled')
# dot.node('O1', '<Solution O1>\nHiFUZZ tests pass on combos \nof flight modes, flying states, and\n killswitch press durations.', shape='circle', margin='0', height='1.9', style='filled')

# # Add edges
# dot.edge('G1', 'S1')
# dot.edge('S1', 'O1')

# # Render the graph to a PNG file
# graph_image_path = 'output_graph'
# dot.render(graph_image_path, format='png')

# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# # Create a Tkinter window
# root = tk.Tk()
# root.title("Graph Visualization")

# # Load the image using PIL
# image = Image.open(graph_image_path + '.png') # Add the .png extension
# photo = ImageTk.PhotoImage(image)

# # Create a label to display the image
# label = ttk.Label(root, image=photo)
# label.image = photo # Keep a reference to the image
# label.pack()

# # Start the Tkinter main loop
# root.mainloop()



# DESIGN IDEA 4 (DYNAMIC WORD WRAPPING)

from graphviz import Digraph
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def wrap_text(text, width):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])

# Create a new directed graph
dot = Digraph()

# Add nodes with word wrapping
G1_text = wrap_text('When needed the kill switch stops the motors on the targeted drone.', 51)
S1_text = wrap_text('Argue that the RPIC can kill motors on the targeted drone when needed.', 51)
O1_text = wrap_text('HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 51)

dot.node('G1', f'<Goal G1>\n{G1_text}', shape='record', fillcolor='gray80', style='filled')
dot.node('S1', f'<Strategy>\n{S1_text}', margin='0', width='4', height='.6', shape='polygon', skew='0.2', fillcolor='gray96', style='filled')
dot.node('O1', f'<Solution O1>\n{O1_text}', shape='circle', margin='0', height='1.9', style='filled')

# Add edges
dot.edge('G1', 'S1')
dot.edge('S1', 'O1')

# Render the graph to a PNG file
graph_image_path = '/mnt/data/output_graph'
dot.render(graph_image_path, format='png')

# Create a Tkinter window
root = tk.Tk()
root.title("Graph Visualization")

# Load the image using PIL
image = Image.open(graph_image_path + '.png') # Add the .png extension
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
label = ttk.Label(root, image=photo)
label.image = photo # Keep a reference to the image
label.pack()

# Start the Tkinter main loop
root.mainloop()
