"""
    File: maze.py
    Author: Xin Li
    Purpose: In this project i will write a code to solve the
    mazes.
"""
class Maze:
    def __init__(self,edge_list):
        self._dic = self._build_maze(edge_list)

    def _build_maze(self, edge_list):
        dic = {}
        for i in edge_list:
            if i[0] not in dic:
                dic[i[0]] = [i[1]]
            else:
                dic[i[0]].append(i[1])
            if i[1] not in dic:
                dic[i[1]] = [i[0]]
            else:
                dic[i[1]].append(i[0])
        return dic
    def solve(self, src, dest):
        lst = []
        visited = []
        return self.helper(src, dest, visited, lst)


    def helper(self, src, dest, visited, lst):
        dic = self._dic
        if src not in dic:
            return None
        check = dic[src]
        if src == dest:
            return [src]
        visited.append(src)
        for k in check:
            if k not in visited:
                lst_1 = self.helper(k, dest, visited, lst)
                if lst_1 is not None:
                    return [src]+ lst_1
        return None
