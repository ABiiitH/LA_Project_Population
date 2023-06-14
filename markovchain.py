import networkx as nx
import matplotlib.pyplot as plt

# Define the transition matrix
transition_matrix = [[0.7, 0.3, 0.0],
                     [0.2, 0.6, 0.2],
                     [0.0, 0.3, 0.7]]

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
num_states = len(transition_matrix)
states = range(1, num_states + 1)
G.add_nodes_from(states)

# Add edges to the graph
for i in states:
    for j in states:
        transition_prob = transition_matrix[i-1][j-1]
        if transition_prob > 0:
            G.add_edge(i, j, weight=transition_prob)

# Set the position of each node in the graph
pos = nx.spring_layout(G)

# Draw the nodes and edges
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray', arrows=True)

# Add labels to the nodes
node_labels = {node: f'State {node}' for node in G.nodes}
nx.draw_networkx_labels(G, pos , labels=node_labels)

# Add labels to the edges
edge_labels = {(u, v): f'{transition_matrix[u-1][v-1]:.2f}' for u, v in G.edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Set plot properties
plt.title('Transition Diagram - Markov Chain Population Model')
plt.axis('off')

# Display the graph
plt.show()