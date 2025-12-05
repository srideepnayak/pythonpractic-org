class A: 
  # Class A is a base class with no methods or attributes
  pass

class B(A): 
  # Class B inherits from A
  pass

class C(A): 
  # Class C also inherits from A
  pass

class D(B, C):
  # Class D inherits from both B and C
  pass
print(D.mro())