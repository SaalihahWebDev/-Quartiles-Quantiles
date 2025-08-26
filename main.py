import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic=sns.load_dataset("titanic")
survival_by_age=titanic.groupby("age")["survived"].mean().reset_index()
plt.figure(figsize=(10,6))
sns.lineplot(x="age",y="survived",data=survival_by_age,marker="o")

plt.title("Titanic Survival Rate by age",fontsize=14)
plt.xlabel("Age")
plt.ylabel("Survival Rate")
plt.grid(True)
plt.show()