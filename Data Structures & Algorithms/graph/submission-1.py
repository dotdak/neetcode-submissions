class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        self.adj_list.setdefault(src, []).append(dst)
        self.adj_list.setdefault(dst, [])

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list.setdefault(src, []).remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        
        if dst in self.adj_list[src]:
            return True

        for neighbor in self.adj_list[src]:
            if self.hasPath(neighbor, dst):
                return True
            
        return False

    
