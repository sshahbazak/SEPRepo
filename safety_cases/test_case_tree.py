import json
import dash
from dash import dcc, html, Input, Output, State
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import os

# Load external layouts
cyto.load_extra_layouts()

# Load the JSON data
json_file_path = os.path.join(os.getcwd(), 'C:\\Users\\jmimnaugh\\Documents\\VScode\\shahbaz_repo\\SEPRepo\\safety_cases\\tree_data.json')
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Extract nodes and edges from the JSON data
nodes = [
    {
        "data": {"id": node["id"], "label": f'{node["label"]}\n{node["text"]}', "shape": node["shape"], "fillcolor": node["fillcolor"]},
        "position": {"x": 0, "y": 0},  # Initial positions; will be laid out by Cytoscape
        "style": {
            "background-color": node["fillcolor"],
            "shape": node["shape"],
            "width": node.get("width", "200px"),
            "height": node.get("height", "180px")
        }
    }
    for node in data["nodes"]
]

edges = [
    {"data": {"source": edge["source"], "target": edge["target"]}}
    for edge in data["edges"]
]

# Define the default stylesheet for the graph
default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(label)',
            'text-wrap': 'wrap',
            'text-max-width': '180px',
            'background-color': 'data(fillcolor)',
            'border-width': '2px',
            'border-color': '#333333',
            'color': '#000000',
            'text-valign': 'center',
            'text-halign': 'center',
            'font-size': '21px',
            'shape': 'data(shape)'  # Use shape from data
        }
    },
    {'selector': 'edge', 'style': {'curve-style': 'bezier'}},
]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    cyto.Cytoscape(
                        id="cytoscape",
                        elements=nodes + edges,
                        layout={"name": "dagre"},  # Use the dagre layout
                        style={"width": "100%", "height": "800px"},
                        stylesheet=default_stylesheet,
                    ),
                    md=8,
                ),
                dbc.Col(
                    [
                        dbc.Input(id="node-id", placeholder="Node ID", disabled=True),
                        dbc.Input(id="node-label", placeholder="Edit Node Label"),
                        dbc.Input(id="node-text", placeholder="Edit Node Text"),  # New input for node text
                        dbc.Row(
                            [
                                dbc.Col(dbc.Button("Update Node", id="update-node-btn", color="primary"), width="auto"),
                                dbc.Col(dbc.Button("Delete Node", id="delete-node-btn", color="danger"), width="auto"),
                            ],
                            justify="start",
                            align="center",
                            className="g-1",  # Use Bootstrap class for horizontal gap
                        ),
                        html.Hr(),
                        dbc.Input(id="new-node-id", placeholder="New Node ID"),
                        dbc.Input(id="new-node-label", placeholder="New Node Label"),
                        dbc.Input(id="new-node-text", placeholder="New Node Text"),
                        dbc.Input(id="new-node-shape", placeholder="New Node Shape"),
                        dbc.Input(id="new-node-color", placeholder="New Node Color"),
                        dbc.Button("Add Node", id="add-node-btn", color="success"),
                        html.Hr(),
                        dbc.Input(id="source-node-id", placeholder="Source Node ID"),
                        dbc.Input(id="target-node-id", placeholder="Target Node ID"),
                        dbc.Button("Add Edge", id="add-edge-btn", color="success"),
                    ],
                    md=4,
                ),
            ]
        ),
    ],
    fluid=True,
)

@app.callback(
    [Output("node-id", "value"), Output("node-label", "value"), Output("node-text", "value")],  # Removed delete button output
    [Input("cytoscape", "tapNodeData")],
)
def display_tapped_node(data):
    if data:
        label, text = data["label"].split('\n', 1)
        return data["id"], label, text
    return "", "", ""

@app.callback(
    Output("cytoscape", "elements"),
    [Input("update-node-btn", "n_clicks"),
     Input("add-node-btn", "n_clicks"),
     Input("add-edge-btn", "n_clicks"),
     Input("delete-node-btn", "n_clicks")],  # Directly listen to delete-node-btn
    [State("node-id", "value"), State("node-label", "value"), State("node-text", "value"), State("cytoscape", "elements"),  # Added node-text state
     State("new-node-id", "value"), State("new-node-label", "value"),
     State("new-node-text", "value"), State("new-node-shape", "value"),
     State("new-node-color", "value"), State("source-node-id", "value"),
     State("target-node-id", "value")]
)
def update_elements(n_clicks_update, n_clicks_add_node, n_clicks_add_edge, n_clicks_delete_node,
                    node_id, node_label, node_text, elements, new_node_id, new_node_label,  # Added node_text parameter
                    new_node_text, new_node_shape, new_node_color, source_node_id, target_node_id):
    ctx = dash.callback_context
    if not ctx.triggered:
        return elements
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "update-node-btn" and node_id and node_label:
        for element in elements:
            if element["data"]["id"] == node_id:
                element["data"]["label"] = f'{node_label}\n{node_text}'  # Update both label and text
    elif button_id == "add-node-btn" and new_node_id and new_node_label:
        new_node = {
            "data": {"id": new_node_id, "label": f'{new_node_label}\n{new_node_text}', "shape": new_node_shape, "fillcolor": new_node_color},
            "style": {
                "background-color": new_node_color,
                "shape": new_node_shape,
                "width": "200px",  # You can adjust the default width
                "height": "180px"  # You can adjust the default height
            }
        }
        elements.append(new_node)
    elif button_id == "add-edge-btn" and source_node_id and target_node_id:
        # Check if source and target nodes exist
        node_ids = {element["data"]["id"] for element in elements if "id" in element["data"]}
        if source_node_id in node_ids and target_node_id in node_ids:
            new_edge = {"data": {"source": source_node_id, "target": target_node_id}}
            elements.append(new_edge)
        else:
            print(f"Cannot create edge with non-existent source '{source_node_id}' or target '{target_node_id}'.")
    elif button_id == "delete-node-btn" and node_id:  # Use node_id instead of delete_node_id
        elements = [element for element in elements if element["data"]["id"] != node_id and element["data"].get("source") != node_id and element["data"].get("target") != node_id]

    return elements

if __name__ == "__main__":
    app.run_server(debug=True)
