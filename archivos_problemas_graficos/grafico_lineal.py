import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\critico.csv")

#creando el grafico
sns.lineplot(x="fecha",y="critico",data=df)

#creando un punto en el momento mas critico
plt.plot("01-09",17,"o")

#mostrando el grafico
plt.show()