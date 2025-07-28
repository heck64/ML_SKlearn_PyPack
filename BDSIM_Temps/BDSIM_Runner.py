#Imports for file
#Template is a way to work through outputs
import matplotlib.pyplot as plt
from string import Template as Tem 
import numpy as np
import subprocess
from ROOT_Loader import *
from multiprocessing import Process

# def _writetxt(variable1,variable2,variable3, outputtxt,template):
#     with open(template, "r+") as f:
#         contents = f.read()
#     template = Tem(contents)
#     template_resolved = template.safe_substitute(MagStrengthGrad = variable1, DistanceBetween=variable2, filename=variable3)
#     with open(outputtxt, "w") as f: #Open in Writing Mode
#         f.write(template_resolved)


class BDSIM_RUNNER:
    def __init__(self, DataSetFileName, LabelFileName, MagRange, DistRange):
        self.DataSet=DataSetFileName
        self.Labels =LabelFileName
        self.MagStrengthGrad = MagRange
        self.DistanceBetween = DistRange
    
    def Dictionary(self,i,a,b,c,d,file,e=None,h=None,j=None,k=None,l=None,m=None,n=None,o=None,**kwargs):
        if i==2:
            multivardic=dict(OneMagStrengthGrad=a,OneMagStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagStrengthGrad=d,TwoMagStrengthGrad=-1*d,filename=file)
        elif i==3:
            multivardic=dict(OneMagStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h)
        elif i==4:
           multivardic=dict(OneMagStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
                    TwoDistanceBetween= c , TwoMagXStrengthGrad=d,TwoMagYStrengthGrad=-1*d,filename=file,
                    ThreeDistanceBetween= e,ThreeMagYStrengthGrad=-1*h, ThreeMagXStrengthGrad=h,
                    FourDistanceBetween=  j, FourMagXStrengthGrad= k,FourMagYStrengthGrad= -1*k)
        elif i==5:
            multivardic=dict(OneMagStrengthGrad=a,OneMagYStrengthGrad=-1*a, OneDistanceBetween= b, 
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
     

    def Two_Quad_BDSIM(self):
        template2 = "2_Quad_Temp.txt"
        i=2
        sub = [OneMagStrengthGrad, OneDistanceBetween, 
                TwoDistanceBetween , TwoMagStrengthGrad]
        BDSIM_RUNNER.BDSIM_TEMP_Changer(self,i,template2)
        BDSIM_RUNNER.BDSIM_AUTO_RUNNER(self,i)
        

    def Three_Quad_BDSIM(self):
        template3 = "Templates/3_Quad_BDSIM_Template.txt"
        i=3
        sub = [OneMagStrengthGrad, OneDistanceBetween, 
                TwoDistanceBetween , TwoMagStrengthGrad,
                ThreeDistanceBetween, ThreeMagStrengthGrad]
        BDSIM_RUNNER.BDSIM_TEMP_Changer(self,i,template3)
        BDSIM_RUNNER.BDSIM_AUTO_RUNNER(self,i)

    def Four_Quad_BDSIM(self):
        template4 = "Templates/4_Quad_BDSIM_Template.txt"
        i=4
        sub = [OneMagStrengthGrad,OneDistanceBetween, 
                    TwoDistanceBetween , TwoMagStrengthGrad,
                    ThreeDistanceBetween, ThreeMagStrengthGrad,
                    FourDistanceBetween, FourMagStrengthGrad]
        BDSIM_RUNNER.BDSIM_TEMP_Changer(self,i,template4)
        BDSIM_RUNNER.BDSIM_AUTO_RUNNER(self,i)

    def Five_Quad_BDSIM(self):
        template5 = "Templates/5_Quad_BDSIM_Template.txt"
        i=5
        sub = {OneMagStrengthGrad, OneDistanceBetween, 
                    TwoDistanceBetween , TwoMagStrengthGrad,
                    ThreeDistanceBetween, ThreeMagStrengthGrad,
                    FourDistanceBetween, FourMagStrengthGrad,
                    FiveDistanceBetween, FiveMagStrengthGrad}
        BDSIM_RUNNER.BDSIM_TEMP_Changer(self,i,template5)
        BDSIM_RUNNER.BDSIM_AUTO_RUNNER(self,i)
        
    def Six_Quad_BDSIM(self):
        template6 = "Templates/6_Quad_BDSIM_Template.txt"
        i=6  
        sub = {OneMagStrengthGrad, OneDistanceBetween, 
                    TwoDistanceBetween , TwoMagStrengthGrad,
                    ThreeDistanceBetween, ThreeMagStrengthGrad,
                    FourDistanceBetween, FourMagStrengthGrad,
                    FiveDistanceBetween, FiveMagStrengthGrad,
                    SixDistanceBetween, SixMagStrengthGrad}
        BDSIM_RUNNER.BDSIM_TEMP_Changer(self,template6)
        BDSIM_RUNNER.BDSIM_AUTO_RUNNER(self,i)

    def _writetxt(self, outputtxt,template,i,subint):
        with open(template, "r+") as f:
            contents = f.read()
        template = Tem(contents)
        template_resolved = template.safe_substitute(subint)
        with open(outputtxt, "w") as f: #Open in Writing Mode
            f.write(template_resolved)

    def BDSIM_TEMP_Changer(self,template,i,sub):   
        for quadno in range(i):
            for k in self.MagStrengthGrad:
                pardict1 = {"self.MagStrengthGrad": str(k)}
                for d in self.DistanceBetween:
                    pardict2 = {"self.DistanceBetween": str(d)}
                    txtFile = f"{i}_Quad_{k}_{d}.txt"
                    rootfile = f"{i}_Quad_{k}_{d}.root"
                    BDSIM_RUNNER._writetxt(self,i=i, outputtxt=txtFile, template=template, sub)
                    
    def BDSIM_AUTO_RUNNER(self, i):
        for k in self.MagStrengthGrad:
            for d in self.DistanceBetween:
                txtFile = f"{i}_Quad_{k}_{d}.txt"
                rootfile = f"{i}_Quad_{k}_{d}.root"               
                subprocess.run(["/Applications/BDSIM/bin/BDSIM", str(txtFile)])
                posxstd,posxmean =Distribution_Values(rootfile,"Position_X__cm_")
                posystd, posymean=Distribution_Values(rootfile,"Position_Y__cm_")
                cosxstd, cosxmean=Distribution_Values(rootfile,"Direction_Cosine_X")
                cosystd, cosymean=Distribution_Values(rootfile,"Direction_Cosine_Y")
                array=f"{posxstd} {posxmean} {posystd} {posymean} {cosxstd} {cosxmean} {cosystd} {cosymean}"
                label=f"{i} {k} {d}"
                t =open(self.DataSet, "a")
                t.write(array + "\n")
                t.close()
                l =open(self.Labels,"a")
                l.write(label + "\n")
                l.close()

### Dictionary Generation

#if __name__ == "__main__":
#    TOP_SET=BDSIM_RUNNER("DataSet_Class_Run.txt","LabelSet_Class_Run.txt", np.linspace(0.01, 0.2, 2),np.linspace(10,100,2, dtype = int))
#    p1 = Process(target=TOP_SET.Two_Quad_BDSIM())
#    p1.start()
#    p2 = Process(target=TOP_SET.Three_Quad_BDSIM())
#    p2.start()
#    p1.join()
#    p2.join()

TOP_SET=BDSIM_RUNNER("DataSet_Class_Run.txt","LabelSet_Class_Run.txt", np.linspace(0.0, 0.0, 1),np.linspace(10,100,1, dtype = int))
TOP_SET.Four_Quad_BDSIM()



#All the Templated Variables in BDSIM Files
#$filename

#$OneXMagStrengthGrad
#$OneYMagStrengthGrad
#$OneDistanceBetween

#$TwoDistanceBetween
#$TwoXMagStrengthGrad
#$TwoYMagStrengthGrad

#$ThreeDistanceBetween
#$ThreeXMagStrengthGrad
#$ThreeYMagStrengthGrad

#$FourDistanceBetween
#$FourXMagStrengthGrad
#$FourYMagStrengthGrad

#$FiveDistanceBetween
#$FiveXMagStrengthGrad
#$FiveYMagStrengthGrad

#$SixDistanceBetween
#$SixXMagStrengthGrad
#$SixYMagStrengthGrad

