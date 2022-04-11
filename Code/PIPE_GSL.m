clear;
clc;

InputPath = '/FunctionalConnectomeHubs/Preprocess_xbcdswran';
OutputPath = '/FunctionalConnectomeHubs/GSL';

Opt.mode                = 'batch'; % qsub session
Opt.max_queued          = 3;
Opt.flag_verbose        = true;
Opt.flag_pause          = true;
Opt.flag_update         = false;
Opt.time_between_checks = 5;

%%

load( '/FunctionalConnectomeHubs/Participant_Update.mat' );

Pipeline = [];
for counter = 1：1000
    IndividualPath = [ InputPath, Participant_Update.Path{ counter }, filesep, 'FunRaw', filesep, num2str( Participant_Update.ID( counter ), [ '%.', Participant_Update.IDLength{ counter }, 'd' ] ) ];
    Pipeline.( [ 'PP_', num2str( counter, '%.4d' ) ] ).opt.InputFile    = [ IndividualPath filesep, 'xbcNGSdswranrest.nii' ];
    Pipeline.( [ 'PP_', num2str( counter, '%.4d' ) ] ).opt.OutputFile   = [ OutputPath, Participant_Update.Path{ counter }, filesep, num2str( Participant_Update.ID( counter ), [ '%.', Participant_Update.IDLength{ counter }, 'd' ] ) ];
    Pipeline.( [ 'PP_', num2str( counter, '%.4d' ) ] ).command          = 'RUN_GSL( opt.InputFile, opt.OutputFile )';
end


PipeLogPath = [ pwd, filesep, 'GSLLogs_', datestr( now, 30 ) ];

while exist( PipeLogPath, 'dir' ) == 7
    PipeLogPath = [ pwd, filesep, 'GSLLogs_', datestr( now, 30 ) ];
end
mkdir( PipeLogPath );
Opt.path_logs = PipeLogPath;

addpath( pwd );

psom_run_pipeline( Pipeline, Opt );