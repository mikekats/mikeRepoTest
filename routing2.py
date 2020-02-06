"""
Distance vector algorithm
Bellman-Ford

- Each router determines the distance to any known destination in distance vector table
- The table contains rows of destinations and their cost
- Each router creates its own table. The costs: 0 for itself, 1 for first neighboor and Inf for rest
- Periodically each router send the copy of the table to neighboors
- The receiver router, calculates the total cost to the destination by adding its own cost to the destination
- The routing table in each router is the minimum cost for each destination
- Recalcuation is needed when new table arrives
- simple but many messages/tables are transmitted among routers periodically. Control signal is getting enormous for huge networks

Find the minimum cost path for different number of hops

"""