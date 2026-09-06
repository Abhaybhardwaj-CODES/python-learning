import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)      # or original[:]  or list(original)
deep = copy.deepcopy(original)

original[0][0] = 999

print(shallow)  # [[999, 2], [3, 4]]  <- inner list is SHARED
print(deep)     # [[1, 2], [3, 4]]    <- inner list is independent