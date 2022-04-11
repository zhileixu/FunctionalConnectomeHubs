close all;
clear;
clc;

Percentage_8x35 = load( '\FunctionalConnectomeHubs\Figure2\Figure2F\PercentageMatrix_8x35.csv' );;
    
Z = linkage( Percentage_8x35' );
figure( 'Position', [ 0, 0, 330, 1680 ]/2*0.755 );
[ H, ~, HubReorder ] = dendrogram( Z, 35, 'Orientation', 'left', 'ColorThreshold', 0.58 );
% cmap = [ 255, 127, 14; 44, 160, 44; 31, 119, 180; 0, 0, 0 ]/255;
set( H,'LineWidth',2 );
xlim( [ 0, 1.21 ] );
ylim( [ 0.5, 35.5] );         
axis off;
set( gca, 'Position', [ 0, 0, 1, 1 ] );