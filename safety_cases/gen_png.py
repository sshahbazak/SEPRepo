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

# # Add nodes with word wrapping
# G1_text = wrap_text('When needed the kill switch stops the motors on the targeted drone.', 3)
# S1_text = wrap_text('Argue that the RPIC can kill motors on the targeted drone when needed.', 7)
# O1_text = wrap_text('HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 4)

# dot.node('G1', f'<Goal G1>\n{G1_text}', shape='record', fillcolor='gray80', style='filled')
# dot.node('S1', f'<Strategy>\n{S1_text}', margin='0', width='4', height='.6', shape='polygon', skew='0.2', fillcolor='gray96', style='filled')
# dot.node('O1', f'<Solution O1>\n{O1_text}', shape='circle', margin='0', height='1.9', style='filled')

# # Add edges
# dot.edge('G1', 'S1')
# dot.edge('S1', 'O1')

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



# DESIGN IDEA 5 (IMPROVED WORD WRAP AND DYNAMIC NODES)

# from graphviz import Digraph
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def wrap_text(text, width):
#     words = text.split()
#     wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
#     return '\n'.join(wrapped_lines)

# # Specifications for the safety case
# specifications = {
#     'nodes': [
#         {'id': 'G1', 'label': 'Goal G1', 'text': 'When needed the kill switch stops the motors on the targeted drone.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
#         {'id': 'S1', 'label': 'Strategy', 'text': 'Argue that the RPIC can kill motors on the targeted drone when needed.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.0'},
#         {'id': 'O1', 'label': 'Solution S1', 'text': 'HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
#         {'id': 'T1', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (118 Passed, 12 Failed)\nL2 (2 Passed, 1 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True}
#     ],
#     'edges': [
#         ('G1', 'S1'),
#         ('S1', 'O1'),
#         ('O1', 'T1')
#     ]
# }

# # Create a new directed graph
# dot = Digraph()

# # Add nodes with word wrapping and reduced font size
# for node in specifications['nodes']:
#     if node.get('rows'):
#         text_lines = node['text'].split('\n')
#         label = f"""<
#             <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="tomato">
#                 <TR><TD COLSPAN="3">{text_lines[0]}</TD></TR>
#                 {''.join(f'<TR><TD>{line}</TD></TR>' for line in text_lines[1:])}
#             </TABLE>
#         >"""
#     else:
#         wrap_width = 3 if node['shape'] == 'circle' else 7
#         text = wrap_text(node['text'], wrap_width)
#         label = f'<{node["label"]}>\n{text}' if node['label'] else text
#     node_attrs = {
#         'fontsize': '15',
#         'margin': node.get('margin', '0.1'),
#         'fixedsize': 'false'
#     }
#     dot.node(node['id'], label, shape=node['shape'], fillcolor=node['fillcolor'], style='filled', **node_attrs)

# # Add edges
# for edge in specifications['edges']:
#     dot.edge(*edge)

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



# DESIGN 6: (PROMPT USER FOR CREATION OF NODES AND BRANCHES)

# from graphviz import Digraph
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def wrap_text(text, width):
#     words = text.split()
#     wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
#     return '\n'.join(wrapped_lines)

# def get_user_input():
#     nodes = []
#     edges = []
#     previous_node_id = None

#     while True:
#         node_type = input("Enter the type of node (Goal, Strategy, Solution, HiFUZZ, or 'done' to finish): ")
#         if node_type.lower() == 'done':
#             break

#         node_message = input("Enter the message for the node: ")
#         node_id = f"N{len(nodes) + 1}"

#         if node_type.lower() == 'goal':
#             shape = 'rectangle'
#             fillcolor = 'gray80'
#         elif node_type.lower() == 'strategy':
#             shape = 'parallelogram'
#             fillcolor = 'gray96'
#         elif node_type.lower() == 'solution':
#             shape = 'circle'
#             fillcolor = 'gray80'
#         elif node_type.lower() == 'hifuzz':
#             shape = 'none'
#             fillcolor = 'tomato'
#             node_message += '\n' + input("Enter additional HiFUZZ data (e.g., L1 (118 Passed, 12 Failed)): ")
#         else:
#             print("Invalid node type. Please enter again.")
#             continue

