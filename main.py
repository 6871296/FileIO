import sys,os
print("FileIO for Python(Indev2)")
path='~'
isfile=False
while True:
	cmd=input(os.path.abspath(path)+' >_ ').split(' ')
	if cmd[0]=='pwd':
		print(os.path.abspath(path))
	elif cmd[0]=='open':
		if isfile:
			w.close()
			r.close()
			a.close()
		isfile=True
		path2=path
		if cmd[1][0]=='/' or cmd[1][0]=='~':
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
			a=open(path,'a')
			poi=0
		except IOError:
			isfile=False
		if isfile:
			t=r.read()
			print(path+' is a readable file. Context:\n'+t)
		else:
			print(path.split('/')[-1]+'\n')
			l=os.listdir(path)
			if l==[]:
				print('(Empty Directory)')
			for i in l:
				if l.index(i)==len(l)-1:
					print('\-'+i)
				else:
					print('|-'+i)
	elif cmd[0]=='poi':
		if isfile:
			if cmd[1]=='-r' or cmd[1]=='--read':
				print('char#'+poi,t[poi])
			elif cmd[1]=='-w' or cmd[1]=='--write':
				t=t[:poi]+cmd[2]+t[poi+1:]
			elif cmd[1]=='-m' or cmd[1]=='--move':
				if poi+int(cmd[2])<=len(t) and poi+int(cmd[2])>=0:
					poi+=int(cmd[2])
				else:
					print('Pointer out of range.')
			elif cmd[1]=='-a' or cmd[1]=='--append':
				t=t[:poi]+t[poi]+cmd[2]+t[poi:]
		else:
			print('The current path is not a file.')
	elif cmd[0]=='ls':
		if isfile:
			print('The current path is a file.')
		else:
			l=os.listdir(path)
			print(path.split('/')[-1]+'\n')
			if l==[]:
				print('(Empty Directory)')
			else:
				for i in l:
					if l.index(i)==len(l)-1:
						print('\-'+i)
					else:
						print('|-'+i)
				print('total '+str(len(l))+' items')
	elif cmd[0]=='save':
		if isfile:
			w.close()
			a.close()
			r.close()
			w=open(path,'w')
			a=open(path,'a')
			r=open(path,'r')
			t=r.read()
			print('File saved.')
		else:
			print('The current path is not a file.')
	elif cmd[0]=='io':
		if isfile:
			if cmd[1]=='-r' or cmd[1]=='--read':
				if len(cmd)==2:
					print(t[:poi]+'*'+t[poi]+'*'+t[poi:])
				else:
					if len(cmd)==3:
						if cmd[2]=='--hide-poi':
							print(t)
					elif len(cmd)==5:
						if cmd[2]=='-s' or cmd[2]=='--sized':
							start=int(cmd[3])
							end=int(cmd[4])
							print(t[start:end])
							print(t[poi:poi+size])
			elif cmd[1]=='-w' or cmd[1]=='--write':
				w.write(cmd[2])
			elif cmd[1]=='-a' or cmd[1]=='--append':
				a.write(cmd[2])
		else:
			print('The current path is not a file.')
	elif cmd[0]=='quit':
		if input('Enter y to quit')=='y':
			break
	else:
		print('Unknown command: '+cmd[0])
if isfile:
	w.close()
	r.close()
	a.close()