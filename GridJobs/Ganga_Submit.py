

def SubmitMCDec( eventNumber, prod_filter = "*", batch_submit = False):
	from fnmatch import fnmatch

	Application = DaVinci()
	Application.version = 'v38r1p1'


	JobName = ""
	datafiles = []
	DSTs = []
	nfiles = 5


	if len( eventNumber ) == 8:
		try:
			eventType = int( eventNumber )
		except:
			print "Invalid event type entered"
			return
		f = open('MC_DATA.conf', 'r')

		for line in f:
			if line == '\n':
				continue
			if line[0] == '#':
				continue
			line_data = line.split()
			if line_data[0] == eventNumber or eventNumber == "*":
				if fnmatch( line_data[1], prod_filter):
					DSTs.append(line_data)
					print line
			 
		
		
		ndfiles = len( DSTs )
		
	else:
		print "Event Type needs to be 8 digits"
		exit()

	

	for job_number in range(ndfiles):
		
		ds = []
		#for filename in datafiles:
		bk_query = BKQuery( path =  DSTs[job_number][1] )
		ds.extend( bk_query.getDataset() )
		
		Splitter = SplitByFiles(filesPerJob = nfiles, maxFiles = -1, ignoremissing = True, bulksubmit=False)
		Output   = [ DiracFile('*.root'), LocalFile('summary.xml') ]
		Backend  = Dirac()
		#Input    = [ File ( './LFNs.py' ) ]
		import os
		pwd = os.getcwd()
		
		Options = [];

			Options = [ File ( pwd + "/DecayTreeBuilder.py" ) ]
		
		
		
		Application.optsfile = Options
		j = Job ()
		j.name         = JobName + DSTs[job_number][0] + " AutoSubmission"
		j.comment      = eventNumber + " " + DSTs[job_number][1] 
		j.application  = Application
		
		j.application.user_release_area = '/afs/cern.ch/user/i/ismith/cmtuser'
		j.splitter     = Splitter
		j.backend      = Backend
		j.outputfiles  = Output
		j.inputdata  = ds
		j.do_auto_resubmit = True
		j.application.extraopts = ""
		j.application.extraopts += "DaVinci().DDDBtag   = '" + DSTs[job_number][2] + "'" + "\n"
		j.application.extraopts += "DaVinci().CondDBtag   = '" + DSTs[job_number][3] + "'" + "\n"
		j.application.extraopts += "DaVinci().EvtMax   = -1" + "\n"
		
		
		#Fill in the correct information for the year
		if fnmatch( DSTs[job_number][1], "/MC/2011/*"):
			j.application.extraopts += "DaVinci().DataType = '2011'" + "\n"
			
		elif fnmatch( DSTs[job_number][1], "/MC/2012/*"):
			j.application.extraopts += "DaVinci().DataType = '2012'" + "\n"
			
		elif fnmatch( DSTs[job_number][1], "/MC/2015/*"):
			j.application.extraopts += "DaVinci().DataType = '2015'" + "\n"
			
		elif fnmatch( DSTs[job_number][1], "/MC/2016/*"):
			j.application.extraopts += "DaVinci().DataType = '2016'" + "\n"
			
		if batch_submit:
			queues.add( j.submit )
		

	

def help_PhiMuNu():
	print "Usage:"
	print ""
	print "To run over MC Data:"
	print "\tSubmitMCDec( eventNumber, prod_filter = \"*\", batch_submit = False):"
	print "eventNumber = 8 digit string or '*', JpsiPhi: Reconstruct as Bs->JpsiPhi, ProdFilter: Wildcard for BK Addresses."
	print ""
	print ""


help_PhiMuNu()
