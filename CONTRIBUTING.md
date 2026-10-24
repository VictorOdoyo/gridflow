# Contributing

Use Python 3.11+ with NumPy. Run `python -m unittest discover -s tests -v` and `python -m compileall -q gridflow`. New electrical behavior needs explicit unit/sign conventions, domain validation, an independent analytic/reference case, and an engineering scope note. Avoid deriving expected values from the function under test. A reference-data change must explain the independent source of the new values.

Test GUI changes with a packaged network, an invalid model, a parameter edit, result invalidation, undo and export. Do not conflate layout coordinates with electrical lengths. Keep commits reviewable by separating implementation, independent verification and model documentation when useful. Never add empty commits, fictional authorship dates or arbitrary parameter fixtures solely to increase the commit count.
