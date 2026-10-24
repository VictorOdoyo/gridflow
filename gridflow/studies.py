from .solver import solve
from .sensitivity import sensitivity
from .continuation import continuation
from .compare import compare

def run(network,action='solve',options=None):
    actions={'solve':solve,'sensitivity':sensitivity,'continuation':continuation,'compare':compare}
    if action not in actions:raise ValueError('Unknown study action')
    if options is not None and not isinstance(options,dict):raise ValueError('Options must be an object')
    try:return actions[action](network,**(options or {}))
    except TypeError as exc:raise ValueError('Invalid study option: '+str(exc)) from exc
