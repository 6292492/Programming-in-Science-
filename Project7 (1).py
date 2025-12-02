# Student Starter File — Complete all TODOs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation
DATAFILE = r"'/Users/ubaidullah/Desktop/7PharmacokineticsSimulatorTeamProjectQues/PK_sample.csv'"
def load_params(path):
    df = pd.read_csv(path)
   
    return df

# TODO load CSV containing Dose, Vd, k per patient
pass
def concentration_curve(dose, vd, k, t):
    df["C(t)"]=(
        (df["dose"])/df["vd"])*
    np.exp(-df["k"]*df["t"]
    )
    return df

# TODO return C(t) = (Dose/Vd) * exp(-k*t)
pass
def compute_metrics(df, t):

# TODO compute Cmax, Tmax, and AUC for each patient
pass
def create_plots(df):
# TODO concentration_curves.png ( title conctrtaion time curves and instead of site a b or c we have p1 p2 p3 for [atient id)
plt.figure(figsize=(8,4))
sns.lineplot(data=df, hue="PatientID")
plt.title("Concentration-time curves")
plt.close()

# TODO cmax_hist.png (cmax is x and count is y) title is cmax distribution




# TODO dose_vs_cmax.png ( dose is x and cmax is y, patient id instead of site id)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df,x="Dose",y="Cmax", hue="PatientID")
plt.title("\Dose vs Cmax")
plt.savefig(r"...) #copy path of the images later " \
plt.close()
# TODO auc_boxplot.png
plt.figure(figsize(7,5))
sns.boxplot(data=df,x="PatientID",y="AUC)
plt.title("\AUC Box plot")
plt.savefig(r"....) # same copy path of corresponding image
plt.close()
pass
def make_animation(df, t):
# TODO animate the concentration curves over time
pass
def export_outputs(df):
# TODO export pk_summary.csv and patient_auc.csv'''