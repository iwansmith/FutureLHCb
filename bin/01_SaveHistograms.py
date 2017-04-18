import sys
sys.path.append('../../FourVector')
sys.path.append('../project')

from FourVector import FourVector
from ThreeVector import ThreeVector

from FutureColliderTools import SmearVertex, GetCorrectedMass, GetMissingMass2, GetQ2
from FutureColliderDataLoader import SaveHistogram_KMuNu, SaveHistogram_DsMuNu


import numpy as np
import ROOT

# Loop over every resolution .
for resolution in np.linspace(0.0, 1.0, 11):

	# Generate an empty root file where the histograms will be saved
	
	f_Histogram = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb.root".format(resolution), "RECREATE")
	f_Histogram.Close()
	f_Histogram = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb.root".format(resolution), "RECREATE")
	f_Histogram.Close()
	
	from FutureColliderVariables import DataTuple
	
	for EvType, FileTree in DataTuple.iteritems():
	    SaveHistogram_KMuNu ( EvType, FileTree, resolution = resolution, combinatorial = False )
	    SaveHistogram_DsMuNu( EvType, FileTree, resolution = resolution, combinatorial = False )

	# Save some combinatorial samples. This moves the kaon, end vertex to the next event so half of one event is combined with another.
	SaveHistogram_KMuNu ("13512010", DataTuple["13512010"], resolution = resolution, combinatorial = True )
	SaveHistogram_KMuNu ("13774000_Ds", DataTuple["13774000_Ds"], resolution = resolution, combinatorial = True )
	SaveHistogram_DsMuNu("13774000_Ds", DataTuple["13774000_Ds"], resolution = resolution, combinatorial = True )
	
	# Save the PseudoData Histogram
	DataFile = ROOT.TFile.Open("../output/Data_Histograms_{0}_LHCb.root".format(resolution), "RECREATE")
	SignalFile = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb.root".format(resolution), "READ")
	ControlFile = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb.root".format(resolution), "READ")
	
	h_MCORR = ROOT.TH1F("MCORR_Data_KMuNu", "", 100, 2500, 6000)

	from FutureColliderVariables import Signal_Yields
	for hname, Yield in Signal_Yields.iteritems():
	    temphist = SignalFile.Get("MCORR_" + hname)
	    #print temphist
	    for ev in xrange(int(Yield)):
	        MCORR = temphist.GetRandom()
	        h_MCORR.Fill(MCORR)
	        
	DataFile.cd()
	h_MCORR.Write()

	h_MCORR = ROOT.TH1F("MCORR_Data_DsMuNu", "", 100, 2500, 6000)

	from FutureColliderVariables import Control_Yields
	for hname, Yield in Control_Yields.iteritems():
	    temphist = ControlFile.Get("MCORR_" + hname)
	    #print temphist, hname
	    for ev in xrange(int(Yield)):
	        MCORR = temphist.GetRandom()
	        h_MCORR.Fill(MCORR)
	        
	DataFile.cd()
	h_MCORR.Write()

	DataFile.Close()
