import numpy as np
import matplotlib.pyplot as plt

C_m = 1.0
g_Na = 120.0
g_K = 36.0
g_L = 0.3
E_Na = 50.0
E_K = -77.0
E_L = -54.387

def alpha_m(V): return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))
def beta_m(V):  return 4.0 * np.exp(-(V + 65.0) / 18.0)
def alpha_h(V): return 0.07 * np.exp(-(V + 65.0) / 20.0)
def beta_h(V):  return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))
def alpha_n(V): return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))
def beta_n(V):  return 0.125 * np.exp(-(V + 65.0) / 80.0)

T = 50.0
dt = 0.01
t = np.arange(0, T, dt)

V = -65.0
m = alpha_m(V) / (alpha_m(V) + beta_m(V))
h = alpha_h(V) / (alpha_h(V) + beta_h(V))
n = alpha_n(V) / (alpha_n(V) + beta_n(V))

V_trace = []

print("Simulando disparo neuronal...")

for i in t:
    I_inj = 10.0 if 10.0 <= i <= 40.0 else 0.0
    
    I_Na = g_Na * (m**3) * h * (V - E_Na)
    I_K = g_K * (n**4) * (V - E_K)
    I_L = g_L * (V - E_L)
    
    dVdt = (I_inj - I_Na - I_K - I_L) / C_m
    V += dVdt * dt
    
    m += (alpha_m(V) * (1 - m) - beta_m(V) * m) * dt
    h += (alpha_h(V) * (1 - h) - beta_h(V) * h) * dt
    n += (alpha_n(V) * (1 - n) - beta_n(V) * n) * dt
    
    V_trace.append(V)

plt.figure(figsize=(10, 4))
plt.plot(t, V_trace, color='red')
plt.title('Potencial de Acción (Neurona Real)')
plt.xlabel('Tiempo (ms)')
plt.ylabel('Voltaje (mV)')
plt.grid(True)
plt.show()