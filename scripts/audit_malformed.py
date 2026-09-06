import json, urllib.request
BASE='https://raw.githubusercontent.com/zvonebeslic/balkanska_pub_prica/main/'
FILES=['AmerickiPredsjednici.json','AntickiRim.json','Gaming.json','Glazba.json','Knjizevnost.json','Moreplovci.json','Nogomet.json','Sport.json','Svastara.json','Zemljopis.json']
count=0
for fn in FILES:
    data=json.loads(urllib.request.urlopen(BASE+fn,timeout=60).read().decode('utf-8'))
    for i,q in enumerate(data,1):
        a=q.get('answers')
        if not (isinstance(a,list) and len(a)>0 and str(a[0]).strip()):
            count+=1
            print('MALFORMED',fn,i,'QUESTION=',repr(q.get('question')),'ANSWERS=',repr(a))
print('TOTAL_MALFORMED',count)
