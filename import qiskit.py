import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# PARAMETERS
screen_points = 200             # Number of positions on screen
num_photons = 5000              # Total number of simulated photons
fringe_multiplier = 6           # Controls number of interference fringes

# Generate phase shifts across screen
phi_vals = np.linspace(0, 2 * np.pi * fringe_multiplier, screen_points)

# Calculate quantum intensity (probability of hitting each screen position)
intensity = []
for phi in phi_vals:
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.p(phi, 0)
    qc.h(0)
    state = Statevector.from_instruction(qc)
    prob0 = state.probabilities_dict().get('0', 0)
    intensity.append(prob0)
prob_dist = np.array(intensity)
prob_dist /= np.sum(prob_dist)
hits_x = np.random.choice(screen_points, size=num_photons, p=prob_dist)
hits_y = np.random.uniform(0, 1, size=num_photons) * prob_dist[hits_x]
fig, ax = plt.subplots(figsize=(12, 6))
ax.scatter(hits_x, hits_y, s=2, alpha=0.4, color='navy', label='Photon Hits')
ax.plot(np.arange(screen_points), prob_dist / max(prob_dist), color='crimson', lw=2, label='Interference Pattern')
ax.set_title("Quantum Double-Slit: Photon Hits + Interference Graph")
ax.set_xlabel("Position on Screen")
ax.set_ylabel("Relative Intensity / Hit Height")
ax.set_ylim(0, 1.1)
ax.legend()
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()
