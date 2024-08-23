# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1
from typing import List
from queue import Queue
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		def BFS(vartex, adj, visited):
		    q = Queue()
		    visited[vartex] = 1
		    q.put((vartex, -1))
		    while q.empty() != True:
		        new = q.get()
		        node = new[0]
		        parent = new[1]
		        
		        for i in range(len(adj[node])):
		            new_elem = adj[node][i]
		            if new_elem == parent:
		                continue
		            if visited[new_elem] == 1:
		                return True
		            
		            visited[new_elem] = 1
		            q.put((new_elem, node))
		            
		    
		    return False
		    
		visited = [-1] * V
		for i in range(V):
		    if visited[i] == -1:
		        if BFS(i, adj, visited): # for this i, i use vartex
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