#Matrix Creation
#Insert 
#Delete
#Size



class graphs:
    def __init__(self,size:int,weight=None) -> None:
        self.weight = weight
        self.AdjMatrix = []
        for i in range(size):
            self.AdjMatrix.append([0 for i in range(size)])
        self.size = size
        # print(self.AdjMatrix)

    def adding_edges(self,v1,v2):
        self.AdjMatrix[v1][v2] = 1
        self.AdjMatrix[v2][v1] = 1

    def deleting_edges(self,v1,v2):
        if self.AdjMatrix[v1][v2]:
            self.AdjMatrix[v1][v2] = self.AdjMatrix[v2][v1] = 0

    def Travese_Graph(self):
        for row in self.AdjMatrix:
            for val in row:
                print(val, end='')
            print()
            
    def dfs(self, v, discovered, parent=-1):
        discovered[v] = True

        for w in range(len(self.adj_matrix[v])):
            if self.adj_matrix[v][w]:
                if discovered[w]:
                    if w != parent:
                        return True
                else:
                    if self.dfs(w, discovered, v):
                        return True
        return False



gg = graphs(4)
gg.adding_edges(1,2)
gg.adding_edges(1,1)
gg.adding_edges(1,0)
gg.adding_edges(3,2)
gg.adding_edges(0,0)
gg.deleting_edges(0,0)
gg.Travese_Graph()
