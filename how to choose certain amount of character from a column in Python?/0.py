import pandas as pd
data = pd.DataFrame({
  "ID":['13245993','3004992'],
  "A":['9','10']
})

print(data[data['ID'] == '13245993'])
