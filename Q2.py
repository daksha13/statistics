# b. Give the demonstration of bar graph and histogram using python programming.


# Q2.

'''
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot
#df = pd.read_csv('Book1.csv')

sb.histplot(df['Age'], kde=False)
plot.show()
'''

import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot
df = pd.read_csv('Book1.csv')
sb.barplot(df['Age'], kde =True)

plot.figure(figsize=(10, 5))
plot.title('Bar Graph')
plot.show()
