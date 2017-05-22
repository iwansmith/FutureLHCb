import sys
sys.path.append('../../FourVector')
sys.path.append('../project')

from FourVector import FourVector
from ThreeVector import ThreeVector

from FutureColliderTools import SmearVertex, GetCorrectedMass, GetMissingMass2, GetQ2, SaveHistogram
from FutureColliderDataLoader import SaveHistogram_KMuNu, SaveHistogram_DsMuNu
from FutureColliderVariables import *
from FutureColliderFitter import *

import numpy as np
import ROOT


from prettytable import PrettyTable

Yields = {}
Errors = {}
FracErr = {}

Yields["K"]   = []
Yields["Ds"]  = []
Errors["K"]   = []
Errors["Ds"]  = []
FracErr["K"]  = []
FracErr["Ds"] = []

ResultTables = {}
ResultTables["K"]  = PrettyTable()
ResultTables["Ds"] = PrettyTable()
ResultTables["K"]. field_names = ["Vertex Error / LHCb", "Signal Fraction", "Error [%]"]
ResultTables["Ds"].field_names = ["Vertex Error / LHCb", "Signal Fraction", "Error [%]"]


file_plot = ROOT.TFile.Open("../output/FitterOutput.root", "RECREATE")


for Mode in ["K", "Ds"]:
	for resolution in np.linspace(0.0, 1.0, 11):

		Fitter = FutureFitter("../output/Data_Histograms_{0}_LHCb.root".format(resolution), "MCORR_Data_{0}MuNu".format(Mode),  "../output/Source_Histograms_{0}Mu_{1}_LHCb_Merged.root".format(Mode, resolution), Mode == "K")
		status = Fitter.Fit()

		FitYields = Fitter.GetYield()

		Yield = 0
		Error = 0
		try:
			Yield = FitYields["13512010"][0]
			Error = FitYields["13512010"][1]
		except:
			Yield = FitYields["13774000_Ds"][0]
			Error = FitYields["13774000_Ds"][1]

		print "Signal Yield:", Yield, "+/-", Error

		Yields[Mode] += [Yield]
		Errors[Mode] += [Error]
		FracErr[Mode] += [100 * Error/Yield ]

		canvas = ROOT.TCanvas("c_Fit_{mode}_{resolution}".format(mode = Mode, resolution = resolution), "canvas", 900, 900)

		Fitter.Plot(canvas)

		file_plot.cd()

		canvas.Write()

		ResultTables[Mode].add_row(( resolution, Yield, 100 * Error/Yield  ) )

		del Fitter

Graphs = {}

Graphs["K"]  = ROOT.TGraph(11, np.linspace(0.0, 1.0, 11),  np.asarray( FracErr["K"] ) )
Graphs["Ds"] = ROOT.TGraph(11, np.linspace(0.0, 1.0, 11),  np.asarray( FracErr["Ds"]) )


for key, graph in Graphs.iteritems():
	graph.SetTitle("")
	graph.SetName("Error_Budget_{Mode}".format(Mode=key))
	graph.GetXaxis().SetTitle("Vertex precision / LHCb Vertex precision")
	graph.GetYaxis().SetTitle("Signal Yield Uncertainty [%]")
	graph.SetMaximum(10.0)
	graph.Write()


file_plot.Close()

for i in range(9):
	print "K: ", Yields["K"][i], Errors["K"][i], "Ds: ", Yields["Ds"][i], Errors["Ds"][i]

import dill
import pickle
print ResultTables["K"]
print ResultTables["Ds"]

pickle.dump( ResultTables, open("../output/FitResults.p", "wb"))