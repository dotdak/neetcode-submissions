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
        return self._dfs(src, dst, set())
    def _dfs(self, src, dst, visited):
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        
        if dst in self.adj_list[src]:
            return True
        
        visited.add(src)

        for neighbor in self.adj_list[src]:
            if neighbor not in visited and self.hasPath(neighbor, dst):
                return True
        
        return False
            
    
