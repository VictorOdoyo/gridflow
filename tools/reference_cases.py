import json, math, cmath, argparse
import numpy as np

def gf_reference(shape,variant):
    layouts={
        'two_bus':(2,[(0,1)]),'chain':(3,[(0,1),(1,2)]),'triangle':(3,[(0,1),(1,2),(2,0)]),
        'ring':(4,[(0,1),(1,2),(2,3),(3,0)]),'star':(5,[(0,i) for i in range(1,5)]),
        'mesh':(6,[(0,1),(1,2),(2,3),(3,4),(4,5),(5,0),(1,4),(2,5)]),
        'ladder':(7,[(0,1),(1,2),(2,3),(0,4),(4,5),(5,6),(1,5),(2,6)]),
        'tree':(8,[(0,1),(1,2),(1,3),(0,4),(4,5),(4,6),(6,7)])}
    size,edges=layouts[shape];n={'schema_version':1,'name':shape+' / '+variant,'base_mva':100,'buses':[],'branches':[],'loads':[],'generators':[]}
    v=np.array([(1.02 if i==0 else 1-.004*i)*cmath.exp(-1j*.015*i) for i in range(size)])
    if variant=='reverse_flow':v=np.array([(1.02 if i==0 else 1.02+.001*i)*cmath.exp(1j*.008*i) for i in range(size)])
    for i in range(size):n['buses'].append({'id':str(i+1),'kind':'Slack' if i==0 else 'PV' if variant=='pv_control' and i==1 else 'PQ','vm':float(abs(v[i])) if i==0 or (variant=='pv_control' and i==1) else 1.,'va_deg':0.,'base_kv':110,'gs_mw':.2*i if variant=='bus_shunts' else 0.,'bs_mvar':.4*i if variant=='bus_shunts' else 0.})
    injection=np.zeros(size,complex);flows=[]
    for k,(i,j) in enumerate(edges):
        r=.018+.002*(k%3) if variant=='resistive' else .004+.001*(k%3);x=.12+.01*(k%4);b=.025 if variant=='charging' else 0;tap=1.025 if variant=='tap_ratio' and k==0 else 1.;angle=2. if variant=='phase_shift' and k==0 else 0.
        branch={'id':'line-'+str(k+1),'from':str(i+1),'to':str(j+1),'r':r,'x':x,'b':b,'tap':tap,'shift_deg':angle,'rate_mva':150};n['branches'].append(branch)
        # Independent circuit calculation using the ideal-transformer internal voltage.
        t=cmath.rect(tap,math.radians(angle));internal=v[i]/t;series=(internal-v[j])/complex(r,x)
        from_current=(series+1j*b/2*internal)/t.conjugate();to_current=-series+1j*b/2*v[j]
        sf=v[i]*from_current.conjugate()*100;st=v[j]*to_current.conjugate()*100;injection[i]+=sf;injection[j]+=st
        flows.append({'id':branch['id'],'p_from_mw':sf.real,'q_from_mvar':sf.imag,'p_to_mw':st.real,'q_to_mvar':st.imag})
    for i,bus in enumerate(n['buses']):
        injection[i]+=abs(v[i])**2*complex(bus['gs_mw'],-bus['bs_mvar'])
        if bus['kind'] in ['Slack','PV']:n['generators'].append({'id':'gen-'+str(i+1),'bus':str(i+1),'p_mw':float(injection[i].real),'q_mvar':float(injection[i].imag),'qmin':-1000,'qmax':1000})
        else:n['loads'].append({'id':'load-'+str(i+1),'bus':str(i+1),'p_mw':float(-injection[i].real),'q_mvar':float(-injection[i].imag)})
    expected={'vm_pu':np.abs(v).tolist(),'va_deg':np.angle(v,deg=True).tolist(),'branches':flows,'losses_mw':sum(x['p_from_mw']+x['p_to_mw'] for x in flows)}
    return n,expected

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Independent reference circuit generator, no production imports')
    parser.add_argument('--group',required=True)
    parser.add_argument('--variant',required=True)
    args=parser.parse_args()
    network,expected=gf_reference(args.group,args.variant)
    print(json.dumps({'network':network,'expected':expected},indent=2,allow_nan=False))
