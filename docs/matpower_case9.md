# External nine-bus reference

`benchmarks/case9.m` is the upstream MATPOWER nine-bus case. Its upstream license is preserved in `benchmarks/LICENSE-MATPOWER`. The native bundled `case9` example is the supported subset converted to GridFlow's schema. Source: [MATPOWER case9](https://github.com/MATPOWER/matpower/blob/master/data/case9.m).

The expected numerical solution was generated separately with [PYPOWER](https://github.com/rwl/PYPOWER), using a 1e-12 pu tolerance. The installed oracle version is recorded in the JSON fixture. Branch parameters, PV active powers, reactive bounds, bus voltage setpoints and demands were checked between the two inputs. The upstream initial slack active-power guess differs from PYPOWER's bundled case; that guess was aligned before solving, although the slack injection is an unknown in both formulations.

All three GridFlow AC methods are checked against the external solution for voltage magnitude, angle, and both-end branch powers. Observed maximum voltage differences during local verification were below 5e-11 pu for Gauss-Seidel and 8e-12 pu for FDXB; these are measurements from this small case, not general accuracy or speed guarantees. The regression tolerances are 1e-8 pu, 1e-6 degrees and 2e-6 MW/MVAr.

The fixture allows ordinary tests to run without PYPOWER or network access. Synthetic prescribed-voltage tests remain useful because they isolate electrical stamping and topology features that this one external network does not cover.
