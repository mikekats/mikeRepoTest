"""
Open Shortest Path First (OSFP) RFC 2328

Link state algorithm or Shortest Path First (SPF)

Dijkstra 

notes:
- Each router has a data base which describe the topology
- The DB describes also the links state of all router in the network
- The routers exchange messages (link States Advertisements LSA) only if the topology has changed
- Only the changes are transmitted
- The LSA message is trasmitted using IP multicast (flooding): Each neighboor router update its DB and forward the message to its neighboors except from the one which sent it
- Dijkstra find the shortest path and all the routing tables are updated
- Important to split the netwrok in local areas and hierarchical structure to avoid an overall update for a single change

Interior Gateway Protocols (IGP) inside an Autonomous System (AS):
- Routing Information Protocol (RIP)
- Open Shortest Path First (OSFP)

Exterior Gateway Protocols (EGP) for routing among ASs:
- Border Gateway Protocol (BGP)

"""

import pprint

# RT for routers, N for networks
network_component = ["RT1", "RT2", "RT3", "RT4", "RT5", "RT6", "N1", "N2", "N3", "N4", "N12"]
stub_networks = ["N1", "N2", "N4", "N12"]
#routing_table_headers = ["Destination" ,"Nexthop", "Cost"]

# Link State Database (topology table). From as keys of dictionary --> To as nested dictionary
# Assumed that retrieved from database
lsdb = {"RT1": {"N1": 3, "N3":1,},
		"RT2": {"N2": 3, "N3": 1},
		"RT3": {"RT6": 8,"N3": 1, "N4": 2},
		"RT4": {"RT5": 8, "N3": 1},
		"RT5": {"RT4": 8, "RT6": 7, "N12": 8},
		"RT6": {"RT3": 6,"RT5": 8},
		"N3": {"RT1": 0,"RT2": 0,"RT3": 0,"RT4": 0}}

# initializing routing tables dictionary for all network components
#routing_tables = {net_comp:{rt_header: [] for rt_header in routing_table_headers} for net_comp in set(network_component)-set(stub_networks)}

source_nodes = ["RT6"]
destination_nodes = network_component
dest = network_component[3] # RT4

visited_node = []
shortest_path = []

for source in source_nodes:

	visited_node.append(source)
	shortest_path.append(source)
	

	source_lsa = {source: {net_comp: lsdb.get(source).get(net_comp,float("Inf"))
				  for net_comp in network_component}}
	source_lsa[source][source] = 0
	#pprint.pprint(source_lsa)

	while visited_node[-1] != dest:

		min_cost = min([value for key, value in source_lsa[source].items() if key not in visited_node])
		next_candidates_hops = [key for key, value in source_lsa[source].items() if value == min_cost]
		next_hop = next_candidates_hops[0] if dest not in next_candidates_hops else dest

		visited_node.append(next_hop)

		#adj_lsa = {visited_node[-1]: {net_comp: lsdb.get(visited_node[-1]).get(net_comp,float("Inf")) 
		#			for net_comp in set(network_component)-set(visited_node)}}	
		#pprint.pprint(adj_lsa)

		for adj in set(lsdb[next_hop].keys())-set(visited_node):
			source_lsa[source][adj] = min(min_cost + lsdb[next_hop][adj], source_lsa[source][adj])
	pprint.pprint(source_lsa)
	print("Path: ", visited_node)
	print("Cost: ", source_lsa[source][dest])

