class SparseArray(object):

    def __init__(self,items=0):
        self.L=[0]*items
    def __setitem__(self, i, e):
        self.L[i] = e
    def __getitem__(self, item):
        return self.L[i]
    def __str__(self):
        return str(self.L)

jay=SparseArray(5)
jay[0]=(12,"Java")
jay[1]=(21,"Python")
jay[2]=(51,"C")
jay[3]=(76,"C++")
jay[4]=(108,"C#")

print("Sparse Array class: \n",jay)
