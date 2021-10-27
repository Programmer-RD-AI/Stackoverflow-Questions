import pandas as pd

text = """
X   y   pressure    time
0.5     0.5     0.5     0.5
0.5     0.5     0.5     0.5
0.5     0.5     0.5     0.5
0.5     0.5     0.5     0.5
0.5     0.5     0.5     0.5
"""
Xs = []
ys = []
pressures = []
times = []
for t in text.split("\n"):
    try:
        t = list(filter(None, t.strip().split(" ")))
        print(t)
        X = t[0]
        y = t[1]
        pressure = t[2]
        time = t[3]
        Xs.append(X)
        ys.append(y)
        pressures.append(pressure)
        times.append(time)
    except:
        pass
data = pd.DataFrame(
    {
        "X": Xs,
        "y": ys,
        "Pressure": pressures,
        "Times": times,
    }
)
data.to_csv("./data.csv", index=False)
