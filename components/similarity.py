import os
import sys
import csv
import string
import pandas as pd
from fse.models import Average, SIF
from fse import IndexedList
from shorttext.utils import load_word2vec_model
import gensim.downloader
import numpy as np
from gensim.matutils import unitvec

wvmod = gensim.downloader.load("word2vec-google-news-300")
wvmod=load_word2vec_model('/content/drive/MyDrive/GoogleNews-vectors-negative300.bin.gz')
print("News loaded")

def scaled_sim(a, b):
  sim=np.dot(a, b)
  norm_a = np.linalg.norm(a)
  norm_b = np.linalg.norm(b)
  inter=sim/(norm_a*norm_b)
  final=(inter+1)/2
  return final

filelist=["amazon", "flipkart", "ola", "toi", "uber"]
dirpath = "./data"

sentences=list()
for fileitem in filelist:
  print("Reading " + fileitem + "...")
  filepath = os.path.join(dirpath, fileitem)
  with open(filepath + ".txt") as f:
    temps = list()
    for a in map(lambda x: x.split(), f.read().split("\n")):
      temps.extend(a)
    sentences.append(a)
  
  print("Read " + fileitem)
wvmod = gensim.downloader.load("word2vec-google-news-300")

avg = Average(wvmod)
avg.wvmod = gensim.downloader.load("word2vec-google-news-300")
train(IndexedList(sentences))
sif = SIF(wvmod)
sif.train(IndexedList(sentences))

simMat = [[0 for a in filelist] for b in filelist]
for a in range(len(filelist)):
  for b in range(len(filelist)):
    sim1 = avg.sv.similarity(a, b)
    sim2 = sif.sv.similarity(a, b)
    simMat[a][b] = sim2
    # simMat[a][b] = scaled_sim(sim1, sim2)

for i in range(len(filelist)):
  print('  '.join(["     "] + [str(a).center(7, ' ') for a in range(len(filelist))]))
  print(str(i).center(4, " "), end = "  ")
  for j in range(len(filelist)):
    print(str(round(simMat[i][j], 4)).ljust(7, "0"), end = "  ")
  print()