# Gauss-Seidel

Sequential voltage updates use the latest available neighboring voltages. At PV buses, Q is recalculated from the current state before the voltage update and the specified magnitude is restored. Outer reactive-limit handling is shared with Newton. No acceleration factor is hidden. Convergence can be slow or fail on stressed/poorly conditioned systems; iteration history records the actual full AC mismatch.
