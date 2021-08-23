# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:49:36 2020

"""

import pandas as pd
import os

ncbi = pd.read_csv("pubmed.csv", sep=",")
cochrane = pd.read_csv("cochrane.csv", sep = ",")

ncbit = ncbi["Title"]
cochranet = cochrane["Title"]

comuns = []
for i in range(0, len(ncbit)):
    if ncbit[i].lower() not in cochranet:
        if ncbit[i].lower() not in comuns:
            comuns.append(ncbit[i].lower())

for j in range(0, len(cochranet)):
    if cochranet[j].lower() not in ncbit:
        if cochranet[j].lower() not in comuns:
            comuns.append(cochranet[j].lower())
            
out = open("out.txt", 'w')
t = open("test.temp", 'w')
for i in comuns:
    try:
        out.write(i)
        out.write("\n")
    except:
        k = i
        for j in range(0, len(i)):
            try:
                t.write(i[j])
            except:
                k = k.replace(k[j], "_")
        out.write(k)
        out.write("\n")
out.close()
t.close()
os.remove("test.temp")
#**************************************************************

#Avaliando se as kw estão no abstract, titulo ou kw do cochrane
abstract = pd.read_csv("cochrane.csv", sep = ",")
title = abstract["Title"].tolist()
kw = abstract["Keywords"].tolist()
abstract = abstract["Abstract"].tolist()
cochrane = {}
for i in range(0, len(abstract)):
    cochrane[title[i]] = (abstract[i], kw[i])
final =[]
for i in cochrane.keys():
    if ("Acinetobacter" in i) or ("A. baumannii" in i) or ("baumannii" in i):
        try:
            final.append(i.lower())
        except:
            print(i)
        continue
    elif ("Acinetobacter" in str(cochrane[i][0])) or ("A. baumannii" in str(cochrane[i][0])) or ("baumannii" in str(cochrane[i][0])):
        try:
            final.append(i.lower())
        except:
            print(i)
        continue
    elif ("Acinetobacter" in str(cochrane[i][1])) or ("A. baumannii" in str(cochrane[i][1])) or ("baumannii" in str(cochrane[i][1])):
        try:
            final.append(i.lower())
        except:
            print(i)
        continue
#**********************************************************************
      
#Verificando se as kw estão no abstract, titulo ou kw do PubMed
abstract = pd.read_csv("pubmedID.txt", sep = "LLLLLLLL")
abstract = abstract[abstract.columns[0]].tolist()
pubmed = {}
for i in range(0, len(abstract)):
    if "TI  -" in abstract[i]:
        title = abstract[i].replace("\n", " ")
        ind = i + 1
        while (abstract[ind][1].islower()) or (abstract[ind][0].isdigit()):
            title = title + abstract[ind].replace("\n", " ")
            ind = ind + 1
    if "AB  -" in abstract[i]:
        ab = abstract[i].replace("\n", " ")
        ind = i + 1
        while (abstract[ind][1].islower()) or (abstract[ind][0].isdigit()):
            ab = ab + (abstract[ind].replace("\n", " "))
            ind = ind + 1
        pubmed[title] = ab

final2 = []
for i in pubmed.keys():
    if ("Acinetobacter" in i) or ("A. baumannii" in i) or ("baumannii" in i):
        try:
            x = i.lower()
            x = x.replace("ti  - ", "")
            final2.append(x)
        except:
            print(i)
        continue
    elif ("Acinetobacter" in str(pubmed[i][0])) or ("A. baumannii" in str(pubmed[i][0])) or ("baumannii" in str(pubmed[i][0])):
        try:
            x = i.lower()
            x = x.replace("ti  - ", "")
            final2.append(x)
        except:
            print(i)
        continue
    elif ("Acinetobacter" in str(pubmed[i][1])) or ("A. baumannii" in str(pubmed[i][1])) or ("baumannii" in str(pubmed[i][1])):
        try:
            x = i.lower()
            x = x.replace("ti  - ", "")
            final2.append(x)
        except:
            print(i)
        continue
#**********************************************************************

#Sumarizando títulos
fim = final
for i in final2:
    if i not in fim:
        fim.append(i)
#**********************************************************************

pub = open("pub.txt", 'rt')
pubo = pub.readlines()
pub.close()
x = pubo
pubo = []
for i in x:
    pubo.append(i.lower())

final_ = final
for i in pubo:
    if i not in final_:
        final_.append(i.replace("\n", ""))

out = open("final_articles.txt", "w")
for i in final_:
    out.write(i.capitalize())
    out.write("\n")
out.close()    

