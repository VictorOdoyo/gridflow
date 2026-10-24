from .solver import solve
from time import perf_counter

def compare(data,methods=('newton','gauss_seidel','fast_decoupled')):
    if not isinstance(methods,(list,tuple)) or not 1<=len(methods)<=4 or len(set(methods))!=len(methods) or any(m not in ['newton','gauss_seidel','fast_decoupled','dc'] for m in methods):
        raise ValueError('Methods must be a distinct list of 1..4 known solvers')
    records=[];reference=None
    for method in methods:
        try:
            started=perf_counter();r=solve(data,method);elapsed=perf_counter()-started;profile=[b['vm_pu'] for b in r['buses']]
            if reference is None and r['converged']:reference=profile
            records.append({'method':method,'converged':r['converged'],'reason':r.get('reason','linear_solve'),'iterations':r.get('iterations',0),'elapsed_seconds':elapsed,'max_mismatch_pu':r.get('max_mismatch_pu',0),'max_voltage_difference_pu':max(abs(a-b) for a,b in zip(profile,reference)) if reference is not None and r['converged'] else None})
        except ValueError as exc:records.append({'method':method,'converged':False,'reason':str(exc)})
    return {'methods':records,'timing_note':'Single-run wall time, including model setup; not a statistically controlled benchmark.'}
