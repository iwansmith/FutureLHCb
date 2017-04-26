from GaudiConf import IOHelper
from Configurables import DaVinci, DecayTreeTuple
from DecayTreeTuple.Configuration import *
from Configurables import MCDecayTreeTuple, MCTupleToolKinematic, MCTupleToolHierarchy, LoKi__Hybrid__MCTupleTool, LoKi__Hybrid__EvtTupleTool, TupleToolEventInfo
#############################################################################################
#                                                                                           #
#                                  Create The DecayTree                                     #
#                                                                                           #
#############################################################################################
Trees = []

# Bs -> K Mu Nu
DecayTree = MCDecayTreeTuple('TupleBs2KMuNu')
DecayTree.Decay = '([ [B_s0]nos -> ^K- ^mu+ ... ]CC || [ [B_s~0]os -> ^K- ^mu+ ... ]CC)'
Trees.append( DecayTree )

# Bs -> K* Mu Nu
DecayTree = MCDecayTreeTuple('TupleBs2KstarMuNu')
DecayTree.Decay = '([ [B_s0]nos -> ^( K*(892)- => ^k- ^pi0 ) ^mu+ ... ]CC || [ [B_s~0]os -> ^( K*(892)- => ^k- ^pi0 ) ^mu+ ... ]CC)'
Trees.append( DecayTree )


#Ds Decays
DecayTree = MCDecayTreeTuple('TupleBs2DsMuNu')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D_s- => ^K+ ^K- ^pi- ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^( D_s- => ^K+ ^K- ^pi- ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

#DsStar Decays
DecayTree = MCDecayTreeTuple('TupleBs2DsStarMuNu_pi0')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStarMuNu_g')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

#DsStar0 Decays
DecayTree = MCDecayTreeTuple('TupleBs2DsStar0MuNu_pi0')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ) ^mu+ ... ]CC )'
Trees.append( DecayTree )


# These Two Decay Descriptors may be buggy. No events in the Analysis NTuple. But they may not be in the MC anyway?
DecayTree = MCDecayTreeTuple('TupleBs2DsStar0MuNu_g')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D*_s0- => ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^gamma ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^( D*_s0- => ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^gamma ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStar0MuNu_pi0pi0')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ^pi0 ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ^pi0 ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStar0MuNu_pippim')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi+ ^pi- ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s0- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi+ ^pi- ) ^mu+ ... ]CC )'
Trees.append( DecayTree )


#DsStar1(2460) Decays
DecayTree = MCDecayTreeTuple('TupleBs2DsStar12460MuNu_pi0')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D_s1(2460)- => ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^pi0 ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^( D_s1(2460)- => ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^pi0 ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStar12460MuNu_pi0pi0')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D_s1(2460)- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ^pi0 ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D_s1(2460)- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi0 ^pi0 ) ^mu+ ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStar12460MuNu_pippim')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D_s1(2460)- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi+ ^pi- ) ^mu+ ... ]CC ) || ([ [B_s~0]os -> ^(  D_s1(2460)- => ^( D_s- => ^K+ ^K- ^pi- ) ^pi+ ^pi- ) ^mu+ ... ]CC )'
Trees.append( DecayTree )


# Tauonic Decays
DecayTree = MCDecayTreeTuple('TupleBs2DsTauNu')
DecayTree.Decay = '( [ [B_s0]nos -> ^( D_s- => ^K+ ^K- ^pi- ) ^( tau+ => ^mu+ ^nu_tau~ ^nu_mu )  ... ]CC ) || ([ [B_s~0]os -> ^( D_s- => ^K+ ^K- ^pi- ) ^( tau+ => ^mu+ ^nu_tau~ ^nu_mu ) ... ]CC )'
Trees.append( DecayTree )

DecayTree = MCDecayTreeTuple('TupleBs2DsStarTauNu_g')
DecayTree.Decay = '( [ [B_s0]nos -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^( tau+ => ^mu+ ^nu_tau~ ^nu_mu ) ... ]CC ) || ([ [B_s~0]os -> ^(  D*_s- => ^( D_s- => ^K+ ^K- ^pi- ) ^gamma ) ^( tau+ => ^mu+ ^nu_tau~ ^nu_mu ) ... ]CC )'
Trees.append( DecayTree )

for tree in Trees:
	tree.addTool(MCTupleToolKinematic())
	tree.MCTupleToolKinematic.Verbose=True
	
	
	tree.ToolList += [
			 "MCTupleToolHierarchy"
			,"MCTupleToolSemileptonic"
			,"TupleToolRecoStats"
			,"MCTupleToolKinematic"
			]


	DaVinci().UserAlgorithms += [ tree ]


DaVinci().SkipEvents = 0 
DaVinci().PrintFreq = 100
DaVinci().EvtMax = 10000
DaVinci().TupleFile = "DVTuples1.root"
DaVinci().HistogramFile = 'DVHistos.root'
DaVinci().InputType = "DST"
DaVinci().DataType = "2012"	
DaVinci().Simulation = True
DaVinci().Lumi = False

IOHelper().inputFiles([
#    '/eos/lhcb/grid/prod/lhcb/MC/2012/ALLSTREAMS.DST/00051442/0000/00051442_00000061_2.AllStreams.dst' # For Dsmunu Monte Carlo
#    '/eos/lhcb/grid/prod/lhcb/MC/2012/ALLSTREAMS.DST/00026073/0000/00026073_00000059_1.allstreams.dst' # For K mu nu Monte Carlo
'/eos/lhcb/grid/prod/lhcb/MC/2012/ALLSTREAMS.DST/00048126/0000/00048126_00000014_2.AllStreams.dst' # K* mu nu Monte Carlo
], clear=True)

