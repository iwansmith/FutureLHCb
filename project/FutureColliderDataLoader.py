from FourVector import *
from FutureColliderTools import *
from FutureColliderVariables import *
import numpy as np
import ROOT


import pickle
from root_numpy import tree2array


# Try and open the data from the pickle file. If that fails look for the ROOT file and make the pickle file

def LoadData_KMuNu(EvType, FileTree):
	PickleName = "/home/ismith/tmp/Bs_K_" + EvType + ".pickle"

	try:
		InputData,K_PE,Mu_PE,B_PE,B_Origin,B_End = pickle.load( open( PickleName, "rb" ) )
	except:

		Datafile = ROOT.TFile.Open(FileTree[0])
		Tree = Datafile.Get(FileTree[1])
		try:
			B, Mu, K = GetParticleNames_KMu( Tree )
			#print EvType, B, Mu, K
		except:
			# If there is no compatible data return nothing
			return None
			
		K_PE     = ["{0}_TRUEP_E".format(K) , "{0}_TRUEP_X".format(K) , "{0}_TRUEP_Y".format(K) , "{0}_TRUEP_Z".format(K) ]
		Mu_PE    = ["{0}_TRUEP_E".format(Mu), "{0}_TRUEP_X".format(Mu), "{0}_TRUEP_Y".format(Mu), "{0}_TRUEP_Z".format(Mu)]
		B_PE     = ["{0}_TRUEP_E".format(B),  "{0}_TRUEP_X".format(B),  "{0}_TRUEP_Y".format(B),  "{0}_TRUEP_Z".format(B) ]
		B_Origin = ["{0}_TRUEORIGINVERTEX_X".format(B), "{0}_TRUEORIGINVERTEX_Y".format(B), "{0}_TRUEORIGINVERTEX_Z".format(B)]
		B_End    = ["{0}_TRUEENDVERTEX_X".format(B), "{0}_TRUEENDVERTEX_Y".format(B), "{0}_TRUEENDVERTEX_Z".format(B)]

		branches = K_PE + Mu_PE + B_PE + B_Origin + B_End

		CutString = "{0}_MC_ETA > 2 && {0}_MC_ETA < 5 && {1}_MC_ETA > 2 && {1}_MC_ETA < 5".format(Mu, K)

		InputData = tree2array (
			Tree,
			branches = branches
			#selection = CutString
			)
		pickle.dump( (InputData,K_PE,Mu_PE,B_PE,B_Origin,B_End), open( PickleName, "wb" ) )

	return InputData,K_PE,Mu_PE,B_PE,B_Origin,B_End


def LoadData_DsMuNu(EvType, FileTree):
	
	PickleName = "/home/ismith/tmp/Bs_Ds_" + EvType + ".pickle"
	InputData = None
		
	try:
		InputData,K1_PE,K2_PE,Pi_PE,Mu_PE,B_PE,B_Origin,B_End = pickle.load( open( PickleName, "rb" ) )
	except:


		Datafile = ROOT.TFile.Open(FileTree[0])
		Tree = Datafile.Get(FileTree[1])
		try:
			B, Mu, K1, K2, Pi = GetParticleNames_DsMu( Tree )
			print EvType, B, Mu, K1, K2, Pi
		except:
			# If data can't be laoded return nothing
			return None

		K1_PE    = ["{0}_TRUEP_E".format(K1), "{0}_TRUEP_X".format(K1), "{0}_TRUEP_Y".format(K1), "{0}_TRUEP_Z".format(K1)]
		K2_PE    = ["{0}_TRUEP_E".format(K2), "{0}_TRUEP_X".format(K2), "{0}_TRUEP_Y".format(K2), "{0}_TRUEP_Z".format(K2)]
		Pi_PE    = ["{0}_TRUEP_E".format(Pi), "{0}_TRUEP_X".format(Pi), "{0}_TRUEP_Y".format(Pi), "{0}_TRUEP_Z".format(Pi)]
		Mu_PE    = ["{0}_TRUEP_E".format(Mu), "{0}_TRUEP_X".format(Mu), "{0}_TRUEP_Y".format(Mu), "{0}_TRUEP_Z".format(Mu)]
		B_PE     = ["{0}_TRUEP_E".format(B),  "{0}_TRUEP_X".format(B),  "{0}_TRUEP_Y".format(B),  "{0}_TRUEP_Z".format(B) ]
		B_Origin = ["{0}_TRUEORIGINVERTEX_X".format(B), "{0}_TRUEORIGINVERTEX_Y".format(B), "{0}_TRUEORIGINVERTEX_Z".format(B)]
		B_End    = ["{0}_TRUEENDVERTEX_X".format(B), "{0}_TRUEENDVERTEX_Y".format(B), "{0}_TRUEENDVERTEX_Z".format(B)]

		branches = K1_PE + K2_PE + Pi_PE + Mu_PE + B_PE + B_Origin + B_End

		InputData = tree2array (
			Tree,
			branches = branches
			)
		pickle.dump( (InputData,K1_PE,K2_PE,Pi_PE,Mu_PE,B_PE,B_Origin,B_End), open( PickleName, "wb" ) )

	return InputData,K1_PE,K2_PE,Pi_PE,Mu_PE,B_PE,B_Origin,B_End


