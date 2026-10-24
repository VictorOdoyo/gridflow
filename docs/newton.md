# Damped Newton-Raphson

Each iteration solves `J dx = specified - calculated`, then backtracks until the infinity-norm mismatch decreases. PQ magnitudes below 0.03 pu or any magnitude above 3 pu are rejected. The returned diagnostic distinguishes convergence, iteration limit, singular Jacobian and stalled line search. A failed solution remains a failed study; it is never silently relabeled as converged or replaced by another algorithm. Dense NumPy linear algebra is intended for small/medium educational studies, not large transmission production planning.
