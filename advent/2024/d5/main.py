


from sys import stdin
from collections import deque

ans = 0
adj = [[] for _ in range(100)]

switch = False
for line in stdin:
    if line.strip() == "":
        switch = True
        continue

    if not switch:
        a, b = list(map(int, line.split("|")))
        adj[a].append(b)
    
    else:
        seq = list(map(int, line.split(',')))
        bad = False

        for i, start in enumerate(seq):
            visited = [False] * 100
            tovisit = deque([start])

            while tovisit:
                curr = tovisit.popleft()
                if visited[curr]:
                    continue

                visited[curr] = True
                for n in adj[curr]:
                    tovisit.append(n)
            
            for prev in seq[:i]:
                if visited[prev]:
                    bad = True
            
            print(visited)
            if bad:
                break
        
        if not bad:
            ans += seq[len(seq)//2]
                    




print(ans)