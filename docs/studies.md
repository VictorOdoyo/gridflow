# Study dispatch

`gridflow.studies.run(network, action, options)` dispatches solve, sensitivity, continuation or compare. Solve accepts method, tolerance, max_iterations and enforce_q_limits. Continuation accepts steps, step_size and tolerance. Comparison accepts a list of methods. Each routine copies/validates its inputs. Invalid options and actions raise ValueError. Study outputs are JSON-compatible; they retain their numerical diagnostics and applicability assumptions.
