# -*- coding: utf-8 -*-
"""
例子：
>TRIAE_CS42_7AL_TGACv1_556641_AA1767760.1 pep scaffold:TGACv1:TGACv1_scaffold_556641_7AL:12602:13765:-1 gene:TRIAE_CS42_7AL_TGACv1_556641_AA1767760 transcript:TRIAE_CS42_7AL_TGACv1_556641_AA1767760.1 gene_biotype:protein_coding transcript_biotype:protein_coding
MSCFAVPVRTSSSSSRISGSRQPWRWWRKCAGLAAAAHTKLRRTALRVRWSATGRLGGHR
RRAPAPPLLSVQRGDHMSFAPVYVDELYSQPKGLSVVHEEQQPQPSTSKLARPAGSVNKA
RVHGVAAATGGNKACAAAAAAKSLGVRGFLLSPGRGCVGMGEVDVRAEMFIRKFREEMRL
QSQRSAEELQAMLARGL
>TRIAE_CS42_1BL_TGACv1_031356_AA0112250.1 pep scaffold:TGACv1:TGACv1_scaffold_031356_1BL:10276:13109:1 gene:TRIAE_CS42_1BL_TGACv1_031356_AA0112250 transcript:TRIAE_CS42_1BL_TGACv1_031356_AA0112250.1 gene_biotype:protein_coding transcript_biotype:protein_coding
MDAKKRSPPAPSAAGAAPPAANGYFSSVFSAPASPAANPRDARQMDLYTILNKQNPKGLS
GGGIADAKSQGNPTNGRVAYKDGKQFYPNESSESPYFGSSVHYGGRDFYDSSPHKQADES
SRNYKEDNADGSLATRGDWWQGSLYY

使用说明：设置完下述参数后，将该文件与被挑选序列的源文件放在一起，双击该文件即可
参数说明：需要设置的参数总共有四个，分别是target，maker，inputfile，outputfile，下面分别说明该参数的意义，以及设置方法。所有需要更改的参数只要更改单引号里面的内容就行了

target： 
    指需要挑选的序列与其他序列不同的地方，例如，需要挑选的序列为1BL的，则可设置target='TRIAE_CS42_1BL'，设置为'1BL'也可以，但最好稍微长一点

maker： 	
	指用来区分一段序列开始的连续字母，例如，在这里每一段开头都有>TRIAE，则可设置maker='>TRIAE'

inputfile： 
	指被挑选序列的源文件，例如什么什么300S.fa，源文件的后缀名也需要加上

outputfile：
	指输出文件的名字，这个可以随便起，但是记得加上后缀

"""

import sys

#-------------需要设置的参数----------
target='TRIAE_CS42_1BL'
maker='>TRIAE'
inputfile='input.txt'
outputfile='111.txt'
#-------------------------------------

path=sys.path[0]
f = open(path+'\\'+inputfile,"r")
f1 = open(path+'\\'+outputfile,"w")
line = f.readline()

while line:
    if line.find(target)!=-1:
        
        f1.write(line)
        line = f.readline()

        while line.find(maker)==-1 and line:
            f1.write(line)
            line = f.readline()
        continue
    
    line= f.readline()
    

f.close
f1.close
