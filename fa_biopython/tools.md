## seqkit
https://bioinf.shenwei.me/seqkit/download/
https://github.com/shenwei356/seqkit/releases/download/v2.1.0/seqkit_linux_amd64.tar.gz
解压即可，无需安装


#### seqkit拆分文件（fa/fa.gz)
```bash
seqkit split -s 1000 origin.fa # 每个子文件固定序列数目
seqkit split -p 5 origin.fa    # 固定子文件数目，每个子文件数目均衡
```

#### 合并多个fasta文件
```bash
cat *.fa >total.fa
zcat *.fa.gz >total.fa
```

