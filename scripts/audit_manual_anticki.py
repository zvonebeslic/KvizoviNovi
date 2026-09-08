import json, glob
from pathlib import Path
manifest=json.load(open('redo/AntickiRim_source_index.json',encoding='utf-8'))
byq={x['question']:x for x in manifest}
seen={}; extras=[]; files=[]
for fn in sorted(glob.glob('redo/AntickiRim*.json')):
    if fn.endswith('_source_index.json') or fn.endswith('_manual_audit.json'):
        continue
    files.append(fn)
    try: data=json.load(open(fn,encoding='utf-8'))
    except Exception as e:
        extras.append({'file':fn,'error':str(e)}); continue
    if not isinstance(data,list): continue
    for pos,item in enumerate(data,1):
        q=item.get('question','')
        if q not in byq:
            extras.append({'file':fn,'position':pos,'question':q}); continue
        idx=byq[q]['index']; seen.setdefault(idx,[]).append({'file':fn,'position':pos})
missing=[x for x in manifest if x['index'] not in seen]
duplicates=[{'index':i,'occurrences':v} for i,v in seen.items() if len(v)>1]
report={'source_total':len(manifest),'matched_unique':len(seen),'missing_count':len(missing),'duplicate_index_count':len(duplicates),'extra_or_changed_count':len(extras),'files_scanned':files,'missing':missing,'duplicates':duplicates,'extra_or_changed':extras}
Path('redo/AntickiRim_manual_audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['source_total','matched_unique','missing_count','duplicate_index_count','extra_or_changed_count']},ensure_ascii=False))
