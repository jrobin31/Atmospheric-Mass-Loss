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

# Equation 11
J_norm[r_norm, phi] = math.exp(-tau_norm[r_norm, phi])

# Equation 12 - might need to define this before equation 11
def eq_12_integrand(s):
    return a * n(t, np.sqrt(s**2 + r**2*np.sin(phi)**2))
tau_r_phi = scipy.integrate.quad(eq_12_integrand, a=r*np.cos(phi), b=np.inf, epsabs=0.001)

# Equation 13

# Equation 14

# Equation 15

# Equation 16
A = (eta * sigma_a * r_Q * J_XUV) / (2 * m * v_0**3)