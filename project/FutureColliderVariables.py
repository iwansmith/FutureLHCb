import numpy as np
import math

# Dictionary of Keys for each NTuple/TTree with filename and Tree path

DataTuple = {}
DataTuple["13512010"] = ("root://eoslhcb.cern.ch//eos/lhcb/wg/semileptonic/Bs2KmunuAna/Tuples/Bs2KMuNu_MCTUPLES_RAW_08Feb17/DTT_13512010_Bs_Kmunu_DecProdCut_Up_Py8_MC12.root", "Bs2KMuNuMCTuple/MCDecayTree" )
DataTuple["13512010_combi"] = ("root://eoslhcb.cern.ch//eos/lhcb/wg/semileptonic/Bs2KmunuAna/Tuples/Bs2KMuNu_MCTUPLES_RAW_08Feb17/DTT_13512010_Bs_Kmunu_DecProdCut_Up_Py8_MC12.root", "Bs2KMuNuMCTuple/MCDecayTree" )
DataTuple["13774000_combi"]        = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsMuNu/MCDecayTree") 

DataTuple["11876001"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV11876001.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["12513010"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV12513010.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["15574010"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV15574010.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13114001"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13114001.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13114006"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13114006.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13144032"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13144032.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13146004"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13146004.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["12145052"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV12145052.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["22114001"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV22114001.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["23573002"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV23573002.root", "MCDecayTreeTuple/MCDecayTree")
DataTuple["13774011"] = ("/afs/cern.ch/work/i/ismith/NTuples/VubFromBplus/Backgrounds/GenLevel/DV13774011.root", "MCDecayTreeTuple/MCDecayTree")

DataTuple["13774000_Ds"]        = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsMuNu/MCDecayTree") 
DataTuple["13774000_Dsstar"]    = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStarMuNu_g/MCDecayTree") 
DataTuple["13774000_DsstarTau"] = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStarTauNu_g/MCDecayTree") 
DataTuple["13774000_DsTau"]     = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsTauNu/MCDecayTree") 
DataTuple["13774000_Dsstar0"]   = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStar0MuNu_pi0/MCDecayTree") 
DataTuple["13774000_Dsstar1"]   = ("root://eoslhcb.cern.ch//eos/lhcb/user/i/ismith/MCDecayTree/DTT_MC11_Bs2DsMuNu_13774000_Cocktail_SIGNAL.root", "TupleBs2DsStar12460MuNu_pi0/MCDecayTree") 


# Uncertainty on LHCb Primary and secondary vertices.

sigma_PV_LHCb = np.array( [0.01, 0.01, 0.07])
sigma_SV_LHCb = np.array( [0.02, 0.02, 0.31])


Signal_Yields = {}
Signal_Yields["13512010"] = 17000. # Signal
Signal_Yields["13774000_Dsstar"] = 40000.
Signal_Yields["13774000_Ds"] = 20000.
Signal_Yields["13774000_DsTau"] = 3000
Signal_Yields["13774000_DsstarTau"] = 5000
Signal_Yields["13774000_Dsstar1"] = 1000 
Signal_Yields["13774000_Dsstar0"] = 1000
Signal_Yields["13114006"] = 1000
Signal_Yields["12513010"] = 5000 
Signal_Yields["23573002"] = 1000
Signal_Yields["12145052"] = 5000
Signal_Yields["15574010"] = 2000
Signal_Yields["11876001"] = 1000


Control_Yields = {}
Control_Yields["13774000_Dsstar"] = 4.42e5
Control_Yields["13774000_Ds"] = 1.97e5
Control_Yields["13774000_DsTau"] = 5e3
Control_Yields["13774000_DsstarTau"] = 8e3 
Control_Yields["13774000_Dsstar1"] = 2e4
Control_Yields["13774000_Dsstar0"] = 5e4
Control_Yields["13146004"] = 1000
Control_Yields["11876001"] = 1500 #Double D