#         nodes.append({'id': node_id, 'label': node_type.capitalize(), 'text': node_message, 'shape': shape, 'fillcolor': fillcolor, 'margin': '0.1'})

#         if previous_node_id:
#             branch_choice = input("Is this node starting a new branch? (yes or no): ").lower()
#             if branch_choice == 'no':
#                 edges.append((previous_node_id, node_id))
        
#         previous_node_id = node_id

#     return nodes, edges

# # Get user input for nodes and edges
# spec_nodes, spec_edges = get_user_input()

# # Create a new directed graph
# dot = Digraph()

# # Add nodes with word wrapping and reduced font size
# for node in spec_nodes:
#     if node['shape'] == 'none':
#         text_lines = node['text'].split('\n')
#         label = f"""<
#             <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="tomato">
#                 <TR><TD>{text_lines[0]}</TD></TR>
#                 {''.join(f'<TR><TD>{line}</TD></TR>' for line in text_lines[1:])}
#             </TABLE>
#         >"""
#     else:
#         wrap_width = 3 if node['shape'] == 'circle' else 7
#         text = wrap_text(node['text'], wrap_width)
#         label = f'<{node["label"]}>\n{text}' if node['label'] else text
#     node_attrs = {
#         'fontsize': '15',
#         'margin': node.get('margin', '0.0'),
#         'fixedsize': 'false'
#     }
#     dot.node(node['id'], label, shape=node['shape'], fillcolor=node['fillcolor'], style='filled', **node_attrs)

# # Add edges
# for edge in spec_edges:
#     dot.edge(*edge)

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




# import pandas as pd
# from graphviz import Digraph
# import tkinter as tk
# from PIL import Image, ImageTk
# from tkinter import ttk

# def create_fault_tree_from_excel(file_path):
#     # Load data from Excel
#     df = pd.read_excel(file_path, sheet_name='Jane')

#     # Ensure column names are stripped of leading/trailing spaces
#     df.columns = df.columns.str.strip()

#     # Create a new directed graph
#     dot = Digraph()

#     # Add nodes to the graph
#     for _, row in df.iterrows():
#         node_id = row['ID']
#         label = row['Label']
#         node_type = row['Type'].strip().lower()
        
#         if node_type == 'basic event':
#             shape = 'ellipse'
#         elif node_type == 'and':
#             shape = 'box'
#         elif node_type == 'or':
#             shape = 'diamond'
#         else:
#             shape = 'ellipse'  # Default shape for unspecified types
        
#         dot.node(node_id, label, shape=shape)
    
#     # Add edges to the graph
#     for _, row in df.iterrows():
#         if pd.notnull(row['Parent ID']):
#             dot.edge(row['Parent ID'], row['ID'])
    
#     return dot

# # File path to the Excel file
# file_path = 'C:\\Users\\jmimnaugh\\Documents\\VScode\\shahbaz_repo\\SEPRepo\\safety_cases\\drone_dataset.xlsx'

# # Create the fault tree from Excel data
# fault_tree = create_fault_tree_from_excel(file_path)

# # Render the graph to a PNG file
# graph_image_path = 'fault_tree'
# fault_tree.render(graph_image_path, format='png')

# # Display the graph in a Tkinter window
# def display_graph_in_tkinter(image_path):
#     # Create a Tkinter window
#     root = tk.Tk()
#     root.title("Fault Tree Visualization")
    
#     # Load the image using PIL
#     image = Image.open(image_path + '.png')  # Add the .png extension
#     photo = ImageTk.PhotoImage(image)
    
#     # Create a label to display the image
#     label = ttk.Label(root, image=photo)
#     label.image = photo  # Keep a reference to the image
#     label.pack()
    
#     # Start the Tkinter main loop
#     root.mainloop()

# # Display the generated fault tree
# display_graph_in_tkinter(graph_image_path)



# import pydot
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# # Function to create and save the fault tree
# def create_fault_tree(file_path):
#     # Create a new directed graph
#     graph = pydot.Dot(graph_type='digraph', rankdir='TB')

#     # Create nodes
#     top_event = pydot.Node("Y", label="A drone completes its mission of\nflying in a triangle shape, even if it\nencounters a restricted area", shape='box')
#     and_gate = pydot.Node("AND", label="AND", shape='circle')
#     or_gate = pydot.Node("OR", label="OR", shape='ellipse')
#     geofence_setting = pydot.Node("A'", label="Geofence Setting: any values", shape='box')
#     throttle_setting = pydot.Node("B'", label="Throttle: any values", shape='box')
#     mode_offboard = pydot.Node("D", label="Mode: Offboard", shape='box')

