import plotly.express as px
import pandas as pd

data = pd.DataFrame({
  "category"    : ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"],
  "subcategory" : ["Communications", "Communications", "Communications", "Computing", "Computing"],
  "product"     : ["Phones", "HAM Radios", "Citizens Band Radios", "Computers", "Tablets"],
  "value"       : [10, 5, 15, 20, 12]
})

fig = px.sunburst(
  data,
  path=['category', 'subcategory', 'product'],
  values='value',
  title="Gadgets"
)

fig.show()