info=dict()
print info
print type(info)
print len(info)

info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}
print info

info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}

#update
item_key="version"

if item_key in info:  #validate for key
    info[item_key]=3.0

info["arch"]="x86_64"  #add an element
print info


info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}

value=info.pop("desc")  #get the value from hash
print value
print

del info["app"],info["version"]  #deleting from hash

print info


info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}

print info["hostname"]
print info["app"]
print info["version"]
print info.get("domain")
print info.get("domin")
print info.get("domin","unknown-key")



info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}

print info.keys()  #displays only keys
print
print info.values() #displays only values
print
print info.items() #displays full hash


info={"hostname":"ws1",
      "domain":"rootcap.in",
      "desc":"web server",
      "app":"apache htttpd",
      "version":2.7}

for item in info:
    print item,"->",info[item]

for k,v in info.iteritems():
    print k,":",v

print info.iteritems()
print






