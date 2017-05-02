import os
def one_time(folderpath=None):
	for subdir,dirs,files in os.walk(folderpath):
		for file in files:
			a=file.split('_')
			b=a[-1].split('.')
			if (b[-1]=='jpg'):
				if int(b[0])<10:
					newname=''.join(['_'.join([i for i in a[:-1]]),'_0','.'.join([i for i in b])])
					print(folderpath)
					os.rename(folderpath+'/'+file,folderpath+'/'+newname)
for subdir,dirs,files in os.walk('./gif'):
	for dir in dirs:
	    one_time(os.path.join(subdir,dir))
	
