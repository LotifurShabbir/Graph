# GFG problem
from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        def DFS_Topo(node, adj, visited, s):
            visited[node] = 1
            # visiting its neighbours
            for i in range(len(adj[node])):
                new_elem = adj[node][i]
                if visited[new_elem] == 0:
                    DFS_Topo(new_elem, adj, visited, s)
            s.append(node)
        
        
        visited = [0] * V
        s = deque()
        
        for i in range(V):
            if visited[i] == 0:
                DFS_Topo(i, adj, visited, s)
        
        ans = []
        
        while s:
            ans.append(s.pop())
        
        return ans
        


#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends