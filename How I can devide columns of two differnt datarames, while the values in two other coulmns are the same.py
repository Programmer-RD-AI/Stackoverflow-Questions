import pandas as pd

data = pd.DataFrame({"A":[1,2,3,4,5],"B":[1,2,3,4,5]})
A = pd.DataFrame(data["A"])
B = pd.DataFrame(data["B"])
print(A)
print(B)
