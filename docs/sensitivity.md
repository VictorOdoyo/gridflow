# Local injection sensitivities

The inverse reduced analytic Jacobian gives state change per unit injection. Dividing by base MVA returns radians/MW, pu/MW, radians/MVAr and pu/MVAr according to the row/column labels. Positive columns mean increased net generation, not load. The operating point is solved with reactive limits first and the final bus types are held fixed. The condition number warns about numerical sensitivity but is not a stability margin. These derivatives are local and do not predict discrete-control switching.
