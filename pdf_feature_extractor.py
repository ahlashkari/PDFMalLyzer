import csv
import sys
import fitz
import os
import pandas as pd
from fitz import TextPage
dir = os.getcwd()
path = sys.argv[1]
if(not os.path.isabs(path)):      #if the given path is not absolute, we should convert it to one
         print("the path is path is "+str(path))
         print("dir is "+str(dir))
         path = os.path.join(dir,path)
         print("the path is not absolute and the new path is "+str(path))
if(os.path.isdir(path)):
        res = pd.DataFrame(columns=('pdfsize','metadata size', 'page','objects','title characters','isEncrypted','embedded files','contains text','images'))
else:
        print("specify a valid pdf folder path as an argument")
        sys.exit()
i = 0
for j in os.listdir(path):
        f = path + "/" + j
        pdfFileObj = open(f,'rb')
        try:
                doc = fitz.open(f)
                #print("fitz "+str(doc.xrefLength))
                file = open(f, 'rb')
        except:
                continue
        #metadata
        metadata = doc.metadata

        #title
        if metadata:
                title = metadata['title']
        else:
                title = ""
        if not title:
                title = ""
        #whether file is encrypted
        isEncrypted = metadata['encryption']
        if(not isEncrypted):
                isEncrypted = 0
        else:
                isEncrypted = 1
        #number of objects
        objects = doc.xrefLength()
        # printing number of pages in pdf file
        numPages = doc.pageCount
        #extracted text
        pdfsize = int(os.path.getsize(f)/1000)
        #extracted text
        found = False
        text = ""
        try:
                for page in doc:
                        text += page.getText()
                        if (len(text) > 100):
                                found = True
                                break
        except:
                break
        #print("file contains text " + str(found))
        # number of embedded files
        embedcount = doc.embeddedFileCount()
        #number of images
        imgcount = 0
        try:
         for k in range(len(doc)):
                try:
                 #print(doc.getPageImageList(k))
                 imgcount = len(doc.getPageImageList(k)) + imgcount
                except:
                 continue

        except:
         break



        #writing the features in a csv file
        res.loc[i] = [pdfsize, len(str(metadata).encode('utf-8'))] + [numPages] + [objects] + [len(title)] + [isEncrypted] + [embedcount] + [found] + [imgcount]
        i +=1
res.to_csv(os.path.relpath("result.csv",start=os.curdir))
print("general features extracted successfully...")


print("extracting structural features...")        #extracting structural features using pdfid
i = 0
var = r"tr '\n' ','"
header = ['','header','obj','endobj','stream','endstrean','xref','trailer','startxref','pageno' ,'encrypt','ObjStm','JS','Javascript','AA','OpenAction','Acroform','JBIG2Decode','RichMedia','launch','EmbeddedFile','XFA','Colors']
with open(os.path.relpath("output.csv"),'w',encoding='UTF8') as output:
        writer = csv.writer(output)
        writer.writerow(header)
os.chdir('pdfid')
for j in os.listdir(path):
         f = path + "/" + j
         #os.chdir('/home/mary/Downloads/pdfid_v0_2_7')
         os.system("python pdfid.py "+str(f)+"| awk '{print $2}' | "+var+ ">> ../output.csv")
         os.system("echo "" >> ../output.csv") 
os.chdir('../')
a = pd.read_csv("result.csv")
b = pd.read_csv("output.csv")
os.system("paste result.csv output.csv > output1.csv")
os.remove("output.csv")
os.remove("result.csv")









