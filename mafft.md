# MAFFT 
https://mafft.cbrc.jp/alignment/software/source.html

## 下载地址
https://mafft.cbrc.jp/alignment/software/mafft-7.490-without-extensions-src.tgz

#### 高度相似序列比对（如相似度>99%)
为节省时间，提供一个参考序列，其他序列均与此参考序列比对。
```bash
mafft --auto --threads 24 --addfragments ../primer_search/kept_genomes.fa ../ref/NC_045512.2.fasta >aligned.mafft_auto.fa
```
