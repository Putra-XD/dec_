import time, struct, marshal, imp, os

def main():
	fs = raw_input("Enter File  :  ")
	l=lambda _:compile(_,'','exec')
	open('out.pyc','wb').write(imp.get_magic()+struct.pack("<L",int(time.time()))+l(marshal.loads(l(open(fs).read()).co_consts[8].decode('base64').decode('zlib')).co_consts[-1].decode('zlib')).co_consts[8].decode('base64').decode('zlib'))

main()
