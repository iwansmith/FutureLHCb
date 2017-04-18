from FourVector import *
import numpy as np
import ROOT

ROOT.gStyle.SetOptStat(0)


def GetParticleNames_KMu( Tree, skip = 0):

	Kaons = []
	Muons = []
	B = ""


	for Branch in Tree.GetListOfBranches():
		BranchName = Branch.GetName()
		
		ParticleName = BranchName.split("_")[0]
		B_name = BranchName.split("_TRUEP")[0]
		
		if BranchName != B_name:
			if B == "":
				B = B_name
		
		if ParticleName[0] == "K":
			if (ParticleName not in Kaons ):
				Kaons.append( ParticleName)

		if ParticleName[0:2] == "mu":
			if (ParticleName not in Muons ):
				Muons.append( ParticleName)

	for K in Kaons: # Find a pair of opposite sign kaons and muons
		for Mu in Muons:
			if ( "plus" in K+Mu and "minus" in K+Mu ):
				if skip == 0:
					return B, Mu, K
				else:
					skip-=1

def GetParticleNames_DsMu( Tree, skip = 0):

	Kaons = []
	Muons = []
	Pions = []
	B = ""


	for Branch in Tree.GetListOfBranches():
		BranchName = Branch.GetName()
		
		ParticleName = BranchName.split("_")[0]
		B_name = BranchName.split("_TRUEP")[0]
		
		if BranchName != B_name:
			if B == "":
				B = B_name
		
		if ParticleName[0] == "K":
			if (ParticleName not in Kaons ):
				Kaons.append( ParticleName)

		if ParticleName[0:2] == "mu":
			if (ParticleName not in Muons ):
				Muons.append( ParticleName)

		if ParticleName[0:2] == "pi":
			if (ParticleName not in Pions ):
				Pions.append( ParticleName)

	for K1 in Kaons: # Find a pair of opposite sign kaons and muons
		for K2 in Kaons: # Find a pair of opposite sign kaons and muons
			if Kaons.index(K2) >= Kaons.index(K1):
				continue
			if not ( "plus" in K1+K2 and "minus" in K1+K2 ): # Require the two kaons to be opposite sign
				continue
			for Mu in Muons:
				for Pi in Pions:
					if not ( "plus" in Mu+Pi and "minus" in Mu+Pi ): # Require the Muon and Pion to be opposite sign
						continue
						
					if skip == 0:
						return B, Mu, K1, K2, Pi
					else:
						skip-=1


def SaveHistogram(File, Histogram ):
    File.cd()
    
    nBins = Histogram.GetNbinsX()
    Histogram.SetBinContent(0, 0)
    Histogram.SetBinContent(nBins+1, 0)

    Histogram.Sumw2()
    
    for n in range(nBins):
        BinContent = Histogram.GetBinContent( n+1 )
        Histogram.SetBinContent( n+1, BinContent+0.0001 )
    
    Histogram.Write()
    Histogram.Scale( 1/ Histogram.Integral() )
    Histogram.SetName( Histogram.GetName() + "_norm" )
    Histogram.Write()

def SmearVertex(Vertex, sigma = (0,0,0)):
    
    nev = Vertex.shape[0]
    
    Smearing = np.zeros((nev,3))
    for x in range(3):
        smear = sigma[x]
        if smear != 0.:
            Smearing[:,x] = np.random.normal(0, smear, nev )
    return Vertex + Smearing

def GetCorrectedMass(Y, B_Direction):
              

    Y_M = Y.M()
    Y_PT = Y.Perp( B_Direction ) # This is momentum perp. to B, not Z

    Bs_MCORR = np.sqrt( np.square( Y_M ) + np.square( Y_PT ) ) + Y_PT

    return Bs_MCORR
    
def GetMissingMass2(K, Mu, B_Direction):

    Y = K + Mu

    B_PZ = np.multiply( np.divide( 5301, Y.M() ), Y.PZ() )
    B_P = B_Direction / B_Direction.PZ
    B_P = B_P * B_PZ
    B = FourVector()
    B.SetXYZM( B_P, 5301)

    return (B - K - Mu).M2()

def GetQ2(Y, Mu, B_Direction ):

    mass = 5370.
    B_Direction = B_Direction.Unit() # Just to be safe
    
    Y3  = Y.Vect(); 
    

    Perp_dirn  = ( Y3  - (B_Direction) * Y3.Dot(B_Direction)).Unit(); 

    Ppmu = FourVector()
    Ppmu.SetX( Y3.Dot(B_Direction) )
    Ppmu.SetY( Y3.Perp(B_Direction) )
    Ppmu.SetZ( np.zeros(Y.PX().shape) )
    Ppmu.PE = Y.PE.copy()
    
    E_nurest = ( mass  * mass  - Y.M2())/ (2 * mass ); 
    E_pmurest = np.sqrt(E_nurest * E_nurest + Y.M2());

    px_rest = np.sqrt( E_nurest * E_nurest  - Ppmu.PY() * Ppmu.PY() ); 

    # quadratic coefficients
    A = Y.PE * Y.PE  - Ppmu.PX() * Ppmu.PX()
    B = - 2 * Ppmu.PX()  * (E_nurest * E_pmurest + px_rest * px_rest )
    C = - (E_nurest * E_pmurest + px_rest * px_rest )* \
        (E_nurest * E_pmurest + px_rest * px_rest ) +  Y.PE * Y.PE * Ppmu.PY() * Ppmu.PY()

    p1nu = (- B + np.sqrt(B*B - 4 * A * C) )/(2*A);
    p2nu = (- B - np.sqrt(B*B - 4 * A * C) )/(2*A);
    

    # reconstruct neutrino 3 vectors and 4 vectors
    P_nu_recon_3V1 = (B_Direction) * p1nu  + Perp_dirn * -Ppmu.PY(); 
    P_nu_recon_3V2 = (B_Direction) * p2nu  + Perp_dirn * -Ppmu.PY(); 
    
    NuSol1 = FourVector()
    NuSol1.SetX( P_nu_recon_3V1.PX )
    NuSol1.SetY( P_nu_recon_3V1.PY )
    NuSol1.SetZ( P_nu_recon_3V1.PZ )
    NuSol1.PE = np.sqrt(p1nu*p1nu + Ppmu.PY() * Ppmu.PY() )
    
    NuSol2 = FourVector()
    NuSol2.SetX( P_nu_recon_3V2.PX )
    NuSol2.SetY( P_nu_recon_3V2.PY )
    NuSol2.SetZ( P_nu_recon_3V2.PZ )
    NuSol2.PE = np.sqrt(p2nu*p2nu + Ppmu.PY() * Ppmu.PY() )
        
    Q21 = (NuSol1 + Mu).M2()
    Q22 = (NuSol2 + Mu).M2()
    
    return Q21, Q22


