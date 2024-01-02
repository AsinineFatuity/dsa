def max_pair_sum(arr, k):
    left, right = 0, k-1
    max_pair = arr[left:right+1]
    max_sum = sum(max_pair)

    while right < len(arr)-1:
        left += 1
        right += 1
        window = arr[left:right+1]
        window_sum = sum(window)
        if window_sum > max_sum:
            max_pair = window
            max_sum = window_sum

    return max_pair
