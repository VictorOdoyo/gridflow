# Reduced AC state

Calculated complex injection is `S=V conj(YV)`. The mismatch stacks specified minus calculated P at every non-slack bus followed by Q at PQ buses only. Unknowns stack non-slack angles in radians then PQ voltage magnitudes. Slack phasors and PV magnitudes remain fixed. The convergence metric is the infinity norm of this reduced mismatch in per unit. It does not include unspecified slack injection or PV Q.
