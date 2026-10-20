#!/usr/bin/env python3
"""Independent semantic regression checks; NOT a natural-deduction verifier.

Standard library only. Enumerates all TFL valuations for registered claims;
checks specified FOL models and bounded interpretations. Does not establish FOL
validity by bounded search, translation fidelity, or correctness of proof lines.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
COURSE = HERE.parent
ROOT = COURSE.parent.parent
COUNT = {'tfl_claims': 0, 'tfl_valuations': 0, 'fol_model_assertions': 0,
         'fol_bounded_claims': 0, 'fol_bounded_interpretations': 0,
         'local_links': 0}

class Parser:
    def __init__(self, text):
        self.ts = re.findall(r'[A-Z][0-9]*|[a-z][0-9]*|[¬∧∨→↔∀∃=(),⊥]', text)
        residue = re.sub(r'[A-Z][0-9]*|[a-z][0-9]*|[¬∧∨→↔∀∃=(),⊥]|\s', '', text)
        assert not residue, (text, residue)
        self.i = 0
    def take(self, token=None):
        value = self.ts[self.i]
        assert token is None or value == token, (self.ts, self.i, token)
        self.i += 1
        return value
    def peek(self):
        return self.ts[self.i] if self.i < len(self.ts) else None
    def unary(self):
        t = self.take()
        if t == '¬': return ('¬', self.unary())
        if t in ('∀', '∃'): return (t, self.take(), self.unary())
        if t == '(':
            a = self.expr()
            self.take(')')
            return a
        if t == '⊥': return ('⊥',)
        if t[0].islower():
            self.take('=')
            return ('=', t, self.take())
        if self.peek() == '(':
            self.take('(')
            args = [self.take()]
            while self.peek() == ',':
                self.take(','); args.append(self.take())
            self.take(')')
            return ('pred', t, tuple(args))
        return ('atom', t)
    def expr(self, minimum=0):
        left = self.unary()
        precedence = {'↔': 1, '→': 2, '∨': 3, '∧': 4}
        while self.peek() in precedence and precedence[self.peek()] >= minimum:
            op = self.take(); p = precedence[op]
            right = self.expr(p if op == '→' else p+1)
            left = (op, left, right)
        return left
    def parse(self):
        a = self.expr()
        assert self.i == len(self.ts), self.ts[self.i:]
        return a

def parse(s): return Parser(s).parse()
def truth(a, model, env=None):
    env = {} if env is None else env
    op = a[0]
    def term(t): return env[t] if t in env else model['names'][t]
    if op == 'atom': return model['atoms'][a[1]]
    if op == 'pred': return tuple(term(t) for t in a[2]) in model['preds'][a[1]]
    if op == '=': return term(a[1]) == term(a[2])
    if op == '⊥': return False
    if op == '¬': return not truth(a[1], model, env)
    if op in ('∀', '∃'):
        vals = [truth(a[2], model, dict(env, **{a[1]: d})) for d in model['domain']]
        return all(vals) if op == '∀' else any(vals)
    l, r = truth(a[1], model, env), truth(a[2], model, env)
    return {'∧': l and r, '∨': l or r, '→': (not l) or r, '↔': l == r}[op]

def symbols(a, bound=frozenset()):
    op = a[0]
    if op == 'atom': return {a[1]}, {}, set()
    if op == 'pred': return set(), {a[1]:len(a[2])}, set(a[2])-bound
    if op == '=': return set(), {}, set(a[1:])-bound
    if op == '⊥': return set(), {}, set()
    if op in ('∀','∃'): return symbols(a[2], bound|{a[1]})
    if op == '¬': return symbols(a[1],bound)
    x,y = symbols(a[1],bound),symbols(a[2],bound)
    for k in x[1].keys() & y[1].keys(): assert x[1][k] == y[1][k]
    return x[0]|y[0], x[1]|y[1], x[2]|y[2]

def valuations(forms):
    atoms=set()
    for f in forms:
        ats,preds,names=symbols(f)
        assert not preds and not names
        atoms |= ats
    atoms=sorted(atoms)
    for vals in product([False,True],repeat=len(atoms)):
        yield {'atoms':dict(zip(atoms,vals)), 'names':{},'preds':{},'domain':(0,)}

def entail(label, premises, conclusion, expected=True):
    fs=[parse(s) for s in premises]; c=parse(conclusion)
    cases=list(valuations(fs+[c])); COUNT['tfl_claims']+=1
    COUNT['tfl_valuations']+=len(cases)
    bad=[m for m in cases if all(truth(f,m) for f in fs) and not truth(c,m)]
    assert (not bad)==expected,(label,bad)

def equiv(label,a,b,expected=True): entail(label,[],f'({a})↔({b})',expected)
def sat(label,forms,expected):
    fs=[parse(s) for s in forms]; cases=list(valuations(fs))
    COUNT['tfl_claims']+=1; COUNT['tfl_valuations']+=len(cases)
    assert any(all(truth(f,m) for f in fs) for m in cases)==expected,label

def model(n=2, names=None, **preds):
    return {'domain':tuple(range(n)),'names':names or {},'preds':
        {k:{(v,) if isinstance(v,int) else tuple(v) for v in vs} for k,vs in preds.items()},'atoms':{}}
def check(label,m,claims):
    for formula,expected in claims:
        COUNT['fol_model_assertions']+=1
        actual=truth(parse(formula),m)
        assert actual==expected,(label,formula,actual,expected)

def bounded(label,premises,conclusion,max_n=2):
    fs=[parse(s) for s in premises]; c=parse(conclusion)
    preds={}; names=set()
    for f in fs+[c]:
        ats, ps, ns=symbols(f); assert not ats; preds.update(ps); names |= ns
    COUNT['fol_bounded_claims']+=1
    for n in range(1,max_n+1):
        domain=tuple(range(n)); pkeys=sorted(preds); nkeys=sorted(names)
        extensions=[]
        for key in pkeys:
            tuples=list(product(domain,repeat=preds[key]))
            extensions.append([{t for t,bit in zip(tuples,bits) if bit}
                for bits in product([False,True],repeat=len(tuples))])
        for exts in product(*extensions):
            for refs in product(domain,repeat=len(nkeys)):
                m={'domain':domain,'names':dict(zip(nkeys,refs)),
                   'preds':dict(zip(pkeys,exts)),'atoms':{}}
                COUNT['fol_bounded_interpretations']+=1
                assert not(all(truth(f,m) for f in fs) and not truth(c,m)),(label,m)

# Exhaustive truth-functional bank: class, equivalence, joint satisfiability, entailment.
entail('S01',[],'P→P'); entail('S02',[],'¬(P∧¬P)')
sat('S03 true',['P→Q'],True); sat('S03 false',['¬(P→Q)'],True)
entail('S04',[],'(P↔Q)→(P→Q)')
for label,a,b,yes in [('S05','¬(P∨Q)','¬P∧¬Q',True),('S06','P→Q','Q→P',False),
 ('S07','P→(Q→R)','(P∧Q)→R',True),('S08','P↔Q','(P→Q)∧(Q→P)',True),
 ('T10','¬A→D','D∨A',True),('T12/T13','(L∧D)→A','L→(D→A)',True),
 ('T20','(L∧D)∨A','L∧(D∨A)',False),('T21','¬(L→A)','L∧¬A',True),
 ('B1.1','¬¬E→P','P∨¬E',True)]: equiv(label,a,b,yes)
for lab,fs,e in [('S09',['P∨Q','¬P'],True),('S10',['P→Q','P','¬Q'],False),
 ('S11',['P→Q','Q→R','¬R'],True),('S12',['P↔Q','P','¬Q'],False)]: sat(lab,fs,e)
for lab,ps,c,e in [('S13',['P→Q','¬Q'],'¬P',True),('S14',['P→Q','¬P'],'¬Q',False),
 ('S15',['P∨Q','P→R','Q→R'],'R',True),('S16',['P→(Q∨R)','¬Q','¬R'],'¬P',True),
 ('M3-I',['P→(Q∧R)','Q'],'P',False),('M3-I-alt',['P↔Q','Q∨R'],'P',False),
 ('M3-D',['P↔Q','P∨R','¬Q'],'R',True),('A2.1',['P∨Q','P→R','¬R'],'Q',True),
 ('B2.1',['P→Q','Q→R','R'],'P',False)]: entail(lab,ps,c,e)
equiv('M3-I pair','¬(P∧Q)','¬P∧¬Q',False)
equiv('M3-I-alt pair','¬(P∨Q)','¬P∨¬Q',False)
sat('M3-I set',['P∨Q','¬P','¬Q'],False)

TFL_PROOFS=[
 (['P∧Q'],'Q∧P'),(['P','Q'],'P∧Q'),(['P→Q','P'],'Q'),(['P'],'Q→P'),([], 'P→P'),
 (['P→Q','Q→R'],'P→R'),(['P∨Q','P→R','Q→R'],'R'),(['P↔Q','P'],'Q'),
 (['P→Q','Q→P'],'P↔Q'),(['P→Q','¬Q'],'¬P'),(['¬¬P'],'P'),([], 'P→(Q→P)'),
 (['P','¬P'],'R'),(['P'],'Q∨P'),(['P∨Q','¬P'],'Q'),(['P→Q','Q→R','¬R'],'¬P'),
 (['¬(P∨Q)'],'¬P∧¬Q'),(['¬¬P'],'P∨R'),(['P→R','¬P→R'],'R'),([], '(P∧Q)→(Q∧P)')]
for i,(ps,c) in enumerate(TFL_PROOFS,1): entail(f'P{i:02}',ps,c)
for lab,ps,c in [('M4-I',['P→Q'],'(P∧R)→(Q∧R)'),('M4-Ib',['¬(P∨Q)'],'¬P'),
 ('M4-alt',['P→Q'],'(R∧P)→(R∧Q)'),('M4-alt-b',['¬(P∧Q)','P'],'¬Q'),
 ('M4-D',['P→Q'],'¬Q→¬P'),('A3.1',[],'(P→(Q→R))→((P∧Q)→R)'),
 ('B3.1',['P∨Q'],'(P→R)→((Q→R)→R)')]: entail(lab,ps,c)

FOL_PROOFS=[
 (['∀x(F(x)→G(x))','F(a)'],'G(a)'),(['F(a)'],'∃x F(x)'),(['∀x F(x)'],'∃x F(x)'),
 (['∀x(F(x)→G(x))','∀x F(x)'],'∀x G(x)'),(['∃x F(x)','∀x(F(x)→G(x))'],'∃x G(x)'),
 (['∀x(F(x)∧G(x))'],'∀x F(x)'),(['∀x F(x)','∀x G(x)'],'∀x(F(x)∧G(x))'),
 (['∃x(F(x)∧G(x))'],'∃x F(x)'),(['∀x¬F(x)'],'¬∃x F(x)'),(['¬∀x F(x)'],'∃x¬F(x)'),
 (['a=b','F(a)'],'F(b)'),(['a=b'],'b=a'),(['a=b','b=c'],'a=c'),([], '∀x x=x'),
 (['∃x(F(x)∧x=a)'],'F(a)'),(['∀x∀y R(x,y)'],'∀y∀x R(x,y)')]
for i,(ps,c) in enumerate(FOL_PROOFS,1): bounded(f'Q{i:02}',ps,c)
for lab,ps,c in [
 ('M7-I',['∀x(F(x)→G(x))','∃x(F(x)∧H(x))'],'∃x(G(x)∧H(x))'),
 ('M7-I-alt',['∀x(F(x)→G(x))','∀x¬G(x)'],'∀x¬F(x)'),
 ('M7-D',['∀x(F(x)→G(x))','¬∃x G(x)'],'¬∃x F(x)'),
 ('A3.2',['∀x(F(x)→G(x))','∀x(G(x)→H(x))'],'∀x(F(x)→H(x))'),
 ('B3.2',['∃x∀y R(x,y)'],'∀y∃x R(x,y)'),
 ('D3',['∀x(F(x)→G(x))','∃x¬G(x)'],'∃x¬F(x)'),
 ('Dprime3',['∀x(F(x)→G(x))','∃x(F(x)∧H(x))'],'∃x G(x)'),
 ('M7-identity',['a=b','R(a,c)'],'R(b,c)'),
 ('M7-identity-alt',['a=b','R(c,a)'],'R(c,b)')]: bounded(lab,ps,c)

worked=model(2,{'a':0,'b':1},F={0},G={0,1},R={(0,1),(1,0)})
check('I01-03',worked,[('F(a)',True),('G(b)',True),('R(a,a)',False),('a=b',False),
 ('∀x(F(x)→G(x))',True),('∃x(G(x)∧¬F(x))',True),('∀x∃y R(x,y)',True),('∃y∀x R(x,y)',False)])
check('I04',model(F={0},G={0}),[('∀x(F(x)→G(x))',True),('∃x F(x)',True),('¬∀x G(x)',True)])
check('I05',model(F={0},G={1}),[('∃x F(x)',True),('∃x G(x)',True),('∃x(F(x)∧G(x))',False)])
check('I06',model(F=set(),G={0}),[('∀x(F(x)→G(x))',True),('∀x(G(x)→F(x))',False)])
identity=model(2,{'c':0},R={(0,0),(1,1)})
check('I07/B3.3',identity,[('∀x∃y R(x,y)',True),('∃y∀x R(x,y)',False),('∀x R(x,x)',True),('∀x R(x,c)',False),('∀y∃x R(x,y)',True),('∃x∀y R(x,y)',False)])
check('I08',model(3,{'a':0,'b':1,'c':2},R={(0,1),(1,2)}),[('R(a,b)',True),('R(b,c)',True),('R(a,c)',False)])
check('I09a',model(1,{'a':0,'b':0},F={0}),[('a=b∧F(a)∧F(b)',True)])
check('I09b',model(2,{'a':0,'b':1},F={0,1}),[('¬a=b∧F(a)∧F(b)',True)])
relation_properties=['∀x R(x,x)','∀x∀y(R(x,y)→R(y,x))',
 '∀x∀y∀z((R(x,y)∧R(y,z))→R(x,z))','∀x∀y((R(x,y)∧R(y,x))→x=y)']
check('I10a',identity,list(zip(relation_properties,[True]*4)))
check('I10b',worked,list(zip(relation_properties,[False,True,False,False])))
check('I12',model(1,F=set(),G=set()),[('∀x(F(x)→G(x))',True),('∃x F(x)',False)])
check('M6-I',model(R={(0,0),(0,1)}),[('∃x∀y R(x,y)',True),('∀y∀x R(x,y)',False)])
check('M6-D',model(F={0},G=set()),[('∃x(F(x)→G(x))',True),('(∃x F(x)→∃x G(x))',False)])
check('M7bad1',model(2,{'a':0},F={0}),[('F(a)',True),('∀x F(x)',False)])
check('M7bad2/A3.3',model(2,{'a':0},F={1}),[('∃x F(x)',True),('F(a)',False)])
check('A2.2',model(F={0},G={1}),[('∀x(F(x)∨G(x))',True),('(∀x F(x)∨∀x G(x))',False)])
check('B3.3-new',model(2,{'a':0},R={(1,0)}),[('∃x R(x,a)',True),('∃x R(x,x)',False)])
check('B2.2',model(F={0},G={0}),[('∃x F(x)',True),('∀x(F(x)→G(x))',True),('∀x G(x)',False)])
check('paper',model(1,W={0},P={0},A=set()),[('∀x(A(x)→P(x))',True),('∃x(W(x)∧¬A(x))',True),('∃x(W(x)∧¬P(x))',False)])
check('A4',model(1,{'a':0},A={0},L=set()),[('∀x(L(x)→A(x))',True),('A(a)',True),('L(a)',False)])
check('B4',model(1,{'a':0},T=set(),A={0}),[('∀x(T(x)→A(x))',True),('¬T(a)',True),('¬A(a)',False)])
check('D2/Dprime2',model(1,F=set(),G={0}),[('∀x(F(x)→G(x))',True),('(∃x G(x)→∃x F(x))',False),('(∀x G(x)→∀x F(x))',False)])
check('M5-I',model(4,{'a':0},R={0,1},P={2,3},H={(0,2),(1,3)}),[
 ('∀x(R(x)→∃y(P(y)∧H(x,y)))',True),('∃y(P(y)∧∀x(R(x)→H(x,y)))',False)])
check('B1.3',model(4,M={0,1},S={2,3},T={(0,2),(1,3)}),[
 ('∀y(S(y)→∃x(M(x)∧T(x,y)))',True),('∃x(M(x)∧∀y(S(y)→T(x,y)))',False)])
check('B1.4',model(1,{'a':0},M=set(),T=set()),[
 ('∃x((M(x)∧∀y(M(y)→y=x))∧¬T(x,a))',False),
 ('¬∃x((M(x)∧∀y(M(y)→y=x))∧T(x,a))',True)])
# Identity-cardinality translations against independent counting specifications.
exact2=parse('∃x∃y(((S(x)∧S(y))∧¬x=y)∧∀z(S(z)→(z=x∨z=y)))')
exact1=parse('∃x((R(x)∧¬C(x))∧∀y((R(y)∧¬C(y))→y=x))')
atmost1=parse('∀x∀y(((R(x)∧¬C(x))∧(R(y)∧¬C(y)))→x=y)')
for n in range(1,4):
    for s in product([False,True],repeat=n):
        ext={i for i,b in enumerate(s) if b}; m=model(n,S=ext)
        assert truth(exact2,m)==(len(ext)==2); COUNT['fol_model_assertions']+=1
    for rs in product([False,True],repeat=n):
        for cs in product([False,True],repeat=n):
            r={i for i,b in enumerate(rs) if b}; c={i for i,b in enumerate(cs) if b}
            m=model(n,R=r,C=c)
            assert truth(exact1,m)==(len(r-c)==1)
            assert truth(atmost1,m)==(len(r-c)<=1)
            COUNT['fol_model_assertions']+=2

# Negative controls ensure the evaluator rejects invalid goals and accepts actual countermodels.
entail('negative-control affirm consequent',['P→Q','Q'],'P',False)
check('negative-control arbitrary-name',model(2,{'a':0},F={0}),[('F(a)',True),('∀x F(x)',False)])

manifest=json.loads((COURSE/'authoring.json').read_text())
track=manifest['tracks'][0]
assert sum(m['hours'] for m in track['modules']) == track['baseline_hours'] == 150
assert len(track['modules']) == 8
for field in ['readme','outcomes','assessment','examiner','source_audit']:
    assert (ROOT/track[field]).is_file(),track[field]
for mod in track['modules']: assert (ROOT/mod['path']).is_file(),mod['path']
for path in COURSE.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if re.match(r'[a-z]+:',target) or target.startswith('#'): continue
        local=target.split('#')[0]
        assert (path.parent/local).exists() or (path.parent/local).resolve() == HERE/'results.json', (str(path.relative_to(ROOT)),target)
        COUNT['local_links']+=1
sources={}
for rel in ['collection/philosophy-study-collection/texts/introduction_logic/required/forallx_calgary_textbook.pdf',
 'collection/philosophy-study-collection/texts/introduction_logic/solutions/forallx_calgary_solutions.pdf']:
    sources[rel]=hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
report={'date':'2026-10-20','status':'pass','counts':COUNT,'baseline_hours':150,
 'assessment_minutes':{'translation':30,'semantics':30,'proof':60,'limits':20,'total':140},
 'source_sha256':sources,
 'limitations':['Not a natural-deduction proof checker: derivation lines require direct rule/scope review.',
 'FOL valid-goal enumeration covers only domains of size 1 and 2; it is not a proof of FOL validity.',
 'Explicit countermodels and cardinality checks use their stated finite domains, including sizes 3 and 4.',
 'No learner pilot, expert review, live Carnap test, or rendered accessibility QA.']}
(HERE/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
