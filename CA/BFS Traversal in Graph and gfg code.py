#https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1?page=1&difficulty%5B%5D=0&category%5B%5D=Graph&sortBy=submissions

#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        ans = []
        q = Queue()
        q.put(0)
        visited = [0] * V
        visited[0] = 1
        
        while q.empty() != True:
            node = q.get() 
            ans.append(node)
            
            # now adj list traverse
            for i in range(len(adj[node])):
                new_elem = adj[node][i]
                if visited[new_elem] != 1:
                    q.put(new_elem)
                    visited[new_elem] = 1
        return ans

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
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends