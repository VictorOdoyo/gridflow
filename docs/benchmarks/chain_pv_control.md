# Chain: pv control

This independently specified circuit checks **pv control** on a 3-bus chain topology with 2 branches. The fixture supplies input data plus full expected bus phasors and both-end branch powers. All three AC methods must recover the prescribed operating point from ordinary initial guesses.

Reference construction starts with known balanced phasors, computes ideal-transformer internal voltages, series currents and charging currents, then sets the nodal injections to those circuit results. It does not run a load-flow solver. Signed nodal demands can represent injection; these are mathematical verification circuits, not claimed utility measurements or IEEE standard networks.

Expected minimum voltage: **0.992000000 pu**. Expected branch active loss: **0.029364547 MW**. Bus count and topology deliberately vary to exercise indexing, parallel paths and sparse reference placement.

Run `python -m unittest tests.test_reference_chain_pv_control`. The fixture is `benchmarks/chain_pv_control.json`. Voltage tolerance is 2e-8 pu, angle tolerance 2e-6 degrees and branch-power tolerance 2e-5 MW/MVAr. These are numerical residual checks, not uncertainty bounds.
