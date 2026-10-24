# Interchange boundaries

Native JSON preserves string IDs, explicit loads/generators and all supported model properties. CSV export consists of four named tables plus base MVA; `from_csv_tables` reverses it. Booleans are true/false and blank optional cells restore defaults. CSV is not a free-form spreadsheet parser.

MATPOWER import reads literal `mpc.baseMVA`, `mpc.bus`, `mpc.gen` and `mpc.branch` matrices. It never executes MATLAB or expressions. It supports bus types 1/2/3 and the standard columns through branch ANGMAX. Isolated type-4 buses, ZIP loads, generator costs/capability curves, DC lines and procedural case construction are not supported. Export renumbers string bus IDs from one, aggregates online demand and writes only the supported subset. Equipment IDs do not survive that conversion. Bus VM provides controlled-voltage setpoints; generator VG is not independently enforced. MATPOWER is a reference format, not a claim of full MATPOWER feature parity.
