"""
Apply Breadth First Search

Time: O(V+E) -> V = number of vertices, E = number of edges
Space: O(V)
"""
from collections import deque

graph = {
    "Luis": ["Nanci", "Kike", "Balta", "Mau", "Marco"],
    "Nanci": ["Norma", "Gaby"],
    "Kike": ["Lalo", "Tomas", "Norma"],
    "Balta": ["Norma", "Nanci", "Isabel"],
    "Mau": [],
    "Marco": [],
    "Lalo": [],
    "Tomas": [],
    "Norma": ["Nanci"],
    "Gaby": [],
    "Isabel": ["Balta"]
}

def bfs(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seller(person):
                print(person + " is seller")
                print(searched)
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def is_seller(name):
    return name == "Isabel"

bfs("Luis")