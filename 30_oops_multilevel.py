class Dad:
    basketball = 1

class Son(Dad):
    dance_type = 1
    basketball = 5
    def is_dance(self):
        return f"Yes i can dance type {self.dance_type}"

class Grand_son(Son):
    dance_type = 5
    def is_dance(self):
        return f"Yes i can more dance type {self.dance_type}"

darry = Dad()
larry = Son()
harry = Grand_son()
print("Harry")
print(harry.is_dance())
print(harry.basketball)
print(harry.basketball)
print("larry")
print(larry.is_dance())
print(larry.basketball)
