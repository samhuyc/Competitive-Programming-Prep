

from collections import deque

t = int(input())



for _ in range(t):
    n, k, q = list(map(int, input().split()))
    lst = list(map(int, input().split()))


    buckets = []
    ans = []


    first = lst[:k-1]
    for i, v in enumerate(first):

        maxlen = 1
        stop = False
        keep = deque()
        for j, b in enumerate(buckets):
            if b[0][1] + k <= i:
                b.popleft()
            if len(b) == 0:
                continue
            else:
                keep.append(j)

            if not stop and b[-1][0] == v-1:
                b.append([v, i])
                stop = True
            maxlen = max(maxlen, len(b))
        
        newbuckets = [buckets[j] for j in keep]
        newbuckets.sort(key=lambda x:-len(x))
        buckets = newbuckets
        if not stop:
            buckets.append(deque([[v, i]]))
        
    
    for i in range(k-1, n):
        v = lst[i]
        maxlen = 1
        stop = False
        keep = deque()
        for j, b in enumerate(buckets):
            if b[0][1] + k <= i:
                b.popleft()
            if len(b) == 0:
                continue
            else:
                keep.append(j)

            if not stop and b[-1][0] == v-1:
                b.append([v, i])
                stop = True
            maxlen = max(maxlen, len(b))
        
        newbuckets = [buckets[j] for j in keep]
        newbuckets.sort(key=lambda x:-len(x))
        buckets = newbuckets
        if not stop:
            buckets.append(deque([[v, i]]))
        
        ans.append(maxlen)
    
    # print(ans)


    for _ in range(q):
        l, _  = list(map(int, input().split()))
        print(k-ans[l-1])
