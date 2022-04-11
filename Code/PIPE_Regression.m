clear;
clc;


InputPath = '/FunctionalConnectomeHubs/FCS/FCS_0.1_WDM_xbcWGSdswran';
Measurement = 'FCS';

for Cohort = 1:61
	load( '/FunctionalConnectomeHubs/SiteList.mat' );
	load( '/FunctionalConnectomeHubs/Participant_Update.mat' );

	opt.InputFile   = [ InputPath, SiteList{ Cohort, 2 }, filesep, Measurement, filesep, Measurement ];
	opt.OutputFile  = [ InputPath, filesep, 'PoolMeasurement', filesep, Measurement, filesep, SiteList{ Cohort, 1 } ];
	opt.SubjectList = Participant_Update.ID( SiteList{ Cohort, 5 }:SiteList{ Cohort, 6 } );
	opt.IDLength    = SiteList{ Cohort, 3 };
	RUN_PoolMeasurement( opt.InputFile, opt.OutputFile, opt.SubjectList, opt.IDLength )

	opt.InputFile   = [ InputPath, filesep, 'PoolMeasurement', filesep, Measurement, filesep, SiteList{ Cohort, 1 }, '.mat' ];
	opt.OutputFile  = [ InputPath, filesep, 'Regression', filesep, Measurement, filesep, SiteList{ Cohort, 1 } ];
	opt.Cohort   = Cohort;
	RUN_Regression( opt.InputFile, opt.OutputFile, opt.Cohort )
end