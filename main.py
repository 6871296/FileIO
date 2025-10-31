import sys,os
print("FileIO for Python(Indev1)")
path='~'
isfile=False
while True:
	cmd=input(os.path.abspath(path)+'>_').split(' ')
	if cmd[0]=='pwd':
		print(os.path.abspath(path))
	elif cmd[0]=='open':
    	isfile=True
    	path2=path
    	if cmd[1][0]='/':
      		path=cmd[1]
    	else:
      		path+='/'+cmd[1]
    	if not os.path.exists(path):
      		print('This path does not exist.')
      		path=path2
      		continue
    	try:
      		r=open(path,'r')
      		w=open(path,'w')
    	except IOError:
      		isfile=False
    	if isfile:
      		t=r.read()
      		r.close()
      		print(t)
	elif cmd[0]=='io':
		if isfile:
			if cmd[1]=='-r' or cmd[1]=='--read':
   				print(t)
	   		elif cmd[1]=='-w' or cmd[1]=='--write':
				w.write(cmd[2])
	elif cmd[0]='quit':
		if input('Enter y to quit')=='y':
			break;
