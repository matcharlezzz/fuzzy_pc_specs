from membership import TrapMF
from membership import TriMF
from membership import PCSpecsMembership


pc = PCSpecsMembership()


val = input("Type number for Budget: ")
print(pc.budget(val))
val = input("Type number for Workload: ")
print(pc.workload(input))
val = input("Type number for Storage: ")
print(pc.storage(input))