#     # Add nodes to the graph
#     graph.add_node(top_event)
#     graph.add_node(and_gate)
#     graph.add_node(or_gate)
#     graph.add_node(geofence_setting)
#     graph.add_node(throttle_setting)
#     graph.add_node(mode_offboard)

#     # Create edges
#     graph.add_edge(pydot.Edge(top_event, and_gate))
#     graph.add_edge(pydot.Edge(and_gate, or_gate))
#     graph.add_edge(pydot.Edge(and_gate, mode_offboard))
#     graph.add_edge(pydot.Edge(or_gate, geofence_setting))
#     graph.add_edge(pydot.Edge(or_gate, throttle_setting))

#     # Save the graph as a PNG file
#     graph.write_png(file_path)

# # Function to display the image using matplotlib
# def display_image(file_path):
#     img = mpimg.imread(file_path)
#     plt.imshow(img)
#     plt.axis('off')
#     plt.show()

# # File path to save the image
# file_path = 'fault_tree.png'

# # Create the fault tree
# create_fault_tree(file_path)

# # Display the generated fault tree
# display_image(file_path)



# from graphviz import Digraph
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# def wrap_text(text, width):
#     words = text.split()
#     wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
#     return '\n'.join(wrapped_lines)

# # Specifications for the safety case
# specifications = {
#     'nodes': [
#         {'id': 'G1', 'label': 'Goal G1', 'text': 'When needed the kill switch stops the motors on the targeted drone.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
#         {'id': 'S1', 'label': 'Strategy', 'text': 'Argue that the RPIC can kill motors on the targeted drone when needed.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.0'},
#         {'id': 'O1', 'label': 'Solution S1', 'text': 'HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
#         {'id': 'T1', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (118 Passed, 12 Failed)\nL2 (2 Passed, 1 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True}
#     ],
#     'edges': [
#         ('G1', 'S1'),
#         ('S1', 'O1'),
#         ('O1', 'T1')
#     ]
# }

# # Create a new directed graph
# dot = Digraph()

# # Add nodes with word wrapping and reduced font size
# for node in specifications['nodes']:
#     if node.get('rows'):
#         text_lines = node['text'].split('\n')
#         label = f"""<
#             <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="tomato">
#                 <TR><TD COLSPAN="3">{text_lines[0]}</TD></TR>
#                 {''.join(f'<TR><TD>{line}</TD></TR>' for line in text_lines[1:])}
#             </TABLE>
#         >"""
#     else:
#         wrap_width = 3 if node['shape'] == 'circle' else 7
#         text = wrap_text(node['text'], wrap_width)
#         label = f'<{node["label"]}>\n{text}' if node['label'] else text
#     node_attrs = {
#         'fontsize': '15',
#         'margin': node.get('margin', '0.1'),
#         'fixedsize': 'false'
#     }
#     dot.node(node['id'], label, shape=node['shape'], fillcolor=node['fillcolor'], style='filled', **node_attrs)

# # Add edges
# for edge in specifications['edges']:
#     dot.edge(*edge)

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




# DESIGN 7: FULL SAFETY-CASE GRAPH WITH ZOOM AND SCROLLBARS: 

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from graphviz import Digraph

# Function to wrap text
def wrap_text(text, width):
    words = text.split()
    wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
    return '\n'.join(wrapped_lines)

