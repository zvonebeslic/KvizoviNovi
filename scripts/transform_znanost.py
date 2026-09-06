import urllib.request
url='https://raw.githubusercontent.com/zvonebeslic/KvizoviNovi/main/scripts/transform_remaining.py'
text=urllib.request.urlopen(url,timeout=30).read().decode('utf-8')
start=text.index('FILES = [')
end=text.index(']\n', start)+2
text=text[:start]+"FILES = ['Znanost.json']\n"+text[end:]
exec(compile(text,'transform_znanost_runtime.py','exec'))
