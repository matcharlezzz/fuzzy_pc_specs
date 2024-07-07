from membership import TrapMF
from membership import TriMF
from membership import PCSpecsMembership


pc = PCSpecsMembership()


val = input("Type number for Budget: ")
print(pc.budget(float(val)))
val = input("Type number for Workload: ")
print(pc.workload(float(val)))
val = input("Type number for Storage: ")
print(pc.storage(float(val)))