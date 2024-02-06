#!/usr/bin/env python3

proto= ["ssh","http","https"]
protoa= ["ssh","http","https"]
print(proto)
proto.append("dns")
protoa.append("dns")
print(proto)
proto2=[22,80,443,53]
proto.extend(proto2)
print(proto)
protoa.append(proto2)
print(protoa)
proto.append("ftp")
proto2.append(20)
proto2.append(21)
protoa.insert(4,"ftp")
protoa[5].append(20)
protoa[5].append(21)
print(proto)
print(proto2)
print(protoa)
