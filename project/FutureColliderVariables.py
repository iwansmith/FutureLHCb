# Uncertainty on LHCb Primary and secondary vertices.
import numpy as np

sigma_PV_LHCb = np.array( [0.01, 0.01, 0.07])
sigma_SV_LHCb = np.array( [0.02, 0.02, 0.31])




# Dictionary of Keys for each NTuple/TTree with filename and Tree path

DataTuple = {}
DataTuple["13512010"] = ("root://eoslhcb.cern.ch//eos/lhcb/wg/semileptonic/Bs2KmunuAna/Tuples/Bs2KMuNu_MCTUPLES_RAW_08Feb17/DTT_13512010_Bs_Kmunu_DecProdCut_Up_Py8_MC12.root", "Bs2KMuNuMCTuple/MCDecayTree" )

DataTuple["12513010"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV12513010.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["15574010"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV15574010.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13144032"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13144032.root", "MCDecayTreeTuple/MCDecayTree")

DataTuple["13774000_Ds"]        = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsMuNu/MCDecayTree") 
DataTuple["13774000_Dsstar"]    = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStarMuNu_g/MCDecayTree") 
DataTuple["13774000_DsstarTau"] = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStarTauNu_g/MCDecayTree") 
DataTuple["13774000_DsTau"]     = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsTauNu/MCDecayTree") 
DataTuple["13774000_Dsstar0"]   = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStar0MuNu_pi0/MCDecayTree") 
DataTuple["13774000_Dsstar1"]   = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStar12460MuNu_pi0/MCDecayTree") 


SourceNames = {}
SourceNames["13512010"] = "B_{s} #rightarrow K^{-} #mu^{+} #nu"
SourceNames["13512010_Combinatorial"] = "Combinatorial"
SourceNames["12513010"] = "B^{+} #rightarrow #phi #mu^{+} #nu"
SourceNames["15574010"] = "#Lambda_{b} #rightarrow #Lambda_{c} #mu^{+} #nu"
SourceNames["13144032"] = "B_{s} #rightarrow J/#psi #phi"

SourceNames["13774000_Ds"]        = "B_{s} #rightarrow D_{s} #mu^{+} #nu"
SourceNames["13774000_Ds_Combinatorial"] = "Combinatorial"
SourceNames["13774000_Dsstar"]    = "B_{s} #rightarrow D_{s}* #mu^{+} #nu"
SourceNames["13774000_DsstarTau"] = "B_{s} #rightarrow D_{s}* #tau^{+} #nu"
SourceNames["13774000_DsTau"]     = "B_{s} #rightarrow D_{s} #tau^{+} #nu"
SourceNames["13774000_Dsstar0"]   = "B_{s} #rightarrow D_{s}*0 #mu^{+} #nu"
SourceNames["13774000_Dsstar1"]   = "B_{s} #rightarrow D_{s}*1 #mu^{+} #nu"

SourceNames["13774000_Tau"] = "B_{s} #rightarrow D_{s} #tau^{+} #nu X"
SourceNames["13774000_Ds01"]   = "B_{s} #rightarrow D_{s}*01 #mu^{+} #nu"
SourceNames["13774000_DsX"] = "B_{s} #rightarrow D_{s}^{(*)} #mu^{+} #nu X"
SourceNames["Combinatorial_K"] = "Combinatorial"
SourceNames["Combinatorial_Ds"] = "Combinatorial"

SourceNames["13774000_DsX_Tau"] = "B_{s} #rightarrow D_{s}^{(*)} #mu^{+}(#tau^+) #nu X"

# Dictionary that merges the histograms

MergeDict_K = {}
#MergeDict_K["13774000_Tau"]  = ["13774000_DsTau", "13774000_DsstarTau"]
MergeDict_K["13774000_Ds01"] = ["13774000_Dsstar0", "13774000_Dsstar1", "15574010"]
MergeDict_K["13774000_DsX_Tau"]   = ["13774000_Ds", "13774000_Dsstar","13774000_DsTau", "13774000_DsstarTau"]
MergeDict_K["Combinatorial_K"] = ["13774000_Ds_Combinatorial", "13512010_Combinatorial"]
MergeDict_K["12513010"] = ["12513010"]
MergeDict_K["13512010"] = ["13512010"]

MergeDict_Ds = {}
MergeDict_Ds["13774000_Tau"]  = ["13774000_DsTau", "13774000_DsstarTau"]
MergeDict_Ds["13774000_Ds01"] = ["13774000_Dsstar0", "13774000_Dsstar1"]
MergeDict_Ds["13774000_Ds"]  = ["13774000_Ds"]
MergeDict_Ds["13774000_Dsstar"]  = ["13774000_Dsstar"] 
MergeDict_Ds["Combinatorial_Ds"]  = ["13774000_Ds_Combinatorial"]



Signal_Yields = {}
#Signal_Yields["13774000_Tau"] = 10000. # Signal
Signal_Yields["13774000_Ds01"] = 15000. # Signal
Signal_Yields["13774000_DsX_Tau"] = 70000.
Signal_Yields["Combinatorial_K"] = 10000.
Signal_Yields["12513010"] = 10000
Signal_Yields["13512010"] = 20000


Control_Yields = {}
Control_Yields["13774000_Tau"] = 20000
Control_Yields["13774000_Ds01"] = 40000
Control_Yields["13774000_Ds"] = 200000
Control_Yields["13774000_Dsstar"] = 400000
Control_Yields["Combinatorial_Ds"] = 30000


MonteCarloYields = {}
MonteCarloYields["Combinatorial_K"] = 20000.
MonteCarloYields["12513010"] = 5000.
MonteCarloYields["13512010"] = 17000.
MonteCarloYields["13774000_DsX_Tau"] = 80000.

MonteCarloYields["Combinatorial_Ds"] = 20000.
MonteCarloYields["13774000_Ds"] = 20000.
MonteCarloYields["13774000_Dsstar"] = 40000.
MonteCarloYields["13774000_Tau"] = 5000. # Signal
MonteCarloYields["13774000_Ds01"] = 15000. # Signal






