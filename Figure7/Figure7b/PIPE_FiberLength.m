clear;
clc;


FiberLength = ft_read_cifti( '\FunctionalConnectomeHubs\Figure7\Figure7b\iFOD2.76.mean-length-maps.dscalar.nii' );
Fiber = zeros( 124, numel( FiberLength.brainstructure ) );
for LengthIndex = 1:124
    Temp = [ 'ctl_map_at_', num2str( 2*LengthIndex ), '_', num2str( 2*LengthIndex + 2 ), '_mm' ];
    Fiber( LengthIndex, : ) = FiberLength.( Temp );
end
CortexMask = ~isnan( Fiber( 1, : ) );
FiberCortex = Fiber( :, CortexMask );

Length = 2*( 1:124 ) + 1;
LengthBin = [ 0, 20, 40, 60, 80, 120, 180, 250 ];
FiberBin = zeros( numel( LengthBin ) - 1, sum( CortexMask ) );
for Bin = 1:numel( LengthBin ) - 1
    FiberBin( Bin, : ) = sum( FiberCortex( ( Length > LengthBin( Bin ) ).*( Length < LengthBin( Bin + 1 ) ) > 0.5, : ) );
end

%%
Surf.L = gifti( '\FunctionalConnectomeHubs\Figure7\Figure7b\average.76.L.midthickness.surf.gii' );
Surf.R = gifti( '\FunctionalConnectomeHubs\Figure7\Figure7b\average.76.R.midthickness.surf.gii' );
Surf = [ Surf.L.vertices; Surf.R.vertices ];
SurfCortex = Surf( CortexMask, : );


load( '\FunctionalConnectomeHubs\BrainMask\GrayMatter_WithoutCER_Mask.mat' );
Hub = spm_vol( '\FunctionalConnectomeHubs\Figure1\Figure1cd\ZValue_P0.001_ClusterSize200_Mask.nii' );
[ Hub, XYZ ] = spm_read_vols( Hub );
Hub = Hub( MaskIndex );
XYZ = XYZ( :, MaskIndex )';


Distance = pdist2( SurfCortex, XYZ );
[ DistanceMin, MinIndex ] = min( Distance, [], 2 );
HubVertex = ( DistanceMin < 3 ).*( Hub( MinIndex ) > 0.5 );
NonHubVertex = ( DistanceMin < 3 ).*( Hub( MinIndex ) < 0.5 );

%%
Fiber_Hub = FiberBin( :, HubVertex > 0.5 );
Fiber_NonHub = FiberBin( :, NonHubVertex > 0.5 );

%csvwrite( '\FunctionalConnectomeHubs\Figure7\Figure7b\FiberNumber.csv', [ [ ones( 1, sum( HubVertex ) ), zeros( 1, sum( NonHubVertex ) ) ]; ...
%    zscore( [ Fiber_Hub, Fiber_NonHub ], [], 2 ) ] );

RankSum_Raw = zeros( 1, numel( LengthBin ) - 1 );
for LengthCounter = 1:numel( LengthBin ) - 1
    [ ~, ~, stat ] = ranksum( Fiber_Hub( LengthCounter, : ), Fiber_NonHub( LengthCounter, : ) );
    RankSum_Raw( LengthCounter ) = stat.ranksum;
end

%%
ZValue_Surrogate = load( '\FunctionalConnectomeHubs\SurrogateMap\ZValue_Surrogate.txt' );

N = 1000;
RankSum_Null = zeros( N, numel( LengthBin ) - 1 );

for Counter = 1:N
    [ ~, ZValue_Null ] = sort( ZValue_Surrogate( Counter, : ), 'descend' );
    Hub_Null = zeros( numel( Hub ), 1 );
    Hub_Null( ZValue_Null( 1:15461 ) ) = 1;
    HubVertex_Null = ( DistanceMin < 3 ).*( Hub_Null( MinIndex ) > 0.5 );
    NonHubVertex_Null = ( DistanceMin < 3 ).*( Hub_Null( MinIndex ) < 0.5 );
    
    for LengthCounter = 1:numel( LengthBin ) - 1
        [ ~, ~, stat ] = ranksum( FiberBin( LengthCounter, HubVertex_Null > 0.5 ), FiberBin( LengthCounter, NonHubVertex_Null > 0.5 ) );
        RankSum_Null( Counter, LengthCounter ) = stat.ranksum;
    end
end


RankSumP = zeros( 1, numel( LengthBin ) - 1 );
for Counter = 1:numel( LengthBin ) - 1
    RankSumP( Counter ) = sum( RankSum_Null( :, Counter ) > RankSum_Raw( Counter ) )/N;
end

save( '\FunctionalConnectomeHubs\Figure7\Figure7b\RankSumP.mat', 'RankSum_Raw', 'RankSum_Null', 'RankSumP' );