import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# we need to get a data file with all the vraible like t, dose, etc to be bal eto read them and cretae the gprahs this is what i did so far.

df = pd.read_csv(r"/Users/ubaidullah/Desktop/7Pharmacokinetics SimulatorTeamProjectQues/pk_summary.csv")
def create_plots(df):

   ''' # 1. Concentration-time curves
    plt.figure(figsize=(8,4))
    sns.lineplot(data=df, x="Time", y="Concentration", hue="PatientID")
    plt.title("Concentration-Time Curves")
    plt.savefig(r"C:/Users/ubaidullah/Downloads/7Pharmacokinetics SimulatorTeamProjectQues/concentration_curves.png")
    plt.close()'''

    # 2. Cmax histogram
plt.figure(figsize=(8,4))
sns.histplot(
        data=df,
        x="Cmax",
        kde=True,
        stat="count",
        bins=5,
        alpha=0.4
    )
plt.xlabel("Cmax")
plt.ylabel("Count")
plt.title("Cmax Distribution")
plt.savefig(r"C:/Users/ubaidullah/Downloads/7Pharmacokinetics SimulatorTeamProjectQues/cmax_hist.png")
plt.close()

'''    # 3. Dose vs Cmax
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x="Dose", y="Cmax", hue="PatientID")
plt.title("Dose vs Cmax")
plt.savefig(r"C:/Users/ubaidullah/Downloads/7Pharmacokinetics SimulatorTeamProjectQues/dose_vs_cmax.png") 
plt.close()'''

    # 4. AUC boxplot
plt.figure(figsize=(7,5))
sns.boxplot(data=df, x="PatientID", y="AUC")
plt.title("AUC Box Plot")
plt.savefig(r"C:/Users/ubaidullah/Downloads/7Pharmacokinetics SimulatorTeamProjectQues/auc_boxplot.png")
plt.close()

create_plots(df)
