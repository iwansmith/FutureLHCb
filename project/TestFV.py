import ROOT
import numpy as np
from FourVector import *

from root_numpy import root2array


InputData = root2array( "root://eoslhcb.cern.ch//eos/lhcb/wg/semileptonic/Bs2KmunuAna/Tuples/Bs2KMuNu_MCTUPLES_TRIMMED_30May16/DTT_13512010_Bs_Kmunu_DecProdCut_Up_Py8_MC12_trimmed.root",
	treename = "reducedTree",
	branches = ["Bs_PE", "Bs_PX", "Bs_PY", "Bs_PZ", "kaon_m_PX", "kaon_m_PY", "kaon_m_PZ", "muon_p_PX", "muon_p_PY", "muon_p_PZ", "Bs_ENDVERTEX_X", "Bs_ENDVERTEX_Y", "Bs_ENDVERTEX_Z", "Bs_OWNPV_X", "Bs_OWNPV_Y", "Bs_OWNPV_Z", "Bs_MCORR"]
	)

atype = InputData["Bs_ENDVERTEX_X"].dtype
B_End  = InputData[["Bs_ENDVERTEX_X", "Bs_ENDVERTEX_Y", "Bs_ENDVERTEX_Z"]].copy().view(( atype, 3 ))
B_Start = InputData[["Bs_OWNPV_X", "Bs_OWNPV_Y", "Bs_OWNPV_Z"]].copy().view(( atype, 3 ))
 
B_Dirn = ThreeVector( B_End - B_Start )

K = FourVector()
K.SetXYZM( InputData[["kaon_m_PX", "kaon_m_PY", "kaon_m_PZ"]],  493.677 )
Mu = FourVector()
Mu.SetXYZM( InputData[["muon_p_PX", "muon_p_PY", "muon_p_PZ"]],  105.6583 )

Bs = K + Mu
 
Y_M = Bs.M()
Y_PT = Bs.Perp( B_Dirn )

Bs_MCORR = np.sqrt( np.square( Y_M ) + np.square( Y_PT ) ) + Y_PT

print Bs_MCORR

Bs_M = Bs.M()



h1 = ROOT.TH1F("h1", "h1", 100, 2000, 6000)
h2 = ROOT.TH1F("h2", "h2", 100, 2000, 6000)
h2.SetLineColor(2)

c = ROOT.TCanvas("c1", "c1", 1600, 1600)

for v1, v2 in zip( Bs_MCORR, InputData["Bs_MCORR"] ):
	h1.Fill(v1)
	h2.Fill(v2)
h1.Draw()
h2.Draw("SAME")
c.Print ("Bs_M.pdf")

print Bs_M
