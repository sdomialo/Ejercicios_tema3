def bucket_sort(arr):
    # Find the maximum value in the array
    max_value = max(arr)
    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]
    # Assign elements to buckets
    for num in arr:
        index = int(num * len(arr) / (max_value + 1))
        buckets[index].append(num)
    # Sort each bucket
    for bucket in buckets:
        bucket.sort()
    # Concatenate the sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)
    return sorted_arr

# Test the bucket sort algorithm
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print(sorted_arr)