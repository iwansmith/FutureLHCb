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


Yields = {}
Errors = {}

Yields["K"] = []
Yields["Ds"] = []
Errors["K"] = []
Errors["Ds"] = []



for Mode in ["K", "Ds"]:
	for resolution in np.linspace(0.0, 1.0, 11):

		Fitter = FutureFitter("../output/Data_Histograms_{0}_LHCb.root".format(resolution), "MCORR_Data_{0}MuNu".format(Mode),  "../output/Source_Histograms_{0}Mu_0.3_LHCb_Merged.root".format(Mode, resolution))
		Fitter.Fit()


		Yields = Fitter.GetYield()

		Yield = 0
		Error = 0
		try:
			Yield = Yields["13512010"][0]
			Error = Yields["13512010"][1]
		except:
			Yield = Yields["13774000_Ds"][0]
			Error = Yields["13774000_Ds"][1]

		print "Signal Yield:", Yield, "+/-", Error

		del Fitter

