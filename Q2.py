# Demonstration of bar graph and histogram using python programming.

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot
df = pd.read_csv('Book1.csv')
sb.barplot(df['Age'], kde =True)

plot.figure(figsize=(10, 5))
plot.title('Bar Graph')
plot.show()
