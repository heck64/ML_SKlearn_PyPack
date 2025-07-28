import numpy
import ROOT
import sys
from ROOT import RDataFrame


def RATIO_Creator(File,Variable,LowBound,UpBound):
    f=ROOT.TFile.Open(str(File))
    tree =f.Get("ROOTOutput")
    total=tree.GetEntries()
    df = ROOT.RDataFrame("ROOTOutput", File)
    df =df.Filter(f"{Variable} < {UpBound}")
    df =df.Filter(f"{Variable} > {LowBound}")
    hist=df.Histo1D(("Woah", "Please", 100, -5, 5), str(Variable))
    withcut=hist.GetEntries()
    ratio = withcut/total
    ratio = round(ratio,3)
    return ratio


def Distribution_Values(File,Variable):
    f=ROOT.TFile.Open(str(File))
    tree = f.Get("ROOTOutput")
    df = ROOT.RDataFrame("ROOTOutput", File)
    stdev=df.StdDev(Variable).GetValue()
    meanval=df.Mean(Variable).GetValue()
    return stdev, meanval

def NumberLeft(File):
    f=ROOT.TFile.Open(str(File))
    tree = f.Get("ROOTOutput")
    total=tree.GetEntries()
    return total