def SaveHistogram_KMuNu( EvType, FileTree, resolution = 1.0, combinatorial = False ):
	
	isCombi = ""
	if combinatorial:
		isCombi = "_Combinatorial"
	HistTitle = SourceNames[EvType + isCombi] 

	h_MCORR = ROOT.TH1F("MCORR_" + EvType + isCombi, HistTitle, 100, 2500, 6000)
	h_MM2   = ROOT.TH1F("MissingMass2_" + EvType + isCombi, HistTitle, 100, -10e6, 20e6) 
	h_Q21   = ROOT.TH1F("QSQ_SOL1_" + EvType + isCombi, HistTitle, 100, 0, 25e6) 
	h_Q22   = ROOT.TH1F("QSQ_SOL2_" + EvType + isCombi, HistTitle, 100, 0, 25e6) 
	h_Q20   = ROOT.TH1F("QSQ_SOLTrue_" + EvType + isCombi, HistTitle, 100, 0, 25e6) 


	InputData = None
	try:
		InputData,K_PE,Mu_PE,B_PE,B_Origin,B_End = LoadData_KMuNu(EvType, FileTree)
	except:
		return
	 
	DataType = InputData[K_PE[0]].dtype

	B_SV = InputData[B_Origin].copy().view(( DataType, 3 ))
	B_PV = InputData[B_End].copy().view(( DataType, 3 ))


	K  = FourVector(InputData[K_PE])
	Mu = FourVector(InputData[Mu_PE])
	B = FourVector(InputData[B_PE])

	reps = 1
	if combinatorial:
		reps = 10

	for rep in range(reps):
		if combinatorial:
			Mu.roll()
			B.roll()
			B_PV = np.roll(B_PV, 1)

			EvType = EvType+"_Combinatorial"
		
		B_SV_New = SmearVertex( B_SV, sigma_SV_LHCb * resolution )
		B_PV_New = SmearVertex( B_PV, sigma_PV_LHCb * resolution )


		B_Direction = ThreeVector(B_SV_New - B_PV_New)
		Y = K + Mu
			
		Cuts = ()  
		Cuts += ( K.P() > 10000, )
		Cuts += ( K.Pt() > 500, )
		Cuts += ( Mu.P() > 6000., )
		Cuts += ( Mu.Pt() > 1500., )
		Cuts += ( -np.cos( B_Direction.Angle( Y.Vect() ) ) > 0.997,  )
			
		PassCuts = np.all( Cuts, axis = 0)
		
		QSQ = (B - K).M2()

		MCORR = GetCorrectedMass(Y[PassCuts], B_Direction[PassCuts])
		MM2 = GetMissingMass2(K[PassCuts], Mu[PassCuts], B_Direction[PassCuts])
		Q21, Q22 = GetQ2(Y[PassCuts], Mu[PassCuts], B_Direction[PassCuts])
		
		
		nev = MM2.shape[0]
		
		
		#for MC, MM in zip(MCORR, MM2):
		h_MCORR.FillN( nev, MCORR,  np.ones(nev)) 
		h_MM2  .FillN( nev, MM2,    np.ones(nev))
		h_Q21  .FillN( nev, Q21,np.ones(nev))
		h_Q22  .FillN( nev, Q22,np.ones(nev))
		h_Q20  .FillN( nev, QSQ,np.ones(nev))
	
	
	h_MCORR.GetXaxis().SetTitle("m_{corr}(B_{s})")
	h_MM2.GetXaxis().SetTitle("Missing Mass^{2}")
	h_Q21.GetXaxis().SetTitle("q^{2}~Solution~1")
	h_Q22.GetXaxis().SetTitle("q^{2}~Solution~2")
	h_Q20.GetXaxis().SetTitle("q^{2} True Solution")
	
	
	f_Histogram = ROOT.TFile.Open("../output/Source_Histograms_KMu_{0}_LHCb.root".format( resolution ), "UPDATE")
	f_Histogram.cd()
	SaveHistogram( f_Histogram, h_MCORR )
	SaveHistogram( f_Histogram, h_MM2 )
	SaveHistogram( f_Histogram, h_Q21 )
	SaveHistogram( f_Histogram, h_Q22 )
	SaveHistogram( f_Histogram, h_Q20 )
	f_Histogram.Close()

