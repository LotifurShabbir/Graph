from queue import Queue
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        InDeg = [0] * V
        ans = []
        
        # find indegree of the graph
        for i in range(V):
            for j in range(len(adj[i])):
                InDeg[adj[i][j]] += 1
        # put node whose in degree is 0
        
        q = Queue()
        
        for i in range(V):
            if InDeg[i] == 0:
                q.put(i)
        
        while q.empty() != True:
            node = q.get()
            ans.append(node)
            
            # node er neighbours er indegree 1 komai dite hobe
            for i in range(len(adj[node])):
                new_elem = adj[node][i]
                InDeg[new_elem] -= 1
                if InDeg[new_elem] == 0:
                    q.put(new_elem)
                
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