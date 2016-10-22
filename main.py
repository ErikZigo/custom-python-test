import pip 
pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', '--cert=/tmp/cacert.pem', 'networkx']) 
#pip.main(['install', '--disable-pip-version-check', '--no-cache-dir', 'networkx'])
import networkx as nx 
print ("works!") 
