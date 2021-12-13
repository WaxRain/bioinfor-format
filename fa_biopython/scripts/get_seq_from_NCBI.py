#!/usr/bin/python
# coding: utf-8
import os
from Bio import Entrez, SeqIO
Entrez.email = 'haoyucomeon@163.com'   # 必须由此参数，告诉NCBI你是谁
script_folder = os.path.dirname(__file__)


def get_fasta(acc, desc=None, output=None):
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="fasta")
    record = SeqIO.read(handle, 'fasta')
    record.description = desc if desc else record.description
    fw = open(output or "%s.fa" % acc, 'w')    
    SeqIO.write(record, fw, 'fasta')
    fw.close()


def get_genbank(acc, output=None):
    handle = Entrez.efetch(db="nucleotide", id=acc, rettype="gb", retmode='text')
    fw = open(output or '%s.gb' % acc, 'w')
    fw.write(handle.read())
    fw.close()
    handle.close()


if __name__ == '__main__':
    acc = '186972394'
    get_fasta(acc, output=os.path.join(script_folder, '../testdata/test.fa'))
    get_genbank(acc, output=os.path.join(script_folder, '../testdata/test.gb'))
