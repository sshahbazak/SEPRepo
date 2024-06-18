from graphviz import Digraph 
# Create a new directed graph 
dot = Digraph() 

# Add nodes and edges 
dot.node('G1', '<Goal G1>\nWhen needed the kill switch stops the motors on the targeted drone.', shape='record', fillcolor='gray80', style='filled') 
dot.node('S1', '<Strategy>\nArgue that the RPIC can kill motors on the targeted drone when needed.', margin='0', width='4', height='.6', shape='polygon', fixedsize='true', skew='0.2', fillcolor='gray96', style='filled') 
dot.node('O1', '<Solution O1>\nHiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', shape='circle', margin='0', height='1.9', fixedsize='true', style='filled') 
dot.edge('G1', 'S1') 
dot.edge('S1', 'O1') 

# Render the graph to a plain text file 
dot.format = 'plain' 
dot.render('output_graph', format='plain', cleanup=True) 

# Print the plain text output 
with open('output_graph.plain', 'r') as file: 
   print(file.read())