def SaveHistogram_DsMuNu( EvType, FileTree, resolution = 1.0, combinatorial = False ):

	isCombi = ""
	if combinatorial:
		isCombi = "_Combinatorial"
	HistTitle = SourceNames[EvType + isCombi] 

	h_MCORR = ROOT.TH1F("MCORR_" + EvType + isCombi, HistTitle, 100, 2500, 6000)
	h_MM2   = ROOT.TH1F("MissingMass2_" + EvType + isCombi, HistTitle, 100, -10e6, 20e6) 
	h_Q21   = ROOT.TH1F("QSQ_SOL1_" + EvType + isCombi, HistTitle, 100, 0, 12e6) 
	h_Q22   = ROOT.TH1F("QSQ_SOL2_" + EvType + isCombi, HistTitle, 100, 0, 12e6) 
	h_Q20   = ROOT.TH1F("QSQ_SOLTrue_" + EvType + isCombi, HistTitle, 100, 0, 12e6) 

	InputData = None
		
	try:
		InputData,K1_PE,K2_PE,Pi_PE,Mu_PE,B_PE,B_Origin,B_End = LoadData_DsMuNu(EvType, FileTree)
	except:
		return
		
	DataType = InputData[K1_PE[0]].dtype



	K1 = FourVector(InputData[K1_PE])
	K2 = FourVector(InputData[K2_PE])
	Pi = FourVector(InputData[Pi_PE])
	Mu = FourVector(InputData[Mu_PE])
	B = FourVector(InputData[B_PE])

	B_SV = InputData[B_Origin].copy().view(( DataType, 3 ))
	B_PV = InputData[B_End].copy().view(( DataType, 3 ))

	reps = 1
	if combinatorial:
		reps = 10

	for rep in range(reps):
		
		if combinatorial:
			
			B_SV = np.roll(B_SV, 1)
			K1.roll()
			K2.roll()
			Pi.roll()
			
			EvType = EvType+"_Combinatorial"
		

		Ds = K1 + K2 + Pi

		Y  = Ds + Mu
		QSQ = ( B - Ds ).M2()


		B_SV_New = SmearVertex( B_SV, sigma_SV_LHCb * resolution)
		B_PV_New = SmearVertex( B_PV, sigma_PV_LHCb * resolution)
		B_Direction = ThreeVector(B_SV_New - B_PV_New)

		Cuts = ()  

		Cuts += ( K1.P() > 10000., )
		Cuts += ( K1.Pt() > 500, )
		Cuts += ( K2.P() > 10000, )
		Cuts += ( K2.Pt() > 500, )
		Cuts += ( Pi.P() > 2000, )
		Cuts += ( Pi.Pt() > 250, )
		Cuts += ( Mu.P() > 6000., )
		Cuts += ( Mu.Pt() > 1500., )
		Cuts += ( np.abs( Ds.M() - 1968 ) < 80, )
		Cuts += ( Y.M() > 2200, )
		Cuts += ( Y.M() < 8000, )
		Cuts += ( -np.cos( B_Direction.Angle( Y.Vect() ) ) > 0.999,  )

		PassCuts = np.all( Cuts, axis = 0)


		Q20 = (B - Ds).M2()

		MCORR = GetCorrectedMass(Y[PassCuts], B_Direction[PassCuts])
		MM2 = GetMissingMass2(Ds[PassCuts], Mu[PassCuts], B_Direction[PassCuts])
		Q21, Q22 = GetQ2(Y[PassCuts], Mu[PassCuts], B_Direction[PassCuts])


		nev = MM2.shape[0]

		#for MC, MM in zip(MCORR, MM2):
		h_MCORR.FillN( nev, MCORR,  np.ones(nev)) 
		h_MM2  .FillN( nev, MM2,    np.ones(nev))
		h_Q21  .FillN( nev, Q21,np.ones(nev))
		h_Q22  .FillN( nev, Q22,np.ones(nev))
		h_Q20  .FillN( nev, QSQ,np.ones(nev))


	h_MCORR.GetXaxis().SetTitle("m_{corr}(B_{s})")
	h_MM2.GetXaxis().SetTitle("Missing Mass^{2}")
	h_Q21.GetXaxis().SetTitle("q^{2}~Solution~1")
	h_Q22.GetXaxis().SetTitle("q^{2}~Solution~2")
	h_Q20.GetXaxis().SetTitle("q^{2}~True Solution")
	
	
	f_Histogram = ROOT.TFile.Open("../output/Source_Histograms_DsMu_{0}_LHCb.root".format(resolution), "UPDATE")
	f_Histogram.cd()
	SaveHistogram( f_Histogram, h_MCORR )
	SaveHistogram( f_Histogram, h_MM2 )
	SaveHistogram( f_Histogram, h_Q21 )
	SaveHistogram( f_Histogram, h_Q22 )
	SaveHistogram( f_Histogram, h_Q20 )
	f_Histogram.Close()
