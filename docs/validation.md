# Independent numerical validation

The 56 synthetic studies systematically combine electrical conditions and network structure. Each fixture commit introduces a distinct circuit/model case; a following regression commit verifies it; an engineering note records its purpose and tolerances. No empty commits or historical-date manipulation are used.

Eight graph families cross seven electrical conditions: high resistance, line charging, tap ratio, phase shift, bus shunts, PV control and reverse flow. Prescribed phasors define a known operating point. An independent series-current and ideal-transformer circuit calculation derives net bus injections and both-end branch powers. Flat non-slack angle/magnitude initial guesses must recover the point with Newton, Gauss-Seidel and FDXB.

The checked-in generator is `tools/reference_cases.py`. It depends on NumPy and standard-library math only. Normal tests consume fixed expected values and never regenerate them. The reference code intentionally does not import gridflow. If changing equations, review the implementation and reference formulation independently instead of updating expected outputs to match a failed test.

Analytical invariant tests cover Y-bus stamps, finite-difference Jacobian agreement, DC branch flow, power losses and PV reactive clamping. CLI and HTTP tests exercise packaging and application boundaries. Cross-method agreement alone is not the validation oracle. No laboratory, certified utility design package or full IEEE standardized feeder validation is claimed by this suite.
