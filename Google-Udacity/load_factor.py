"""
1. Coworker comes with hash function that divides a group of values by 100,
and uses the remainder as key. The values are 100 numbers that are all multiples of 5
what is the load factor.
2. He thinks it's a little slow. What number would you recommend his function to divide by
rather than 100 to speed it up (87,107,125,1001)
"""
multip = []
hash_keys = []
len_mul = len(multip)
while len_mul < 100:
    for x in range(505):
        if x%5 == 0 and x!=0:
            multip.append(x)
            len_mul += 1
for num in multip:
    hash_keys.append(num%100)
key_buckets = {}
for key in hash_keys:
  key_buckets.update({key:hash_keys.count(key)})  
total_buckets = sum(key_buckets.values())
print("numbers:\n",multip)
print("hash keys:\n",hash_keys)
print("key buckets:\n",key_buckets)
print("total buckets:\n",total_buckets)
print("load factor:\n",len_mul//total_buckets)