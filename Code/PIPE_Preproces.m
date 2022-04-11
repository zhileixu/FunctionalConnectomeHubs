clear;
clc;


Opt.mode                = 'batch'; % qsub session
Opt.max_queued          = 10;
Opt.flag_verbose        = true;
Opt.flag_pause          = true;
Opt.flag_update         = false;
Opt.time_between_checks = 5;

%%

Pipeline = [];
for counter = 1:1000
    Pipeline.( [ 'PP_', num2str( counter, '%.4d' ) ] ).opt.SubjectIndex = counter;
    Pipeline.( [ 'PP_', num2str( counter, '%.4d' ) ] ).command = 'RUN_Preproces( opt.SubjectIndex )';
end


PipeLogPath = [ pwd, filesep, 'PPLogs_', datestr( now, 30 ) ];

while exist( PipeLogPath, 'dir' ) == 7
    PipeLogPath = [ pwd, filesep, 'PPLogs_', datestr( now, 30 ) ];
end
mkdir( PipeLogPath );
Opt.path_logs = PipeLogPath;

addpath( pwd );

psom_run_pipeline( Pipeline, Opt );
