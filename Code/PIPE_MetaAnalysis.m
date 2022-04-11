clear;
clc;

InputPath = '/FunctionalConnectomeHubs/FCS/FCS_0.1_WDM_xbcWGSdswran';
Measurement = 'zFCS'; 
                  
OPT.InputPath = [ InputPath, filesep, 'Regression', filesep, Measurement ];
OPT.OutputPath = [ InputPath, filesep, 'MetaAnalysis', filesep, Measurement, '_Base', num2str( Base ) ];

RUN_MetaAnalysis( OPT.InputPath, OPT.OutputPath );
