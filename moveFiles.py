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
path = '/home/sistemas/Documentos/Recuperados/pdf/Eliminar/Facturas/'
name = 'f1558602112.pdf'
name2 = "/home/sistemas/Documentos/PDF/Thebeamertheme-cuernabeamertheme∗GeriOchoageri@bluesimplexcomSeptember24,20161IntroductionThispack0.pdf"
compareFiles = [path+name,name2]
raw_documents = []
# Define the RAW text to compare
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
	text=unicodedata.normalize('NFKD',text).encode('ascii','ignore')
	raw_documents.append(text)
# Tokenize text
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
print gen_docs
# Generate Dictionari
dictionary = gensim.corpora.Dictionary(gen_docs)
# Corpus to compare
corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
# TF-ID method
tf_idf = gensim.models.refModel(corpus)
# Sims
sims = gensim.similarities.Similarity('/home/sistemas/Documentos/Scripts/',tf_idf[corpus],
                                      num_features=len(dictionary))
# Begins, text analisis
for i in os.listdir(path):
	if i != name:
		pdfFileObj = open(path+i,'rb')
		pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
		num_pages = pdfReader.numPages
		count = 0
		text = ""
		while count < num_pages:
			pageObj = pdfReader.getPage(count)
			count +=1
			text += pageObj.extractText()
		text = unicodedata.normalize('NFKD',text).encode('ascii','ignore')
		query_doc = [w.lower() for w in word_tokenize(text)]
		query_doc_bow = dictionary.doc2bow(query_doc)
		query_doc_tf_idf = tf_idf[query_doc_bow]
		sims[query_doc_tf_idf]
		if sims[query_doc_tf_idf] >= 0.8:
			print "Probablemente ",i," sea una factura"
		else:
			print "Probablemente ",i," no lo sea"
