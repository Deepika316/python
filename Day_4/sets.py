set1={1,2,3,4,5}
set2={'a','b','c'}
set1.add(6)
set2.add('d')
print("After adding  the element:",set1)
print("After adding  the element:",set2)
set1.remove(5)
set2.remove('b')
print("After removing the element:",set1)
print("After remove element:",set2)
set1.discard(5)
print("After Discarding the element:",set1)
set1.pop()
print("After pop the element:",set1)
set1.clear()
print("After clearing the element:",set1)
set3={2,4,6,8}
set4={1,2,5,3}
print("union operations:",set4.union(set3))
print("Intersection operations:",set3.intersection(set4))
print("Difference operation:",set3.difference(set4))
print("symmetric Difference:",set3.symmetric_difference(set4))