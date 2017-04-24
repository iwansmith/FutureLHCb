import sys
sys.path.append('../../FourVector')
sys.path.append('../project')

from FourVector import FourVector
from ThreeVector import ThreeVector

from FutureColliderTools import SmearVertex, GetCorrectedMass, GetMissingMass2, GetQ2, SaveHistogram
from FutureColliderDataLoader import SaveHistogram_KMuNu, SaveHistogram_DsMuNu
from FutureColliderVariables import *


import numpy as np
import ROOT
"""
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
	
"""

# Now Merge similar shapes

HistTypes = ["MCORR", "MissingMass2", "QSQ_SOL1", "QSQ_SOL2", "QSQ_SOLTrue"]

for resolution in np.linspace(0.0, 1.0, 11):


	def MergeHistograms( Dictionary ):
		for HistName, Components in Dictionary.iteritems():
			for Type in HistTypes:
				print Type + "_" + Components[0]
				Merged = f_Histogram.Get(Type + "_" + Components[0] ).Clone()
				Merged.SetDirectory(0)
				Merged.Reset()
				Merged.SetName( Type + "_" + HistName )
				Merged.SetTitle(SourceNames[HistName])

				for Hist in Components:
					#print Type + "_" + Hist 
					Merged += f_Histogram.Get(Type + "_" + Hist ).Clone()

				Merged.Scale( MonteCarloYields[ HistName ] /  Merged.Integral() )
				Merged.Sumw2(False)
				Merged.Sumw2()
				SaveHistogram(f_Histogram_Out, Merged )

	f_Histogram     = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb.root".format(resolution), "READ")
	f_Histogram_Out = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb_Merged.root".format(resolution), "RECREATE")
	MergeHistograms( MergeDict_Ds )

	f_Histogram     = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb.root".format(resolution), "READ")
	f_Histogram_Out = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb_Merged.root".format(resolution), "RECREATE")
	MergeHistograms( MergeDict_K )




# Now generat the PseudoData Histograms
for resolution in np.linspace(0.0, 1.0, 11):

	from FutureColliderVariables import Signal_Yields, Control_Yields

	def MakeFakeData():
		for hname, Yield in ToyYields.iteritems():
		    temphist = ToyFile.Get("MCORR_" + hname)

		    print temphist, "MCORR_" + hname
		    for ev in xrange(int(Yield)):
		        MCORR = temphist.GetRandom()
		        h_MCORR.Fill(MCORR)

	DataFile = ROOT.TFile.Open("../output/Data_Histograms_{0}_LHCb.root".format(resolution), "RECREATE")


	ToyYields = Signal_Yields
	ToyFile = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb_Merged.root".format(resolution), "READ")
	h_MCORR = ROOT.TH1F("MCORR_Data_KMuNu", "", 100, 2500, 6000)
	MakeFakeData()
	DataFile.cd()
	h_MCORR.Write()

	ToyYields = Control_Yields
	ToyFile = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb_Merged.root".format(resolution), "READ")
	h_MCORR = ROOT.TH1F("MCORR_Data_DsMuNu", "", 100, 2500, 6000)
	MakeFakeData()
	DataFile.cd()
	h_MCORR.Write()
	
	DataFile.Close()