# Specifications for the safety case
specifications = {
    'nodes': [
        {'id': 'G1', 'label': 'Goal G1', 'text': 'When needed the kill switch stops the motors on the targeted drone.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'S1', 'label': 'Strategy', 'text': 'Argue that the RPIC can kill motors on the targeted drone when needed.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.1'},
        {'id': 'G2', 'label': 'Goal G2', 'text': 'After the killswitch is depressed for 3 secs, the motors are killed.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'G3', 'label': 'Goal G3', 'text': 'When the drone is in the air, the user only kills motors for the intended drone.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'S2', 'label': 'Strategy', 'text': 'Argue that the operator has sufficient information and appropriate affordances to kill the motors on the correct drone.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.0'},
        {'id': 'G4', 'label': 'Goal G4', 'text': 'The RPIC has sufficient feedback on which drone is to be "killed".', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'G5', 'label': 'Goal G5', 'text': 'RPICs have at least two seconds to avert the kill after alerts are raised.', 'shape': 'rectangle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'S3', 'label': 'Strategy', 'text': 'Argue that the user has sufficient time to abort the kill if they attempt to kill the wrong drone', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.1'},
        {'id': 'O1', 'label': 'Solution S1', 'text': 'HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'T1', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (118 Passed, 12 Failed)\nL2 (2 Passed, 1 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True},
        {'id': 'O2', 'label': 'Solution S5', 'text': 'HiFUZZ tests show that the RPIC has >= 2 secs to abort after a killswitch warning.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'T2', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (52 Passed)\nL2 (0 Passed, 2 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True},
        {'id': 'O3', 'label': 'Solution S6', 'text': 'A verbal warning is issued when the killswitch is activated.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'O4', 'label': 'Solution S7', 'text': 'A mobile app depicts the current location of each sUAS inflight.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'},
        {'id': 'O5', 'label': 'Solution S8', 'text': 'A unique color is used to label each drone, its RC & associated GUI Icons.', 'shape': 'circle', 'fillcolor': 'gray80', 'margin': '0.1'}
    ],
    'edges': [
        ('G1', 'S1'),
        ('S1', 'G2'),
        ('S1', 'G3'),
        ('G2', 'O1'),
        ('O1', 'T1'),
        ('G3', 'S2'),
        ('G3', 'S3'),
        ('S2', 'G4'),
        ('S3', 'G5'),
        ('G4', 'O3'),
        ('G4', 'O4'),
        ('G5', 'O2'),
        ('O2', 'T2'),
        ('G4', 'O5')
    ]
}

# Create a new directed graph
dot = Digraph()

# Add nodes with word wrapping and reduced font size
for node in specifications['nodes']:
    if node.get('rows'):
        text_lines = node['text'].split('\n')
        label = f"""<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="tomato">
                <TR><TD COLSPAN="3">{text_lines[0]}</TD></TR>
                {''.join(f'<TR><TD>{line}</TD></TR>' for line in text_lines[1:])}
            </TABLE>
        >"""
    else:
        wrap_width = 3 if node['shape'] == 'circle' else 7
        text = wrap_text(node['text'], wrap_width)
        label = f'<{node["label"]}>\n{text}' if node['label'] else text
    node_attrs = {
        'fontsize': '15',
        'margin': node.get('margin', '0.1'),
        'fixedsize': 'false'
    }
    dot.node(node['id'], label, shape=node['shape'], fillcolor=node['fillcolor'], style='filled', **node_attrs)

# Add edges
for edge in specifications['edges']:
    dot.edge(*edge)

# Render the graph to a PNG file
graph_image_path = 'output_graph'
dot.render(graph_image_path, format='png')

class ZoomableImage:
    def __init__(self, canvas, image_path):
        self.canvas = canvas
        self.image_path = image_path
        self.image = Image.open(self.image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas_image = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

        self.scale = 1.0
        self.canvas.bind("<MouseWheel>", self.zoom)

    def zoom(self, event):
        if event.delta > 0:
            self.scale *= 1.1
        elif event.delta < 0:
            self.scale /= 1.1

        self.update_image()

    def update_image(self):
        width, height = int(self.image.width * self.scale), int(self.image.height * self.scale)
        resized_image = self.image.resize((width, height), Image.Resampling.LANCZOS)
        self.photo = ImageTk.PhotoImage(resized_image)

        self.canvas.itemconfig(self.canvas_image, image=self.photo)
        self.canvas.config(scrollregion=self.canvas.bbox(tk.ALL))

# Create a Tkinter window with scrollbars
root = tk.Tk()
root.title("Graph Visualization")

# Create a frame for the canvas and scrollbars
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Add a canvas in the frame
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add vertical scrollbar to the canvas
v_scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Add horizontal scrollbar to the canvas
h_scrollbar = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the canvas
canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

# Load the image and add zoom functionality
zoomable_image = ZoomableImage(canvas, graph_image_path + '.png')

# Start the Tkinter main loop
root.mainloop()
