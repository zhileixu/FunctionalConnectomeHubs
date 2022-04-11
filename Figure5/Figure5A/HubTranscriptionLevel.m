clear;
clc;

load( '\FunctionalConnectomeHubs\Figure4\Figure4A\Hub1158.csv' );

%%
load( '\FunctionalConnectomeHubs\AHBAprocessed\AHBA1158x10027.csv' );
load( '\FunctionalConnectomeHubs\AHBAprocessed\ROIxGene_aparcaseg_RNAseq.mat', 'probeInformation' );
EntrezID = load( '\FunctionalConnectomeHubs\BrainSpanAtlas\EntrezID.txt' );
GeneSymbol = importdata( '\FunctionalConnectomeHubs\BrainSpanAtlas\GeneSymbol.txt' );

TranscriptionLevelPC = zeros( 8, 1158 );
Counter = 1;
for Process = { 'NeuronDifferentiation', 'NeuronMigration', 'DendriteDevelopment', 'SynapseDevelopment', 'AxonDevelopment', 'Myelination', 'OP', 'AG' }
    ProcessGenes = importdata( [ '\FunctionalConnectomeHubs\BrainSpanAtlas\', Process{ 1 }, '.txt' ]  );
    Index = ismember( GeneSymbol, ProcessGenes );
    Index = ismember( probeInformation.EntrezID, EntrezID( Index ) );
    Data = AHBA1158x10027( :, Index );
    [ ~, PC ] = pca( Data, 'Centered', false );
    PC = PC( :, 1 );
    if corr( PC, mean( Data, 2 ) ) < 0
        PC = -PC;
    end
    PC = ( PC( :, 1 ) - min( PC( :, 1 ) ) )/( max( PC( :, 1 ) ) - min( PC( :, 1 ) ) );
    TranscriptionLevelPC( Counter, : ) = PC;
    Counter = Counter + 1;
end
% csvwrite( 'HubTranscriptionLevel.csv', [ Hub1158'; TranscriptionLevelPC ] );

%%
load( '\FunctionalConnectomeHubs\SurrogateMap\ZValue_Surrogate.txt' );
load( '\FunctionalConnectomeHubs\Figure4\Figure4A\AHBA1158Index.csv' );
ZValue_Surrogate = ZValue_Surrogate( :, AHBA1158Index );

[ ZValue, ZValueIndex ] = sort( ZValue_Surrogate, 2, 'descend' );

N = 1000;
RankSum = zeros( 8, 1 );
RankSum_Null = zeros( 8, N );
Tail = { 'right', 'left', 'right', 'right', 'left', 'left', 'right', 'right' };
Sign = [ 1, -1, 1, 1, -1, -1, 1, 1 ];
P_Perm = zeros( 8, 1 );
for Process = 1:8
    PC = TranscriptionLevelPC( Process, : );
    [ ~, ~, stats ] = ranksum( PC( Hub1158 > 0.5 ), PC( Hub1158 < 0.5 ), 'tail', Tail{ Process }  );
    RankSum( Process ) = stats.ranksum;
    
    for Counter = 1:N
        [ ~, ~, stats ] = ranksum( PC( ZValueIndex( Counter, 1:sum( Hub1158 > 0.5 ) ) ), PC( ZValueIndex( Counter, sum( Hub1158 > 0.5 ) + 1:end ) ), 'tail', Tail{ Process } );
        RankSum_Null( Process, Counter )= stats.ranksum;
    end
    if Sign( Process ) > 0
        P_Perm( Process ) = sum( RankSum_Null( Process, : ) > RankSum( Process ) )/N;
    else
        P_Perm( Process ) = sum( RankSum_Null( Process, : ) < RankSum( Process ) )/N;
    end
end
save( [ pwd, filesep, 'RankSumP.mat' ], 'RankSum', 'RankSum_Null', 'P_Perm' );