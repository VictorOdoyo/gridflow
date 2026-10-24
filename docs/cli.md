# Command line interface

`python -m gridflow examples` lists packaged native network cases. `python -m gridflow study example:triangle` solves one. A local JSON path or `-` for stdin can replace the example reference. `--action` selects a study and `--options` accepts a JSON options object. `--output` saves a full-precision result file. Use shell-appropriate quoting for JSON or call the Python API. `python -m gridflow serve --port 8766` starts the loopback workbench.

Exit 0 indicates a successful command, 1 an explicitly nonconverged top-level solve, and 2 invalid input or an I/O/numerical exception. Nested studies retain per-sample/per-method success flags; inspect those flags rather than assuming every nested result converged from process exit alone.
