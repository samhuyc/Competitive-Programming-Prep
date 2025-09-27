t = int(input())


for _ in range(t):
    n, m = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    max_a = max(a_list)
    if max_a > b_list[0]:
        print(-1)
        continue  # Impossible to process max_a with any b_k

    k = 1  # Initial k
    total_cost = 0
    sum_a = 0
    i = 0
    while i < n:
        # Check if we can process the current element at a higher k
        can_increase_k = False
        for nk in range(k + 1, m + 1):
            if a_list[i] <= b_list[nk - 1]:
                can_increase_k = True
                break
        if can_increase_k:
            # Process accumulated sum at current k
            if sum_a > 0:
                total_cost += (m - k)
                sum_a = 0
            k = nk  # Increase k
        if a_list[i] > b_list[k - 1]:
            # Cannot process this element at current or any higher k
            total_cost = -1
            break
        sum_a += a_list[i]
        if sum_a > b_list[k - 1]:
            # Need to perform a Type 2 operation
            total_cost += (m - k)
            sum_a = a_list[i]
        i += 1
    else:
        if total_cost != -1 and sum_a > 0:
            total_cost += (m - k)
        print(total_cost if total_cost != -1 else -1)