import json,sys
t=open('build/template.html').read()
def js(o): return json.dumps(o,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')
d=json.load(open('build/data.json'))
w110=json.load(open('geo/node_modules/world-atlas/countries-110m.json'))
w50=json.load(open('geo/node_modules/world-atlas/countries-50m.json'))
out=t.replace('__DATA__',js(d)).replace('__W110__',js(w110)).replace('__W50__',js(w50))
open('index.html','w').write(out)
# test build with local libs
d3=open('geo/node_modules/d3/dist/d3.min.js').read(); tj=open('geo/node_modules/topojson-client/dist/topojson-client.min.js').read()
test=out.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>','<script>'+d3+'</script>').replace('<script src="https://cdn.jsdelivr.net/npm/topojson-client@3.1.0/dist/topojson-client.min.js"></script>','<script>'+tj+'</script>')
test='<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{margin:0}</style></head><body>'+test+'</body></html>'
open('build/test.html','w').write(test)
print(len(out)//1024,'KB')
