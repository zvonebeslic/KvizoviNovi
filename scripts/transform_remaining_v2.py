import urllib.request
url='https://raw.githubusercontent.com/zvonebeslic/KvizoviNovi/main/scripts/transform_remaining.py'
text=urllib.request.urlopen(url,timeout=30).read().decode('utf-8')
old="""def first_answer(q):
    a=q.get('answers')
    if isinstance(a,list) and a: return str(a[0]).strip()
    raise ValueError('Nema izvornog odgovora')
"""
new="""def first_answer(q):
    a=q.get('answers')
    if isinstance(a,list) and a: return str(a[0]).strip()
    if isinstance(a,str) and a.strip(): return a.strip()
    if isinstance(a,dict):
        for k in ('correct','answer','A','a'):
            if k in a and str(a[k]).strip(): return str(a[k]).strip()
    question=str(q.get('question',''))
    overrides={
      'Na Jabukovcu u kojem selu žive Lovrakova tri đaka':'Velikom Selu',
      'Koja knjiga uvodi čitatelja u svijet lova na kitove':'Moby Dick',
      'Koji se naziv koristi za tradicionalnu zastavu europskih i američkih pirata':'Jolly Roger'
    }
    for prefix,answer in overrides.items():
        if prefix in question: return answer
    raise ValueError('Nema izvornog odgovora: '+question+' / '+repr(a))
"""
if old not in text: raise SystemExit('Patch target nije pronađen')
text=text.replace(old,new)
exec(compile(text,'transform_remaining_v2_runtime.py','exec'))
