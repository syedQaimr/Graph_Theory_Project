import networkx as nx
from nltk.tokenize import word_tokenize

def construct_graph(document):
  # Tokenize the document into words
  words = word_tokenize(document)

  G = nx.DiGraph()  # Create a directed graph G

  for i in range(len(words) - 1):
    # Add an edge between word[i] and word[i + 1]
    if G.has_edge(words[i], words[i + 1]):
      # Increment weight for existing edge
      G[words[i]][words[i + 1]]['weight'] += 1
    else:
      # Add edge with weight 1
      G.add_edge(words[i], words[i + 1], weight=1)

  return G

def calculate_degree(graph):
  degrees = dict(graph.degree())
  return degrees

def find_connected_subgraphs(graph):
  # Since connected_components is not for directed graphs, use weakly_connected_components
  weakly_connected_components = list(nx.weakly_connected_components(graph))
  subgraphs = [graph.subgraph(component) for component in weakly_connected_components]
  return list(subgraphs)

def find_frequent_subgraphs(subgraphs):
  fcs_count = {}
  for subgraph in subgraphs:
    count = 0
    for other_subgraph in subgraphs:
      if nx.is_isomorphic(subgraph, other_subgraph):
        count += 1
    fcs_count[subgraph] = count
  return fcs_count

def filter_frequent_subgraphs(fcs_count, min_frequency=50):
  frequent_subgraphs = {subgraph: count for subgraph, count in fcs_count.items() if count >= min_frequency}
  return frequent_subgraphs


# Example usage:
def file_text(input_file):
  Text=[]
  with open(input_file, 'r', encoding='utf-8') as f:
    for text in f:
      Text=text
  return Text
  
input_file="beauty/preprocessed_text1.txt"
document=file_text(input_file)

G = construct_graph(document)
degrees = calculate_degree(G)

subgraphs = find_connected_subgraphs(G)  # Use find_connected_subgraphs with modification

fcs_count = find_frequent_subgraphs(subgraphs)
frequent_fcs = filter_frequent_subgraphs(fcs_count)

# print("Node degrees:", degrees)
# print("Number of connected subgraphs:", len(subgraphs))
# print("Frequent subgraphs (count >= 2):", frequent_fcs)


# print(G.nodes())
# print(G.edges())
