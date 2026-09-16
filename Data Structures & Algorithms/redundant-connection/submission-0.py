class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        parent = [i+1 for i in range(len(edges))]
        #joining two sets, smth like parent[find(A)] = find(B)
        def Uni(A, B):
            ra, rb = find(A), find(B)
            if ra == rb:
                return False
            parent[ra - 1] = rb
            return True

        #find parent of a set A
        def find(a):
            x = a
            while parent[x-1] != x:
                x = parent[x-1]
            return x

        for e in edges:
                a, b = e
                if not Uni(a, b):
                    return e
            
            
