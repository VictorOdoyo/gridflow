# Ring: bus shunts

This independently specified circuit checks **bus shunts** on a 4-bus ring topology with 4 branches. The fixture supplies input data plus full expected bus phasors and both-end branch powers. All three AC methods must recover the prescribed operating point from ordinary initial guesses.

Reference construction starts with known balanced phasors, computes ideal-transformer internal voltages, series currents and charging currents, then sets the nodal injections to those circuit results. It does not run a load-flow solver. Signed nodal demands can represent injection; these are mathematical verification circuits, not claimed utility measurements or IEEE standard networks.

Expected minimum voltage: **0.988000000 pu**. Expected branch active loss: **0.091030574 MW**. Bus count and topology deliberately vary to exercise indexing, parallel paths and sparse reference placement.

Run `python -m unittest tests.test_reference_ring_bus_shunts`. The fixture is `benchmarks/ring_bus_shunts.json`. Voltage tolerance is 2e-8 pu, angle tolerance 2e-6 degrees and branch-power tolerance 2e-5 MW/MVAr. These are numerical residual checks, not uncertainty bounds.
