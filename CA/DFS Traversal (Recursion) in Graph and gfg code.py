#User function Template for python3
def DFS(node, adj, ans, visited):
        visited[node] = 1
        ans.append(node)
            
        for i in range(len(adj[node])):
            new_elem = adj[node][i]
            if visited[new_elem] == 0: # i made a mistake here
                DFS(new_elem, adj, ans, visited)

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0] * V
        ans = []
        DFS(0, adj, ans, visited)
        return ans


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends