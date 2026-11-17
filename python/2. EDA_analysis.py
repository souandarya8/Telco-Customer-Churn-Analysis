import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("../data/processed/cleaned_telco.csv")

# overall churn percentage %
# how  many customers leave
churn_counts=df["churn"].value_counts()
print("Churn counts:")
print(churn_counts)
print("\nchurn percentage:")
for category,count in churn_counts.items():
    percentage=count/len(df)*100
    print(f"{category}: {percentage:.2f}%")

# Churn analysis by contract type
contract_churn=pd.crosstab(df["contract"],df["churn"],normalize="index")*100
print("\nContract churn percentage:")
print("\n",contract_churn.round(2))

# how  many customers leave based on contract?
print("="*80)
contract_churn.plot(kind="bar",figsize=(8,5),stacked=True)
plt.gcf().set_facecolor("powderblue")
plt.gca().set_facecolor("grey")
plt.title("Customer churn by Contract type-",fontweight="bold")
plt.xlabel("Contract type",fontweight="bold")
plt.ylabel("Percentage of customers churn",fontweight="bold")
plt.legend(title="Churn")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Churn by Tenure
avg_tenure=df.groupby("churn")["tenure"].mean()
print("\nAverage tenure Churns by status:")
print("\n",avg_tenure.round(2))
print("="*80)

# Bar chart for Churn by Tenure
#Do churned customers have shorter tenure on average?
avg_tenure.plot(kind="bar",figsize=(8,5),stacked=True)
plt.gcf().set_facecolor("powderblue")
plt.gca().set_facecolor("grey")
plt.title("Average Customer tenure Churns by status",fontweight="bold")
plt.xlabel("Churn status",fontweight="bold")
plt.ylabel("average Tenure (Months)",fontweight="bold")
plt.legend(title="Churn")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Average Monthly Charges by Churn Status
#Do churned customers pay more on average?
plt.figure(figsize=(8,5))
sns.barplot(data=df,x="churn",y="monthlycharges",hue="churn",palette="Set3")
plt.gcf().set_facecolor("powderblue")
plt.gcf().set_facecolor("powderblue")
plt.gca().set_facecolor("grey")
plt.title("Monthly Charges by status",fontweight="bold")
plt.xlabel("Churn status",fontweight="bold")
plt.ylabel("Monthly Charges",fontweight="bold")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#hist
#How are customer charges distributed?
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="churn",y="monthlycharges",color="mediumpurple",errorbar=None)
plt.gcf().set_facecolor("powderblue")
plt.gca().set_facecolor("white")
plt.title("Average Monthly Charges by churn status",fontweight="bold")
plt.xlabel("churn status",fontweight="bold")
plt.ylabel("Average Monthly charges ",fontweight="bold")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Churn by Internet Service
#Does churn rate differ by internet service?
rate=pd.crosstab(df["internetservice"],df["churn"],normalize="index")*100
print("\nChurn rate by Internet service:")
print("\n",rate.round(2))
print("="*80)

ax=rate.plot(kind="bar",figsize=(8,5),stacked=True)
plt.gcf().set_facecolor("powderblue")
plt.gcf().set_facecolor("grey")
plt.title("Internet Service Charges by status",fontweight="bold")
plt.xlabel("Churn status",fontweight="bold")
plt.ylabel("Percentage of customers churn",fontweight="bold")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
