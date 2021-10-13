import pandas as pd

data = pd.DataFrame({"A":[1,2,3,4,5],"B":[1,2,3,4,5]})
A = pd.DataFrame(data["A"])
B = pd.DataFrame(data["B"])
print(A)
print(B)

"""
hi,

So you have a data frame.
And you want to split them into 2 data frames.
Is that the question you are asking?

if that's the question the solution is,

    import pandas as pd
    data = pd.DataFrame({"A":[1,2,3,4,5],"B":[1,2,3,4,5]})
    A = pd.DataFrame(data["A"])
    B = pd.DataFrame(data["B"])
    print(A)
    print(B)

Hope this helps if this is not your question please clarify more
"""
