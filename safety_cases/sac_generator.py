import datetime

class GraphVizFile:
    def __init__(self):
        self.filename = "my_sac.gv"
        self.nodes = []
        self.links = []
        self._initiate_new_file()

    def _initiate_new_file(self):
        with open(self.filename, 'w') as file:
            file.write('digraph G {\n')
            file.write('    fontname="Arial"\n')
            file.write('    fontsize=12\n')
            file.write('    graph [ranksep=".2", pad=".2", nodesep="0.2"];\n')
            file.write('    edge [];\n\n')

    def _format_description(self, description, line_length):
        words = description.split()
        formatted_lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 > line_length:  # line length limit
                formatted_lines.append(current_line)
                current_line = word
            else:
                if current_line:
                    current_line += " "
                current_line += word

        if current_line:
            formatted_lines.append(current_line)

        return "\\n".join(formatted_lines)

    def add_goal(self, id, description):
        formatted_description = self._format_description(description, 18)
        text = f'{id}[label = "<Goal {id}>\n{formatted_description}", shape="record", fillcolor="gray80"]'
        self.nodes.append(text)

    def add_strategy(self, id, description):
        formatted_description = self._format_description(description, 36)
        text = (f'{id}[margin=0, width=4, height=.6, shape=polygon, fixedsize=true, '
                f'label="<Strategy>\n{formatted_description}", skew=0.2, fillcolor="gray96"]')
        self.nodes.append(text)

    def add_solution(self, id, description):
        formatted_description = self._format_description(description, 18)
        text = (f'{id}[label = "<Solution {id}>\n{formatted_description}", '
                f'shape=circle, margin=0, height=1.9, fixedsize=true]')
        self.nodes.append(text)

    def add_link(self, source, target):
        link = f'{source}->{target}'
        self.links.append(link)

    def _write_to_file(self, text):
        with open(self.filename, 'a') as file:
            file.write(text + '\n')

    def close_file(self):
        self.nodes.sort()
        self.links.sort()
        with open(self.filename, 'a') as file:
            for node in self.nodes:
                file.write(f'    {node}\n')
            for link in self.links:
                file.write(f'    {link}\n')
            file.write('}\n')

# Example usage:
gv_file = GraphVizFile()
gv_file.add_goal("G1", "When needed the kill switch stops the motors on the targeted drone.")
gv_file.add_strategy("S1", "Argue that the RPIC can kill motors on the targeted drone when needed.")
gv_file.add_solution("O1", "HiFUZZ tests pass on combos of flight modes, flying states, and killswitch press durations.")
gv_file.add_link("G1", "S1")
gv_file.add_link("S1", "O1")
gv_file.close_file()

