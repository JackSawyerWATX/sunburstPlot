import plotly.express as px
import pandas as pd

data = pd.DataFrame({
  "category" : ["Electronics", "Electronics", "Radios", "Radios"],
  "subcategory" : ["Phones", "Computers", "HAM", "Citizens Band"],
  "value" : [10, 20, 5, 15]
})

fig = px.sunburst(
  data,
  path=['category', 'subcategory'],
  values='value',
  title="Gadgets"
)

fig.show()