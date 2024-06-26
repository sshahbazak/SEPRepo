import tkinter as tk
from tkinter import ttk

class GraphDisplayApp:
    def __init__(self, root, graph_data):
        self.root = root
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.parse_graph_data(graph_data)

    def parse_graph_data(self, graph_data):
        lines = graph_data.strip().split('\n')
        for line in lines:
            if line.startswith('node'):
                self.display_node(line)
            elif line.startswith('edge'):
                self.display_edge(line)

    def display_node(self, node_data):
        parts = node_data.split()
        node_id = parts[1]
        x = float(parts[2]) * 100  # Scaling positions for better visualization
        y = float(parts[3]) * 100
        width = float(parts[4]) * 100
        height = float(parts[5]) * 100
        label = " ".join(parts[6:]).strip('"')
        
        self.canvas.create_rectangle(x - width / 2, y - height / 2, x + width / 2, y + height / 2, fill='lightgray')
        self.canvas.create_text(x, y, text=label, font=('Arial', 10), width=width - 10)

    def display_edge(self, edge_data):
        parts = edge_data.split()
        source = parts[1]
        target = parts[2]
        points = list(map(float, parts[4:-2]))  # Exclude the last two parts (solid black)
        scaled_points = [point * 100 for point in points]
        self.canvas.create_line(*scaled_points, fill='black')

# Sample plain text graph data
graph_data = """
graph 1 5.5139 4.0139
node G1 2.7569 3.7569 5.5139 0.51389 "<Goal G1>\nWhen needed the kill switch stops the motors on the targeted drone." filled record black gray80
node S1 2.7569 2.7014 4 0.59722 "<Strategy>\nArgue that the RPIC can kill motors on the targeted drone when needed." filled polygon black gray96
node O1 2.7569 0.95139 1.9028 1.9028 "<Solution O1>\nHiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations." filled circle black lightgrey
edge G1 S1 4 2.7569 3.5047 2.7569 3.3973 2.7569 3.2671 2.7569 3.1436 solid black
edge S1 O1 4 2.7569 2.3992 2.7569 2.2973 2.7569 2.1757 2.7569 2.0471 solid black
stop
"""

# Create the main window
root = tk.Tk()
root.title("Graph Visualization")

# Create and display the graph
app = GraphDisplayApp(root, graph_data)

# Start the Tkinter main loop
root.mainloop()
