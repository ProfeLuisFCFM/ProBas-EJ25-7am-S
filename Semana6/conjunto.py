conj1 = {1,2,3}
conj2 = set({3,4,5})

#print(type(conj1),type(conj2))

conj1.add(2)

print(conj1)

#print(conj1.union(conj2))

conj1.update(conj2)

print(conj1)