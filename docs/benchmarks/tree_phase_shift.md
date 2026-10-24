# Tree: phase shift

This independently specified circuit checks **phase shift** on a 8-bus tree topology with 7 branches. The fixture supplies input data plus full expected bus phasors and both-end branch powers. All three AC methods must recover the prescribed operating point from ordinary initial guesses.

Reference construction starts with known balanced phasors, computes ideal-transformer internal voltages, series currents and charging currents, then sets the nodal injections to those circuit results. It does not run a load-flow solver. Signed nodal demands can represent injection; these are mathematical verification circuits, not claimed utility measurements or IEEE standard networks.

Expected minimum voltage: **0.972000000 pu**. Expected branch active loss: **0.196042444 MW**. Bus count and topology deliberately vary to exercise indexing, parallel paths and sparse reference placement.

Run `python -m unittest tests.test_reference_tree_phase_shift`. The fixture is `benchmarks/tree_phase_shift.json`. Voltage tolerance is 2e-8 pu, angle tolerance 2e-6 degrees and branch-power tolerance 2e-5 MW/MVAr. These are numerical residual checks, not uncertainty bounds.
