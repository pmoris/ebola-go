#!/usr/bin/env python

# http://biopython.org/DIST/docs/tutorial/Tutorial.html

import sys,csv, time
from Bio import Entrez

Entrez.email = 'pieter.moris@uantwerpen.be'

with open(sys.argv[1],'r') as f:
    taxIDlist = [line.rstrip() for line in f]

with open(sys.argv[2],'w') as o:
    writer = csv.writer(o,lineterminator='\n',delimiter='\t')
    writer.writerow(['Taxonomy ID','Scientific Name'])

    for id in taxIDlist:
        time.sleep(0.5)
        handle = Entrez.efetch(db="Taxonomy", id = id)
        records = Entrez.read(handle)
        writer.writerow([id, records[0]['ScientificName'].rstrip()])
