# The purpose of this file is to calculate the effects of radiative transfer in exoplanet atmospheres
import scipy
from scipy.integrate import quad
import numpy as np
import math


# Global parameters
P =
n_0 =
k =
T_0 =
T =
rho =
m =
v =
q =
r_0 =
r =
t =
G = 6.67e-11
M_pl =
phi =
eta =
sigma_a =
r_Q =
J_XUV =
n =
a = sigma_a * n_0 * r_0

# Normalize the variables
P_norm = P / (n_0 * k * T_0)
rho_norm = rho / (n_0 * m)
v_0 = np.sqrt((k * T_0) / m)
v_norm = v / v_0
T_norm = T / T_0
q_norm = (q * r_0) / (m * n_0 * v_0**3)
r_norm = r / r_0
t_norm =(t * v_0)/ r_0
beta = (G * m * M_pl) / (r_0 * k * T_0)

def J_norm(r):
    # Equation 12
    def eq_12_integrand(s):
        return a * n(t, np.sqrt(s**2 + r**2)) # Only calculate this at phi = pi/2
    tau_r_phi = scipy.integrate.quad(eq_12_integrand, a=0, b=np.inf, epsabs=0.001)
    return np.exp(-tau_r_phi)

# Equation 13
# def eq_13_integrand(r):
#     return A * n * np.exp(-tau_r_phi) * np.sin(phi)
# q_r = scipy.integrate.quad(eq_13_integrand, a=0, b=(np.pi / 2) + np.arccos(1 / r_norm), epsabs=0.001)

# Equation 15
def eq_15_integrand(s):
    return s * (1-J_norm(s))
r_2_ratio = 1 + 2 * scipy.integrate.quad(eq_15_integrand, a=1, b=np.inf, epsabs=0.001)

# Equation 14
total_energy_absorption = np.pi * J_XUV / (m * n_0 * v_0**3) * r_2_ratio

# Equation 16
# A = (eta * sigma_a * r_Q * J_XUV) / (2 * m * v_0**3)