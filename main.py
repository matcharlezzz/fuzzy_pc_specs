from membership import TrapMF
from membership import TriMF


x = TrapMF(1, 8, 5, 7, 1)

tri_test = TriMF(50, 60, 80, 1)

while(True):
    val = input("Type number: ")
    print(tri_test.get_output(float(val)))