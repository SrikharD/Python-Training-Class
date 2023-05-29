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

    def adding_edges(self,v1,v2):
        self.AdjMatrix[v1][v2] = 1
        self.AdjMatrix[v2][v1] = 1

    def deleting_edges(self,v1,v2):
        if self.AdjMatrix[v1][v2]:
            self.AdjMatrix[v1][v2] = self.AdjMatrix[v2][v1] = 0

    def Travese_Graph(self):
        for rows in self.AdjMatrix:
            for val in rows:
                print(self.AdjMatrix[val])
            
        
gg = graphs(4)
gg.adding_edges(1,2)
gg.adding_edges(1,1)
# gg.adding_edges(1,0)
# gg.adding_edges(3,2)
# gg.adding_edges(0,0)
gg.Travese_Graph()