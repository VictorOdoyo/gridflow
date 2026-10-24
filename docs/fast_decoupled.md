# Fast decoupled FDXB

B-prime is negative imaginary Y built with r=0, charging=0, bus shunts=0 and tap magnitudes=1. Phase shifts remain. B-double-prime retains resistance, charging, taps and shunts but sets phase shifts to zero. The updates solve scaled P and Q mismatches sequentially, while convergence always uses the full AC equations. This is the XB variant, not Newton with a mislabeled Jacobian. High R/X distribution circuits and severe stress may not converge. Zero-reactance branches are rejected for this method.
