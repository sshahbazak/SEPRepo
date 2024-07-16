from graphviz import Digraph

def wrap_text(text, width):
    words = text.split()
    wrapped_lines = [' '.join(words[i:i+width]) for i in range(0, len(words), width)]
    return '\n'.join(wrapped_lines)

# Specifications for the safety case
specifications = {
    'nodes': [
        {'id': 'G1', 'label': 'Goal G1', 'text': 'When needed the kill switch stops the motors on the targeted drone.', 'shape': 'rectangle', 'fillcolor': 'gray77', 'margin': '0.1'},
        {'id': 'S1', 'label': 'Strategy', 'text': 'Argue that the RPIC can kill motors on the targeted drone when needed.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.1'},
        {'id': 'G2', 'label': 'Goal G2', 'text': 'After the killswitch is depressed for 3 secs, the motors are killed.', 'shape': 'rectangle', 'fillcolor': 'gray77', 'margin': '0.1'},
        {'id': 'G3', 'label': 'Goal G3', 'text': 'When the drone is in the air, the user only kills motors for the intended drone.', 'shape': 'rectangle', 'fillcolor': 'gray77', 'margin': '0.1'},
        {'id': 'S2', 'label': 'Strategy', 'text': 'Argue that the operator has sufficient information and appropriate affordances to kill the motors on the correct drone.', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.0'},
        {'id': 'G4', 'label': 'Goal G4', 'text': 'The RPIC has sufficient feedback on which drone is to be "killed".', 'shape': 'rectangle', 'fillcolor': 'gray77', 'margin': '0.1'},
        {'id': 'G5', 'label': 'Goal G5', 'text': 'RPICs have at least two seconds to avert the kill after alerts are raised.', 'shape': 'rectangle', 'fillcolor': 'gray77', 'margin': '0.1'},
        {'id': 'S3', 'label': 'Strategy', 'text': 'Argue that the user has sufficient time to abort the kill if they attempt to kill the wrong drone', 'shape': 'parallelogram', 'fillcolor': 'gray96', 'margin': '0.1'},
        {'id': 'O1', 'label': 'Solution S1', 'text': 'HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.', 'shape': 'circle', 'fillcolor': 'gray89', 'margin': '0.1'},
        {'id': 'T1', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (118 Passed, 12 Failed)\nL2 (2 Passed, 1 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True},
        {'id': 'O2', 'label': 'Solution S5', 'text': 'HiFUZZ tests show that the RPIC has >= 2 secs to abort after a killswitch warning.', 'shape': 'circle', 'fillcolor': 'gray89', 'margin': '0.1'},
        {'id': 'T2', 'label': '', 'text': 'HiFUZZ Tests:\nL1 (52 Passed)\nL2 (0 Passed, 2 Failed)', 'shape': 'none', 'fillcolor': 'tomato', 'margin': '0.0', 'rows': True},
        {'id': 'O3', 'label': 'Solution S6', 'text': 'A verbal warning is issued when the killswitch is activated.', 'shape': 'circle', 'fillcolor': 'gray89', 'margin': '0.1'},
        {'id': 'O4', 'label': 'Solution S7', 'text': 'A mobile app depicts the current location of each sUAS inflight.', 'shape': 'circle', 'fillcolor': 'gray89', 'margin': '0.1'},
        {'id': 'O5', 'label': 'Solution S8', 'text': 'A unique color is used to label each drone, its RC & associated GUI Icons.', 'shape': 'circle', 'fillcolor': 'gray89', 'margin': '0.1'},
        {'id': 'B1', 'label': 'Backlogged', 'text': ' ', 'shape': 'rectangle', 'fillcolor': 'dodgerblue3', 'margin': '0.1'},
        {'id': 'B2', 'label': 'Backlogged', 'text': ' ', 'shape': 'rectangle', 'fillcolor': 'dodgerblue3', 'margin': '0.1'},
        {'id': 'U1', 'label': 'UX Test Passed', 'text': ' ', 'shape': 'rectangle', 'fillcolor': 'forestgreen', 'margin': '0.1'}
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
        ('G4', 'O5'),
        ('O3', 'B1'),
        ('O4', 'B2'),
        ('O5', 'U1'),
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

dot_source = dot.source

# Convert Graphviz dot to Cytoscape elements
def graphviz_to_cytoscape(dot_source):
    from pydot import graph_from_dot_data
    graphs = graph_from_dot_data(dot_source)
    graph = graphs[0]

    nodes = []
    edges = []

    for node in graph.get_nodes():
        node_id = node.get_name().strip('"')
        label = node.get_label().strip('"')
        nodes.append({
            'data': {'id': node_id, 'label': label},
            'position': {'x': 0, 'y': 0}  # Initial positions will be set later
        })

    for edge in graph.get_edges():
        source = edge.get_source().strip('"')
        target = edge.get_destination().strip('"')
        edges.append({'data': {'source': source, 'target': target}})

    return nodes, edges

nodes, edges = graphviz_to_cytoscape(dot_source)
