# -*- coding: utf-8 -*-
# importing package
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
# Define base files to compare

path = '/home/sistemas/'
base = path+'Compras/Pedidos Mayoristas/Pedidos Mayoristas 2017/Makicop/'
recover1 = path+'backup1/pdf'
recover2 = path+'backup1/RespaldoGarmas/pdf'
recover3 = path+'backup2/RecoveryTL14/pdf'
recover4 = path+'backup3/RecoveryGarmas/pdf'
recover5 = path+'backup3/RespaldoGarmas/pdf'

recovery = [recover1,recover2,recover3]

compareFiles = []
raw_documents = []

print "Searching base files"
for i in os.listdir(base):
    ruta = base+i
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

print "Makeing compare Matrix"
for i in compareFiles:
    count = 0
    text = ""
    pdfFileObj = open(i,'rb')
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
        #print type(i)
        text = textract.process(i, method='tesseract', language='eng', encoding='ascii')
        #print text
        raw_documents.append(text)

gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]

dictionary = gensim.corpora.Dictionary(gen_docs)
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
tf_idf = gensim.models.TfidfModel(corpus)
sims = gensim.similarities.Similarity('/home/sistemas/Documentos/Scripts/',tf_idf[corpus],
                                      num_features=len(dictionary))

# Begin analysis
print "Begin análisis"
grateCounter = 0
resultados = []

for recover in recovery:
	print recover
	for i in os.listdir(recover):
        	if ".pdf" in i:
			try:
				incidencia = 0
				print "\t"+recover+"/"+i
                		pdfFileObj = open(recover+"/"+i,'rb')
                		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
                		num_pages = pdfReader.numPages
                		count = 0
                		text = ""
                		while count < num_pages:
                        		pageObj = pdfReader.getPage(count)
                        		count +=1
                        		text += pageObj.extractText()
                		if text != "":
                    			text = text
                    			text=unicodedata.normalize('NFKD',text).encode('ascii','ignore')
					raw_documents.append(text)
                		else:
                    			#print "using tesseract"
                    			text = textract.process(recover+"/"+i, method='tesseract', language='eng', encoding='ascii')
                    			raw_documents.append(text)
                		query_doc = [w.lower() for w in word_tokenize(text)]
                		query_doc_bow = dictionary.doc2bow(query_doc)
                		query_doc_tf_idf = tf_idf[query_doc_bow]
                		sims[query_doc_tf_idf]
                		for j in sims[query_doc_tf_idf]:
                    			if j >= .5 and incidencia == 0:
                        			resultados.append(str(sims[query_doc_tf_idf].tolist().index(j))+":"+str(j))
                        			shutil.move(recover+"/"+i,recover+"/maki/"+i)
                        			incidencia+=1
			except:
				pass
