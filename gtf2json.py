#!/usr/bin/python
import re
import json

file = open('/home/boc/data/Ho.txt',"r")
GRCh3775_dic_list = []
for line in file:
    match_obj = re.search(r'(.*)\t(.*)\t(.*)\t(\d+)\t(\d+)\t(.*)\t(.*)gene_name\s\"(.*?)\"\;', line)
    if match_obj.group(3) == 'gene':
        GRCh3775_dic = {}
        gene_name = match_obj.group(8)
        chromosome = match_obj.group(1)
        starting_position = match_obj.group(4)
        ending_position = match_obj.group(5)
        GRCh3775_dic["geneName"] = gene_name
        GRCh3775_dic["chr"] = chromosome
        GRCh3775_dic["startPos"] = starting_position
        GRCh3775_dic["endPos"] = ending_position
        GRCh3775_dic_list.append(GRCh3775_dic)
    else:
        continue
with open("output.json", "w") as outfile:
    json.dump(GRCh3775_dic_list, outfile)
