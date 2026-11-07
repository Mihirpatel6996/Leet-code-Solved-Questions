def longestSubarrayWithSumK(arr, K):
    """
    NOTES: Largest Subarray with Sum = K (Only POSITIVE Numbers)

    1. Ye Variable Size Sliding Window hai.
    2. Ye tabhi kaam karega jab saare numbers > 0 ho.
       Kyunki positive numbers me sum sirf badhta hai, kam nahi hota.

    LOGIC:
    l = left pointer, r = right pointer, curr_sum = window ka sum

    - r ko aage badha ke curr_sum me add karte jao
    - Agar curr_sum == K -> ye ek answer hai, maxLen update karo
    - Agar curr_sum > K -> iska matlab window bahut badi ho gayi, 
      isko left se chota karna padega.
    """

    l = 0
    curr_sum = 0
    maxLen = 0

    for r in range(len(arr)):
        # Step 1: Window ko expand karo
        curr_sum += arr[r]
        # Step 2: jab window sum is greater than given sum toh left se kam karte aana hai 
        while curr_sum > K and l <= r:
            curr_sum -= arr[l]
            l += 1
        
        # Step 3: Check karo kya sum K ke barabar hai
        if curr_sum == K:
            maxLen = max(maxLen, r - l + 1)

    return maxLen

# Example: arr = [1, 2, 1, 2, 1], K = 3 -> Answer = 2
