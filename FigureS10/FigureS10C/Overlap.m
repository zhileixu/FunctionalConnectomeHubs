clear;
clc;

load( '\FunctionalConnectomeHubs\BrainMask\GrayMatter_WithoutCER_Mask.mat' );

GSL = spm_vol( '\FunctionalConnectomeHubs\FigureS10\FigureS10B\GSL.nii' );
GSL = spm_read_vols( GSL );
GSL = GSL( MaskIndex )

Hub = spm_vol( '\FunctionalConnectomeHubs\FigureS10\FigureS10A\ZValue_P0.001_ClusterSize200_Mask.nii' );
Hub = spm_read_vols( Hub );
Hub = Hub( MaskIndex ) > 0.5;

Dice = 2*sum( ( GSL > 0.5 )'.*Hub )/( sum( GSL > 0.5 ) + sum( Hub ) );

load( '\FunctionalConnectomeHubs\SurrogateMap\ZValue_NGS_Surrogate.txt' );
[ ~, Index ] = sort( ZValue_NGS_Surrogate, 2, 'descend' );

N = 1000;
DiceNull = zeros( 1, N );
for Counter = 1:N
    HubNull = zeros( size( Hub ) );
    HubNull( Index( Counter, 1:sum( Hub ) ) ) = 1;
    DiceNull( Counter ) = 2*sum( ( GSL > 0.5 )'.*HubNull )./( sum( GSL > 0.5 ) + sum( HubNull ) );
end
dlmwrite( '\FunctionalConnectomeHubs\FigureS10\FigureS10C\DiceNull.csv', DiceNull, 'delimiter',',','precision','%.6f')

DiceP = sum( DiceNull > Dice )/N;