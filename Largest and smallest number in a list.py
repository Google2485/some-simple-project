a = [12, 45, 2, 41, 31, 10, 8, 6, 4]

# find largest and smallest values
l1 = max(a)
s1 = min(a)

# remove them from the list
a.remove(l1)
a.remove(s1)

# find second largest and second smallest
l2 = max(a)
s2 = min(a)

print(f"Largest: {l1}, Smallest: {s1}, Second Largest: {l2}, Second Smallest: {s2}")