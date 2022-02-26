import pandas as pd

X = '                 X [m]'
Y = '                 Y [m]'
Z = '                 Z [m]'
Sig = '          σ_zz [kN/m²]'
U = '              |u| [m]'

settlement = pd.read_excel(r"dataset.xlsx", sheet_name="settlement")
sett_np = settlement[[X, Y, Z]].to_numpy()
u_np = settlement[U].to_numpy()

stress = pd.read_excel(r"dataset.xlsx", sheet_name="stress")
stress_np = stress[[X, Y, Z]].to_numpy()
sig_np = stress[Sig].to_numpy()

__all__ = (sett_np, stress_np, u_np, sig_np)
