 importing package
from __future__ import division
import os
import re
import sys
import nltk
import gensim
import pprint
import shutil
import PyPDF2
import textract
import unicodedata
# importing package functions
from nltk import *
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
#reload(sys)
#sys.setdefaultencoding('utf8')
# Define base files to compare
path = '/home/sistemas/'
base = 'Compras/Pedidos Mayoristas/Pedidos Mayoristas 2017/Makicop/'
recover = 'backup1/pdf/'
compareFiles = [] #"/home/sistemas/Documentos/Scripts/base.pdf"]
raw_documents = []
TRindex = []

for i in os.listdir(path+base):
    ruta = path+base+i
    if not os.path.isdir(ruta) and ".pdf" in i:
        compareFiles.append(ruta)
    elif os.path.isdir(ruta):
        for j in os.listdir(ruta):
            subruta = ruta+"/"+j
            if not os.path.isdir(subruta) and ".pdf" in j:
                compareFiles.append(subruta)
            elif os.path.isdir(subruta):
                for k in os.listdir(subruta):
                    subsubruta = subruta+"/"+k
                    if not os.path.isdir(subsubruta) and ".pdf" in k:
                        compareFiles.append(subsubruta)

for i in compareFiles:
    if "TR" in i:
        TRindex.append(compareFiles.index(i)) #a = 1 #," "+i #print a,":"+i #a+=1
        print compareFiles.index(i)," ",i

for i in TRindex:
    count = 0
    text = ""
    print compareFiles[i]
    pdfFileObj = open(compareFiles[i],'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()
    if text != "":
        text = text
        text=unicodedata.normalize('NFKD',text).encode('ascii','ignore')
        raw_documents.append(text)
    else:
        text = textract.process(compareFiles[i], method='tesseract', language='eng')
        #if not isinstance(text,str):
        #    text=unicodedata.normalize('NFKD',text).encode('ascii','ignore')
        raw_documents.append(text)

for text in raw_documents:
    for w in word_tokenize(text):
        print raw_documents.index(text),": ",w.lower
        
print gen_docs
# Generate Dictionari
dictionary = gensim.corpora.Dictionary(gen_docs)
# Corpus to compare
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# TF-ID method
tf_idf = gensim.models.TfidfModel(corpus)
# Sims
sims = gensim.similarities.Similarity('/home/sistemas/Documentos/Scripts/',tf_idf[corpus],
                                      num_features=len(dictionary))
