import os
import sys
import hashlib
import logging
PY_VERSION=sys.version_info[0]

if PY_VERSION==2:
  import urllib2
else :
  import urllib.request
  
#this hash function receives the name of the file and returns the hash code
def get_hash(name):
  readsize = 64 * 1024
  with open(name, 'rb') as f:
    size = os.path.getsize(name)
    data = f.read(readsize)
    f.seek(-readsize, os.SEEK_END)
    data += f.read(readsize)
  return hashlib.md5(data).hexdigest()

def go_subtitle(filename):
  url='http://api.thesubdb.com/?action=download&hash='+get_hash(filename)+'&language=en'
  headers={'User-Agent': 'SubDB/1.0'}
  if PY_VERSION==2:
    req=urllib2.Request(url,'',headers)
    res=urllib2.urlopen(req).read()
  else:
    req=urllib.request.Request(url,'',headers)
    res=urllib.request.urlopen(req).read()
  
  with open(filename+'.srt','wb') as f:
    f.write(res)
    logging.info('Downloaded!!')   

def main():
  inp='2'
  f=open("stat.txt","w")
  f.write("Downloaded : "+sys.argv[1])  
  if inp=='2':
    proxy_handler = urllib2.ProxyHandler({})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
  else :
    setProxy()
    
  go_subtitle(sys.argv[1])
      
if __name__=='__main__':
  main()
