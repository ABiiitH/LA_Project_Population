import networkx as nx
import matplotlib.pyplot as plt

food_web = nx.DiGraph()

food_web.add_nodes_from(['Environment', 'Phytoplankton', 'Cyanobacteria', 'Brine Shrimp',
                        'Brine Fly', 'Corixidae', 'Birds'])

food_web.add_edges_from([('Environment', 'Phytoplankton'),
                         ('Environment', 'Cyanobacteria'),
                         ('Phytoplankton', 'Brine Shrimp'),
                         ('Cyanobacteria', 'Brine Fly'),
                         ('Brine Shrimp', 'Corixidae'),
                         ('Brine Fly', 'Corixidae'),
                         ('Corixidae', 'Birds'),
                         ('Brine Shrimp', 'Birds'),
                         ('Brine Fly', 'Birds'),
                         ('Phytoplankton', 'Environment'),
                         ('Cyanobacteria', 'Environment'),
                         ('Brine Shrimp', 'Environment'),
                         ('Brine Fly', 'Environment'),
                         ('Corixidae', 'Environment'),
                         ('Birds', 'Environment'),])

nx.draw(food_web, with_labels=True, node_color='lightblue', node_size=7000)
plt.show()
