# Student Starter File — Complete all TODOs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import animation
DATAFILE = r"'/Users/ubaidullah/Desktop/7Pharmacokinetics SimulatorTeamProjectQues/PK_sample.csv'"
def load_params(path):
    df = pd.read_csv(path)
   
    return df

# TODO load CSV containing Dose, Vd, k per patient
pass
def concentration_curve(dose, vd, k, t):
    df= ((df["Dose/Vd"]) * df["exp(-k*t)"])
        
    
    return df

# TODO return C(t) = (Dose/Vd) * exp(-k*t)
pass
'''def compute_metrics(df, t):
# TODO compute Cmax, Tmax, and AUC for each patient
pass
def create_plots(df):
# TODO concentration_curves.png
# TODO cmax_hist.png
# TODO dose_vs_cmax.png
# TODO auc_boxplot.png
pass
def make_animation(df, t):
# TODO animate the concentration curves over time
pass
def export_outputs(df):
# TODO export pk_summary.csv and patient_auc.csv'''