class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. 그래프화
        graph = collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        # 2. 방문 여부를 확인 하고, 가지치기를 위한 각각의 set 
        traced, visited = set(),set()

        def dfs(i):
            if i in traced:
                return False 
            if i in visited:
                return True 

            # 3. 접점을 처음 도달 했을 떼(이웃도 아님)
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False 
            # 4. 탐색 종료 후 순환 노드 삭제 
            traced.remove(i)
            # 5. 탐색 종료 후 방문 노드 추가(가지치기)
            visited.add(i)

            return True 

        for x in list(graph):
            if not dfs(x):
                return False 

        return True 
