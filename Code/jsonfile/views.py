from django.http import HttpResponse
from django.shortcuts import render
from itertools import permutations
from django.core.cache import cache
import pydoop.hdfs as hdfs
import hadoopy

# Get the hostname and service port of remote file system
hostname = os.environ['FILESYS_HOSTNAME']
port = os.environ['FILESYS_PORT']

def getjsonfile(request):

   # Read json file : myFile.json from remote file system
   fs_path = "http://" + hostname + ":" + port + "/webhdfs/v1/myDir/myFile.json?op=OPEN"
   r=requests.get(fs_path, stream=True)
   r.raw.decode_content = True
   print r
   x=r.raw.read().decode("utf-8",errors="ignore")
   print json.loads(x)
   return json.loads(x)

def storejsonfile(request):
   from_path = request.POST.get('from_path',"")
   to_path = request.POST.get('to_path',"")
   to_path = "http://" + hostname + ":" + port "/webhdfs/v1/" + to_path
   hdfs.put(from_path, to_path)
   return 



