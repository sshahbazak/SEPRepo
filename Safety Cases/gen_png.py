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



# DESIGN IDEA 4 (DYNAMIC WORD WRAPPING WITH STRINGS)

from graphviz import Digraph
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def wrap_text(text, width):
    words = text.split()
    wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
    return '\n'.join(wrapped_lines)

# Create a new directed graph
dot = Digraph()

# Add nodes with word wrapping
G1_text = wrap_text('When needed the kill switch stops the motors on the targeted drone.', 3)
S1_text = wrap_text('Argue that the RPIC can kill motors on the targeted drone when needed.', 7)
O1_text = wrap_text('HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 4)

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



# DESIGN IDEA 5 

# from graphviz import Digraph
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def wrap_text(text, width):
#     words = text.split()
#     wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
#     return '\n'.join(wrapped_lines)

# # Create a new directed graph
# dot = Digraph()

# # Set the graph size and dpi
# dot.attr(size='10,10')
# dot.attr(dpi='100')

# # Add nodes with word wrapping and reduced font size
# G1_text = wrap_text('When needed, the kill switch stops the motors on the targeted drone.', 7)
# S1_text = wrap_text('Argue that the RPIC can kill motors on the targeted drone when needed.', 7)
# G2_text = wrap_text('After the killswitch is depressed for 3 secs, the motors are killed.', 7)
# G3_text = wrap_text('When the drone is in the air, the user only kills motors for the intended drone.', 7)
# G4_text = wrap_text('The RPIC has sufficient feedback on which drone is to be killed.', 7)
# G5_text = wrap_text('RPICs have at least two seconds to avert the kill after alerts are raised.', 7)
# S2_text = wrap_text('HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 7)
# S5_text = wrap_text('HiFUZZ tests show that the RPIC has >= 2 secs to abort after a killswitch warning.', 7)
# S6_text = wrap_text('A verbal warning is issued when the killswitch is activated.', 7)
# S7_text = wrap_text('A mobile app depicts the current location of each sUAS in flight.', 7)
# S8_text = wrap_text('A unique color is used to label each drone, its RC and associated GUI Icons.', 7)
# T1_text = wrap_text('HiFUZZ Tests:\nL1 (118 Passed, 12 Failed)\nL2 (2 Passed, 1 Failed)', 7)
# T2_text = wrap_text('HiFUZZ Tests:\nL1 (52 Passed)\nL2 (0 Passed, 2 Failed)', 7)
# B1_text = wrap_text('Backlogged', 1)
# B2_text = wrap_text('UX Tests Passed', 2)

# node_attrs = {'fontsize': '10', 'width': '2.5', 'height': '1.0'}
# dot.node('G1', f'<Goal G1>\n{G1_text}', shape='record', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S1', f'<Strategy>\n{S1_text}', shape='polygon', fillcolor='gray96', style='filled', **node_attrs)
# dot.node('G2', f'<Goal G2>\n{G2_text}', shape='record', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('G3', f'<Goal G3>\n{G3_text}', shape='record', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('G4', f'<Goal G4>\n{G4_text}', shape='record', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('G5', f'<Goal G5>\n{G5_text}', shape='record', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S2', f'<Solution S2>\n{S2_text}', shape='circle', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S5', f'<Solution S5>\n{S5_text}', shape='circle', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S6', f'<Solution S6>\n{S6_text}', shape='circle', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S7', f'<Solution S7>\n{S7_text}', shape='circle', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('S8', f'<Solution S8>\n{S8_text}', shape='circle', fillcolor='gray80', style='filled', **node_attrs)
# dot.node('T1', f'{T1_text}', shape='box', fillcolor='red', style='filled', **node_attrs)
# dot.node('T2', f'{T2_text}', shape='box', fillcolor='red', style='filled', **node_attrs)
# dot.node('B1', f'{B1_text}', shape='box', fillcolor='blue', style='filled', **node_attrs)
# dot.node('B2', f'{B2_text}', shape='box', fillcolor='green', style='filled', **node_attrs)

# # Add edges
# dot.edge('G1', 'S1')
# dot.edge('S1', 'G2')
# dot.edge('S1', 'G3')
# dot.edge('G3', 'G4')
# dot.edge('G3', 'G5')
# dot.edge('G2', 'S2')
# dot.edge('G4', 'S6')
# dot.edge('G4', 'S7')
# dot.edge('G4', 'S8')
# dot.edge('G5', 'S5')
# dot.edge('S2', 'T1')
# dot.edge('S5', 'T2')
# dot.edge('S6', 'B1')
# dot.edge('S7', 'B1')
# dot.edge('S8', 'B2')

# # Render the graph to a PNG file
# graph_image_path = '/mnt/data/output_graph'
# dot.render(graph_image_path, format='png')

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



