import os
def populate():
	f=open("/home/mrunmayi/wordify-new/wordsadd.txt",'r')
	wrd=True
	str1=""
	count=0
	finalcount=0
	l1=[]
	for line in f:
		if(line!="\n") and wrd==True:
			word=line.split("\n")[0]
			#print word
			if(Word.objects.filter(word=word).exists()):
				print word,"aahe"
			else:
				obj=Word(word=word)
				obj.save()
				print word,"add zala"
				count+=1
				finalcount+=1
				l1.append(word)
		if(line=="\n") and wrd==True:
			pkey=0
			wrd=False
			continue;
		if(line!="\n" and wrd==False):	
			line=line.split("; ")
			str1=""
			for i in range(len(line)):
				str1=str1+"\n"+str(i+1)+")"+str(line[i])
		
			print pkey,str1
			
			obj=Word.objects.get(word=l1[pkey])
			obj.mean=str1
			obj.save()
			pkey+=1
		if(line=="\n" and wrd==False):
			wrd=True
			count=0
			l1=[]
			continue;
# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wordify.settings')
    from words.models import Word
    populate()

	
