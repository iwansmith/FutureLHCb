from FourVector import *
from FutureColliderTools import *
from FutureColliderVariables import *
import numpy as np


class FutureFitter:



	def __init__(self, DataFile, DataHistogram, TemplateFile):

		InDataFile = ROOT.TFile.Open(DataFile, "READ")
		self.DataHist = InDataFile.Get( DataHistogram ).Clone()
		self.DataHist.SetDirectory(0)
		self.DataHist.SetMinimum(0)
		InDataFile.Close()

		InTemplateFile = ROOT.TFile.Open(TemplateFile, "READ")
		
		KeyList = [ Key for Key in InTemplateFile.GetListOfKeys() if "MCORR" in Key.GetName() ]
		self.TemplateHist = [ Key.ReadObj().Clone() for Key in KeyList if "_norm" not in Key.GetName()]

		self.nPar = len(self.TemplateHist)

		self.TemplateList = ROOT.TObjArray( self.nPar )
		for Hist in self.TemplateHist:
			Hist.SetDirectory(0)
			#Hist.Scale( 0.5 * self.DataHist.Integral() / Hist.Integral() )
			self.TemplateList.Add( Hist )
		InTemplateFile.Close()
		
		self.fitter = ROOT.TFractionFitter(self.DataHist, self.TemplateList)

		for par in range(self.nPar):
			self.fitter.Constrain(par, 0., 10)


	def Fit( self ):

		status = int(self.fitter.Fit())
		Total_Data = self.DataHist.Integral()
		Total_Histogram = 0

		value = np.ones(1)
		error = np.ones(1)
		for par in range(self.nPar):
			self.fitter.GetResult(par, value, error)
			Total_Histogram += self.TemplateHist[par].Integral() * value

		self.ScaledTemplates = []
		self.OutHists = []

		for par in range(self.nPar):
			self.fitter.GetResult(par, value, error)
			Hist = self.TemplateHist[par].Clone()
			Hist.Scale( value * Total_Data / Hist.Integral())
			self.ScaledTemplates += [ Hist ]


			OutHist = self.fitter.GetMCPrediction(par).Clone()
			OutHist.Scale(value * self.DataHist.Integral() / OutHist.Integral() )
			OutHist.SetLineColor(par+1)
			OutHist.Sumw2()
			self.OutHists += [OutHist]

		#self.status = status
		return status

	def Plot( self, canvas):

		canvas.cd()

		self.DataHist.SetMinimum(0)
		self.DataHist.Draw()
		FitHist = self.fitter.GetPlot()
		FitHist.Sumw2()
		FitHist.Draw("SAME")

		value = np.ones(1)
		error = np.ones(1)

		InputHists = []

		from prettytable import PrettyTable

		resultTable = PrettyTable(("Template", "Fraction", "Error [%]"))

		self.legend = ROOT.TLegend(0.0, 0.7, 0.3, 1.0, "", "NDC")
		self.legend.SetBorderSize(0)

		for par in range( self.nPar ):
			self.fitter.GetResult(par, value, error)

			Histogram = self.ScaledTemplates[par]
			Histogram.Sumw2(False)
			Histogram.SetLineColor(par+1)

			HistName = Histogram.GetName().replace("MCORR_", "")
			resultTable.add_row(( HistName,  int(value[0]*1000)/1000., int(10000*error[0]/value[0])/100. ))
			InputHists += [ Histogram ]
			
			OutHist = self.OutHists[par]
			OutHist.Draw("SAME")

			Histogram.Draw("SAME")

			self.legend.AddEntry( OutHist,  SourceNames[HistName], "LEP" )

		self.legend.Draw()
		print resultTable

	def GetYield( self):
		Yields = {}
		for i, Hist in enumerate( self.ScaledTemplates ):
			HistName = Hist.GetName().replace("MCORR_", "")
			
			value = np.ones(1)
			error = np.ones(1)
			self.fitter.GetResult(i, value, error)

			Yields[ HistName ] = (value[0], error[0])

		return Yields




	def _del__(self):
		del self.fitter