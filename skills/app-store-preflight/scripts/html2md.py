import sys, re, html
from html.parser import HTMLParser
src=open(sys.argv[1],encoding='utf-8').read()
# keep main content
m=re.search(r'<main.*?</main>',src,re.S); src=m.group(0) if m else src
src=re.sub(r'<(script|style|nav|footer)[^>]*>.*?</\1>','',src,flags=re.S)
class P(HTMLParser):
    def __init__(s): super().__init__(); s.out=[]; s.pre=''
    def handle_starttag(s,t,a):
        a=dict(a)
        if t in('h1','h2','h3','h4','h5'):
            s.out.append('\n\n'+'#'*int(t[1])+' '+(('['+a['id']+'] ') if a.get('id') and re.match(r'^\d',a.get('id','')) else ''))
        elif t=='li': s.out.append('\n- ')
        elif t in('p','div','br','ul','ol','tr'): s.out.append('\n')
        elif t=='a' and a.get('href'): s.href=a['href']
        if a.get('id') and re.match(r'^\d+(\.\d+)*$',a['id']) and t not in('h1','h2','h3','h4','h5'):
            s.out.append(f'\n\n[[GL {a["id"]}]] ')
    def handle_endtag(s,t):
        if t in('p','li','h1','h2','h3','h4','h5'): s.out.append('\n')
    def handle_data(s,d): s.out.append(re.sub(r'\s+',' ',d))
p=P(); p.feed(src); t=''.join(p.out)
t=re.sub(r'\n[ \t]+','\n',t); t=re.sub(r'\n{3,}','\n\n',t)
print(t.strip())
