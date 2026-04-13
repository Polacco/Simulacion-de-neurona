import numpy as np
import matplotlib.pyplot as plt

C_m = 1.0
g_Na, g_K, g_L = 120.0, 36.0, 0.3
E_Na, E_K, E_L = 50.0, -77.0, -54.387

g_syn_max = 0.5 
E_syn = 0.0  
tau_syn = 2.0

def alpha_m(V): return 0.1*(V+40.0)/(1.0-np.exp(-(V+40.0)/10.0))
def beta_m(V): return 4.0*np.exp(-(V+65.0)/18.0)
def alpha_h(V): return 0.07*np.exp(-(V+65.0)/20.0)
def beta_h(V): return 1.0/(1.0+np.exp(-(V+35.0)/10.0))
def alpha_n(V): return 0.01*(V+55.0)/(1.0-np.exp(-(V+55.0)/10.0))
def beta_n(V): return 0.125*np.exp(-(V+65.0)/80.0)

dt = 0.01
t = np.arange(0, 60, dt)

nA = [-65.0, 0.05, 0.6, 0.32]
nB = [-65.0, 0.05, 0.6, 0.32]
g_syn = 0.0 

traceA, traceB = [], []

print("Simulando comunicación inter-neuronal...")

for i in t:
    I_inj = 15.0 if 5.0 <= i <= 10.0 else 0.0
    
    vA, mA, hA, nA_prop = nA
    I_ionA = g_Na*mA**3*hA*(vA-E_Na) + g_K*nA_prop**4*(vA-E_K) + g_L*(vA-E_L)
    dvA = (I_inj - I_ionA) / C_m
    nA[0] += dvA * dt
    nA[1] += (alpha_m(vA)*(1-mA) - beta_m(vA)*mA) * dt
    nA[2] += (alpha_h(vA)*(1-hA) - beta_h(vA)*hA) * dt
    nA[3] += (alpha_n(vA)*(1-nA_prop) - beta_n(vA)*nA_prop) * dt

    if vA > 0:
        g_syn += g_syn_max * dt 
    g_syn -= (g_syn / tau_syn) * dt
    
    I_syn = g_syn * (nB[0] - E_syn)

    vB, mB, hB, nB_prop = nB
    I_ionB = g_Na*mB**3*hB*(vB-E_Na) + g_K*nB_prop**4*(vB-E_K) + g_L*(vB-E_L)
    dvB = (-I_syn - I_ionB) / C_m 
    nB[0] += dvB * dt
    nB[1] += (alpha_m(vB)*(1-mB) - beta_m(vB)*mB) * dt
    nB[2] += (alpha_h(vB)*(1-hB) - beta_h(vB)*hB) * dt
    nB[3] += (alpha_n(vB)*(1-nB_prop) - beta_n(vB)*nB_prop) * dt

    traceA.append(vA)
    traceB.append(vB)

plt.figure(figsize=(10, 5))
plt.plot(t, traceA, label='Neurona A (Habla)', alpha=0.8)
plt.plot(t, traceB, label='Neurona B (Escucha)', linestyle='--')
plt.title('Sinapsis: Transmisión de información entre dos neuronas')
plt.ylabel('Voltaje (mV)')
plt.legend()
plt.grid(True)
plt.show()