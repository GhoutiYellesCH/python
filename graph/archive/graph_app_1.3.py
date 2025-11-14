import re
import networkx as nx
from pyvis.network import Network
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel
import webbrowser  # Import the webbrowser module

class GraphApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.vault_path_input = TextInput(text="/path/to/your/obsidian/vault")
        layout.add_widget(self.vault_path_input)

        self.file_types_input = TextInput(text="md")
        layout.add_widget(self.file_types_input)

        self.generate_button = Button(text="Generate Graph")
        self.generate_button.bind(on_press=self.open_webview)
        layout.add_widget(self.generate_button)

        return layout

    def open_webview(self, instance):
        html_file = self.generate_graph()
        webbrowser.open(html_file)  

    def generate_graph(self):
        vault_path = self.vault_path_input.text
        file_types = self.file_types_input.text.split(",")
    
        notes = extract_notes_from_vault(vault_path, file_types)
        graph = create_network_graph(notes)
        html_file = show_graph(graph)
    
        return html_file
        self.webview.load_url(html_file)

def extract_notes_from_vault(vault_path, file_types):
    notes = []
    for root, _, files in os.walk(vault_path):
        for file in files:
            if file.endswith(tuple(file_types)):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="latin1") as f:
                    content = f.read()

                    # Extract title (assuming it's in the first line)
                    title = re.match(r"^(#+ )?(.*)", content).group(2).strip()

                    # Extract links (assuming they are in the format [[link]])
                    links = re.findall(r"\[\[(.*?)\]\]", content)

                    notes.append({"title": title, "links": links})

    return notes

def create_network_graph(notes):
    G = nx.Graph()
    for note in notes:
        G.add_node(note["title"])
        for link in note["links"]:
            G.add_edge(note["title"], link)
    return G

def show_graph(graph, output_file="graph.html"):
    net = Network(notebook=True,height="750px", width="100%", bgcolor="#222222", font_color="white", select_menu=True)
    #net.toggle_physics(True)
    net.show_buttons()
    net.from_nx(graph)
    for node in graph.nodes():
        net.add_node(node, title=f"Node {node}")

    net.show(output_file)
    return output_file

if __name__ == "__main__":

    GraphApp().run()


