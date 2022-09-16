close all;
clc;

load( '\FunctionalConnectomeHubs\BrainSpanAtlas\expression_matrix.csv' );
load( '\FunctionalConnectomeHubs\BrainSpanAtlas\AgeGenderStructure.mat' );
load( '\FunctionalConnectomeHubs\BrainSpanAtlas\EntrezID.txt' );
GeneSymbol = importdata( '\FunctionalConnectomeHubs\BrainSpanAtlas\GeneSymbol.txt' );

load( '\FunctionalConnectomeHubs\BrainSpanAtlas\HubStructure.txt' );
load( '\FunctionalConnectomeHubs\BrainSpanAtlas\NonHubStructure.txt' );
NonHubStructure = NonHubStructure( 1:9 );

HubIndex    = ismember( AgeGenderStructure( :, 3 ), HubStructure );
NonHubIndex = ismember( AgeGenderStructure( :, 3 ), NonHubStructure );

Age = [ AgeGenderStructure( HubIndex, 1 ); AgeGenderStructure( NonHubIndex, 1 ) ];
AgeUnique = unique( Age );

%%
for Process = { 'NeuronDifferentiation', 'NeuronMigration', 'DendriteDevelopment', 'SynapseDevelopment', 'AxonDevelopment', 'Myelination', 'OP', 'AG' }
    ProcessGenes = importdata( [ '\FunctionalConnectomeHubs\Figure5\GeneSet\', Process{ 1 }, '.txt' ] );
    GeneIndex = ismember( GeneSymbol, ProcessGenes );
    
    ExpressionData_Hub      = expression_matrix( GeneIndex, [ 0; HubIndex ] > 0.5 )';
    ExpressionData_NonHub   = expression_matrix( GeneIndex, [ 0; NonHubIndex ] > 0.5 )';
    
    [ ~, PC ] = pca( zscore( [ ExpressionData_Hub; ExpressionData_NonHub ] ), 'Centered', false );
    if corr( PC( :, 1 ), mean( [ ExpressionData_Hub; ExpressionData_NonHub ], 2 ) ) < 0
        PC = -PC;
    end
    PC = ( PC( :, 1 ) - min( PC( :, 1 ) ) )/( max( PC( :, 1 ) ) - min( PC( :, 1 ) ) );
    
    csvwrite( [ pwd, filesep, 'DevelopmentTrajectoryNeocortex-', Process{ 1 }, '-Data.csv' ], [ log2( Age ), PC, [ ones( sum( HubIndex ), 1 ); zeros( sum( NonHubIndex ), 1 ) ] ]' );
    
    MAD = zeros( numel( AgeUnique ), 1 );
    SampleSize = zeros( numel( AgeUnique ), 1 );
    for Counter = 1:numel( AgeUnique )
        MAD( Counter ) = mad( PC( Age == AgeUnique( Counter ) ), 1 );
        SampleSize( Counter ) = sum( Age == AgeUnique( Counter ) );
    end
    csvwrite( [ pwd, filesep, 'DevelopmentTrajectoryNeocortex-', Process{ 1 }, '-MAD.csv' ], [ log2( AgeUnique( SampleSize > 1.5 ) ), MAD( SampleSize > 1.5 ) ]' );
end