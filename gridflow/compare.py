from .solver import solve

def compare(data,methods=('newton','gauss_seidel','fast_decoupled')):
    records=[];reference=None
    for method in methods:
        try:
            r=solve(data,method);profile=[b['vm_pu'] for b in r['buses']]
            if reference is None and r['converged']:reference=profile
            records.append({'method':method,'converged':r['converged'],'reason':r['reason'],'iterations':r['iterations'],'elapsed_seconds':r['elapsed_seconds'],'max_mismatch_pu':r['max_mismatch_pu'],'max_voltage_difference_pu':max(abs(a-b) for a,b in zip(profile,reference)) if reference is not None and r['converged'] else None})
        except ValueError as exc:records.append({'method':method,'converged':False,'reason':str(exc)})
    return {'methods':records,'timing_note':'Single-run wall time, including model setup; not a statistically controlled benchmark.'}
