# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def CycleDetect(node, parent, visited, adj):
		    visited[node] = 1
		    for i in range(len(adj[node])):
		        new_elem = adj[node][i]
		        if new_elem == parent:
		            continue
		        if visited[new_elem] == 1:
		            return True
		        if(CycleDetect(new_elem, node, visited, adj) == True):
		            return True
            return False
		    
		
        visited = [-1] * V
        for i in range(V):
            if visited[i] == -1:
                if(CycleDetect(i, -1, visited, adj)):
                    return True
        return False    

#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends