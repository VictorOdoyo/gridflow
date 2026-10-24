# Analytic Newton derivatives

The Jacobian differentiates calculated P/Q with respect to the reduced angle/magnitude state. Diagonals use `dP/dtheta=-Q-Bii V²`, `dQ/dtheta=P-Gii V²`, `dP/dV=P/V+Gii V`, `dQ/dV=Q/V-Bii V`. Off-diagonal terms use the angle difference and branch admittance. A central-difference regression independently checks the complete reduced matrix. No finite differences are used in Newton iterations.
