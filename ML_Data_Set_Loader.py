import numpy as np
#dataset_extracted=[]
#data =np.genfromtxt("DataSet5.txt", delimiter=" ", usecols=np.arange(2))
#labels =np.genfromtxt("LabelSet5.txt", delimiter=" ", usecols=np.arange(3))

#print(data)
#print(labels)

def DataLoader(Datafile,LabelFile,DatAm,LabAm):
    data =np.genfromtxt(Datafile, delimiter=" ", usecols=np.arange(DatAm))
    labels =np.genfromtxt(LabelFile, delimiter=" ", usecols=np.arange(LabAm))
    return data, labels



####test
#x=[[0.9519230769230769, 0.875],[0.9423076923076923, 0.875],[0.9615384615384616, 0.9230769230769231],[0.9807692307692307, 0.9615384615384616],[0.9807692307692307, 0.9903846153846154],[1.0, 1.0],[0.9803921568627451, 0.9901960784313726],[0.898989898989899, 0.8585858585858586]]
#y=[[2, 0.01, 180],[2, 0.01, 225],[2, 0.105, 180],[2, 0.105, 225],[2, 0.105, 270],[2, 0.2, 180],[2, 0.2, 225],[2, 0.2, 270]]
