from collections import defaultdict, deque

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Preparing the graph
        adj_element = defaultdict(list)
        indegree = {}
        
        for child,parent in prerequisites:
            adj_element[parent].append(child)
            
            # Each node indegree recording
            indegree[child] = indegree.get(child,0) + 1
            
            
        # queue for maintaining list of node having 0 indegree
        indegree_queue_zero = deque([k for k in range(n) if k not in indegree])
        
        result = []
        
        # Creating while loop until there are no nodes in the indegree_queue_zero
        while indegree_queue_zero:
            
            # Pop one node with 0 in-degree
            vertex = indegree_queue_zero.popleft()
            result.append(vertex)
            
            # Reduce in-degree for all the neighbors
            if vertex in adj_element:
                for neighbor in adj_element[vertex]:
                    indegree[neighbor] -= 1
                    
                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        indegree_queue_zero.append(neighbor)
                        
        return result if len(result) == n else []