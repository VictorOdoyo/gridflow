"""JSON, explicit CSV tables, and MATPOWER numeric matrix interchange (no eval)."""
import csv
import io
import json
import re
from .model import validate

def read_json(text):return validate(json.loads(text))
def write_json(network):return json.dumps(validate(network),indent=2,allow_nan=False)

def csv_tables(network):
    n=validate(network);tables={}
    for key in ['buses','branches','loads','generators']:
        buffer=io.StringIO();fields=list(dict.fromkeys(k for row in n[key] for k in row))
        writer=csv.DictWriter(buffer,fieldnames=fields);writer.writeheader();writer.writerows(n[key]);tables[key]=buffer.getvalue()
    return {'base_mva':n['base_mva'],'tables':tables}

def from_csv_tables(base_mva,tables):
    network={'base_mva':base_mva};text_fields={'id','bus','kind','from','to'}
    for key in ['buses','branches','loads','generators']:
        rows=list(csv.DictReader(io.StringIO(tables.get(key,''))))
        for row in rows:
            for field,value in list(row.items()):
                if value=='':del row[field]
                elif field=='status':
                    if value.lower() not in ['true','false']:raise ValueError('CSV status must be true or false')
                    row[field]=value.lower()=='true'
                elif field not in text_fields:row[field]=float(value)
        network[key]=rows
    return validate(network)

def read_matpower(text):
    # Only literal matrices and baseMVA are recognized. MATLAB code is never executed.
    text=re.sub(r'%[^\n]*','',text)
    base=re.search(r'mpc\.baseMVA\s*=\s*([0-9.eE+\-]+)\s*;',text)
    if not base:raise ValueError('Missing literal mpc.baseMVA')
    matrices={}
    for key in ['bus','gen','branch']:
        match=re.search(r'mpc\.'+key+r'\s*=\s*\[([\s\S]*?)\]\s*;',text)
        if not match:raise ValueError('Missing literal matrix '+key)
        rows=[]
        for row in match.group(1).split(';'):
            if row.strip():
                try:rows.append([float(x) for x in row.replace(',',' ').split()])
                except ValueError as exc:raise ValueError('Only numeric MATPOWER matrix literals are supported') from exc
        matrices[key]=rows
    n={'base_mva':float(base.group(1)),'buses':[],'loads':[],'generators':[],'branches':[]}
    for row in matrices['bus']:
        if len(row)<13 or int(row[1]) not in [1,2,3]:raise ValueError('Unsupported MATPOWER bus row/type (isolated type 4 is not imported)')
        key=str(int(row[0]));n['buses'].append({'id':key,'kind':{1:'PQ',2:'PV',3:'Slack'}[int(row[1])],'vm':row[7],'va_deg':row[8],'base_kv':row[9],'gs_mw':row[4],'bs_mvar':row[5]})
        if row[2] or row[3]:n['loads'].append({'id':'load-'+key,'bus':key,'p_mw':row[2],'q_mvar':row[3]})
    for i,row in enumerate(matrices['gen']):
        if len(row)<10:raise ValueError('Incomplete generator row')
        n['generators'].append({'id':'gen-'+str(i+1),'bus':str(int(row[0])),'p_mw':row[1],'q_mvar':row[2],'qmax':row[3],'qmin':row[4],'status':bool(row[7])})
    for i,row in enumerate(matrices['branch']):
        if len(row)<13:raise ValueError('Incomplete branch row')
        n['branches'].append({'id':'branch-'+str(i+1),'from':str(int(row[0])),'to':str(int(row[1])),'r':row[2],'x':row[3],'b':row[4],'rate_mva':row[5],'tap':row[8] or 1.,'shift_deg':row[9],'status':bool(row[10])})
    return validate(n)

def write_matpower(network):
    n=validate(network);ids={b['id']:i+1 for i,b in enumerate(n['buses'])};blocks={k:[] for k in ['bus','gen','branch']}
    for b in n['buses']:
        loads=[d for d in n['loads'] if d['status'] and d['bus']==b['id']]
        blocks['bus'].append([ids[b['id']],{'PQ':1,'PV':2,'Slack':3}[b['kind']],sum(d['p_mw'] for d in loads),sum(d['q_mvar'] for d in loads),b['gs_mw'],b['bs_mvar'],1,b['vm'],b['va_deg'],b['base_kv'],1,1.1,.9])
    for gen in n['generators']:
        b=next(b for b in n['buses'] if b['id']==gen['bus'])
        blocks['gen'].append([ids[gen['bus']],gen['p_mw'],gen['q_mvar'],gen['qmax'],gen['qmin'],b['vm'],n['base_mva'],int(gen['status']),1e6,-1e6])
    for b in n['branches']:blocks['branch'].append([ids[b['from']],ids[b['to']],b['r'],b['x'],b['b'],b['rate_mva'],0,0,b['tap'],b['shift_deg'],int(b['status']),-360,360])
    text='function mpc = gridflow_case\nmpc.version = \'2\';\nmpc.baseMVA = '+str(n['base_mva'])+';\n'
    for key,rows in blocks.items():text+='mpc.'+key+' = [\n'+''.join('  '+' '.join(format(x,'.15g') for x in row)+';\n' for row in rows)+'];\n'
    return text
