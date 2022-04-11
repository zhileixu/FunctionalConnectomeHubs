function RUN_Preproces( SubjectIndex )

load( '/FunctionalConnectomeHubs/Participant_Update.mat' );

InputPath = '/FunctionalConnectomeHubs/Preprocess_xbcdswran';

ParameterFile   = dir( [ InputPath, Participant_Update.Path{ SubjectIndex }, filesep, 'Preprocess_xbcdswran_*.mat' ] );
Para            = load( [ InputPath, Participant_Update.Path{ SubjectIndex }, filesep, ParameterFile.name ], 'Para' );
Para            = Para.Para;

IndividualPath = [ InputPath, Participant_Update.Path{ SubjectIndex }, filesep, 'FunRaw', filesep, num2str( Participant_Update.ID( SubjectIndex ), [ '%.', Participant_Update.IDLength{ SubjectIndex }, 'd' ] ) ];

%%
InputFile   = { [ IndividualPath, filesep, 'rest.nii' ] };

DelImg      = Para.DelImg{ 1 };

delete( [ IndividualPath, filesep, 'nrest.nii' ] );
gretna_RUN_RmFstImg( InputFile, DelImg );

%%
InputFile   = { [ IndividualPath, filesep, 'nrest.nii' ] };

TR          = Para.TR{ 1 };
SInd        = Para.SliOrd{ 1 };
RInd        = 2;

delete( [ IndividualPath, filesep, 'anrest.nii' ] );
gretna_RUN_SliTim( InputFile, TR, SInd, RInd );

%%
InputFile   = { [ IndividualPath, filesep, 'anrest.nii' ] };

NumPasses   = 2;

delete( [ IndividualPath, filesep, 'ranrest.nii' ] );
gretna_RUN_Realign( InputFile, NumPasses );

%%
InputFile   = { [ IndividualPath, filesep, 'ranrest.nii' ] };

SubjLab     = num2str( Participant_Update.ID( SubjectIndex ), [ '%.', Participant_Update.IDLength{ SubjectIndex }, 'd' ] );
FunPath     = [ InputPath, Participant_Update.Path{ SubjectIndex }, filesep, 'FunRaw' ];

gretna_RUN_ChkHM( InputFile, SubjLab, FunPath );

%%
InputFile   = { [ IndividualPath, filesep, 'ranrest.nii' ] };

SoFile      = { [ IndividualPath, filesep, 'meananrest.nii' ] };
EPITpm      = '/FunctionalConnectomeHubs/spm12/templates/EPI.nii';
BBox        = Para.BBox{ 1 };
VoxSize     = [ 3, 3, 3 ];

delete( [ IndividualPath, filesep, 'wranrest.nii' ] );
gretna_RUN_EpiNorm( InputFile, SoFile, EPITpm, BBox, VoxSize );

%%
InputFile   = { [ IndividualPath, filesep, 'meananrest.nii' ] };

delete( [ IndividualPath, filesep, 'wmeanranrest.nii' ] );
gretna_RUN_EpiNorm( InputFile, SoFile, EPITpm, BBox, VoxSize );

%%
NormSoFile = { [ IndividualPath, filesep, 'wmeananrest.nii' ] };

gretna_RUN_ChkNorm( NormSoFile, SubjLab, FunPath );

%%
InputFile   = { [ IndividualPath, filesep, 'wranrest.nii' ] };

FWHM = [ 6, 6, 6 ];

delete( [ IndividualPath, filesep, 'swranrest.nii' ] );
gretna_RUN_Smooth( InputFile, FWHM )

%%
InputFile   = { [ IndividualPath, filesep, 'swranrest.nii' ] };

PolyOrd     = 1;

delete( [ IndividualPath, filesep, 'dswranrest.nii' ] );
gretna_RUN_Detrend( InputFile, PolyOrd );

%% WGS
InputFile   = { [ IndividualPath, filesep, 'dswranrest.nii' ] };

GRETNAPath  = fileparts( which( 'gretna.m' ) );
GSMsk       = [ GRETNAPath, filesep, 'Mask', filesep, 'BrainMask_3mm.nii' ];
WMMsk       = [ GRETNAPath, filesep, 'Mask', filesep, 'WMMask_3mm.nii' ];
CSFMsk      = [ GRETNAPath, filesep, 'Mask', filesep, 'CSFMask_3mm.nii' ];
HMInd       = 3;
HMFile      = { [ IndividualPath, filesep, 'HeadMotionParameter.txt' ] };

delete( [ IndividualPath, filesep, 'cWGSdswranrest.nii' ] );
gretna_RUN_RegressOut( InputFile, GSMsk, WMMsk, CSFMsk, HMInd, HMFile );

%%
InputFile   = { [ IndividualPath, filesep, 'cWGSdswranrest.nii' ] };

TR          = Para.TR{ 1 };
Band        = [ 0.01, 0.1 ];

delete( [ IndividualPath, filesep, 'bcWGSdswranrest.nii' ] );
gretna_RUN_Filter( InputFile, TR, Band );

%%
InputFile   = { [ IndividualPath, filesep, 'bcWGSdswranrest.nii' ] };

FDFile      = { [ IndividualPath, filesep, 'PowerFD.txt' ] };
InterInd    = 3;
FDTrd       = 0.5;
PreNum      = 1;
PostNum     = 2;

delete( [ IndividualPath, filesep, 'xbcWGSdswranrest.nii' ] );
gretna_RUN_Scrubbing( InputFile, FDFile, InterInd, FDTrd, PreNum, PostNum );

%% NGS
InputFile   = { [ IndividualPath, filesep, 'dswranrest.nii' ] };

GRETNAPath  = fileparts( which( 'gretna.m' ) );
GSMsk       = [];
WMMsk       = [ GRETNAPath, filesep, 'Mask', filesep, 'WMMask_3mm.nii' ];
CSFMsk      = [ GRETNAPath, filesep, 'Mask', filesep, 'CSFMask_3mm.nii' ];
HMInd       = 3;
HMFile      = { [ IndividualPath, filesep, 'HeadMotionParameter.txt' ] };

delete( [ IndividualPath, filesep, 'cNGSdswranrest.nii' ] );
gretna_RUN_RegressOut( InputFile, GSMsk, WMMsk, CSFMsk, HMInd, HMFile );

%%
InputFile   = { [ IndividualPath, filesep, 'cNGSdswranrest.nii' ] };

TR          = Para.TR{ 1 };
Band        = [ 0.01, 0.1 ];

delete( [ IndividualPath, filesep, 'bcNGSdswranrest.nii' ] );
gretna_RUN_Filter( InputFile, TR, Band );

%%
InputFile   = { [ IndividualPath, filesep, 'bcNGSdswranrest.nii' ] };

FDFile      = { [ IndividualPath, filesep, 'PowerFD.txt' ] };
InterInd    = 3;
FDTrd       = 0.5;
PreNum      = 1;
PostNum     = 2;

delete( [ IndividualPath, filesep, 'xbcNGSdswranrest.nii' ] );
gretna_RUN_Scrubbing( InputFile, FDFile, InterInd, FDTrd, PreNum, PostNum );

end