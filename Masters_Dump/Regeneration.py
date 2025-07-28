import numpy as np
import subprocess
from string import Template as Tem
from array import array

a="2 0.021052631578947323 0.27368421052631575 10 10 0 0 0 0 0 0 0 0"
b="2 0.10526315789473684 0.18947368421052624 10 10 0 0 0 0 0 0 0 0"
# python string replace space with comma
newload= a.replace(' ', ',')
bnewload=b.replace(' ',',') 
print(newload)


def _writetxt( outputtxt,template,i,sub):
        with open(template, "r+") as f:
            contents = f.read()
        template = Tem(contents)
        template_resolved = template.safe_substitute(sub)
        with open(outputtxt, "w") as f: #Open in Writing Mode
            f.write(template_resolved)

def Dictionary(i,a,b,c,d,file,e=None,h=None,j=None,k=None,l=None,m=None,n=None,o=None,**kwargs):
        if i==2:
            multivardic=dict(OneMagXStrengthGrad=a,OneMagYStrengthGrad=-1*float(a), OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*float(d),filename=file)
        elif i==3:
            multivardic=dict(OneMagXStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h)
        elif i==4:
           multivardic=dict(OneMagXStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h,
                    FourDistanceBetween=  j, FourMagXStrengthGrad= k,FourMagYStrengthGrad= -1*k)
        elif i==5:
            multivardic=dict(OneMagXStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h,
                    FourDistanceBetween=  j, FourMagXStrengthGrad= k,FourMagYStrengthGrad= -1*k,
                    FiveDistanceBetween=  l, FiveMagXStrengthGrad= m,FiveMagYStrengthGrad=-1*m)
        elif i==6:
            multivardic=dict(OneMagXStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h,
                    FourDistanceBetween=  j, FourMagXStrengthGrad= k,FourMagYStrengthGrad= -1*k,
                    FiveDistanceBetween=  l, FiveMagXStrengthGrad= m,FiveMagYStrengthGrad=-1*m,
                    SixDistanceBetween=n, SixMagXStrengthGrad=o,SixMagYStrengthGrad=-1*o)
        return multivardic




def extract_vals(labelset,i=2):
    va_=labelset
    vars_=va_.split(',')
    #i=vars_[0]
    a=vars_[1]
    d=vars_[2]
    b=vars_[3]
    c=vars_[4]
    e=vars_[5]
    h=vars_[6]
    k=vars_[7]
    j=vars_[8]
    m=vars_[9]
    l=vars_[10]
    n=vars_[11]
    o=vars_[12]
    i==2
    print(i,a,d,b,c)
    template2 = "Templates/2_Quad_TOPAS_Template.txt"
    txtFile = f"{i}_Quad_{a}_{d}_Mag_{b}_{c}_Dist_REGEN.txt"
    rootfile = f"{i}_Quad_{a}_{d}_Mag_{b}_{c}_Dist_REGEN.root"
    sub_vals =Dictionary(i,a,b,c,d,file=rootfile)
    _writetxt(i=i, outputtxt=txtFile, template=template2,sub=sub_vals)
    subprocess.run(["/Applications/topas/bin/topas", str(txtFile)])
    #label=f"{i} {a} {d} {b} {c} {e} {h} {k} {j} {m} {l} {n} {o}"

#extract_vals(newload)
extract_vals(bnewload)
