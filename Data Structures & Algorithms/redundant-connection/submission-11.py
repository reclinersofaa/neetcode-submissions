class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}
        for i in range(len(edges)): #initalize parent and rank maps
            parent[i + 1] = i + 1
            rank[i + 1] = 1
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) #directly assign the parent
            return parent[node]
        
        def union(n1, n2):
            if n1 == n2:
                return False #cycle condition
            
            if rank[n1] > rank[n2]: #this way, find proc can make minimum changes
                parent[n2] = n1
                rank[n1] += rank[n2]
            else:
                parent[n1] = n2
                rank[n2] += rank[n1]

            return True
        
        for e in edges:
            if not union(find(e[0]), find(e[1])):
                return e
        return False

