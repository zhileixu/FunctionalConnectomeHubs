function RUN_FCS( InputFile, OutputFile, Threshold, DistanceMask )

[ OutputPath, name ] = fileparts( OutputFile );

if ~exist( [ OutputPath, filesep, 'zFCS', filesep, 'zFCS_', name, '.nii' ], 'file' )
    
    Mask = '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask.mat';
    Header = '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask_Header.mat';
    
    AdjacentMatrix = RUN_ComputeAdjacentMatrix( InputFile, Mask );
    
    AdjacentMatrix( AdjacentMatrix < Threshold ) = 0;
    
    if DistanceMask > 0.5
        load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask_DistanceMask20.mat' );
        AdjacentMatrix( DistanceMask ) = 0;
        clear DistanceMask;
    end
    
    FCS = sum( AdjacentMatrix )/( length( AdjacentMatrix ) - 1 );
    clear AdjacentMatrix;
    
    load( Mask );
    load( Header );
    Header.dt( 1 ) = 16;
    
    mkdir( [ OutputPath, filesep, 'FCS' ] );
    
    Header.fname = [ OutputPath, filesep, 'FCS', filesep, 'FCS_', name, '.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = FCS;
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );
    
    mkdir( [ OutputPath, filesep, 'zFCS' ] );
    
    Header.fname = [ OutputPath, filesep, 'zFCS', filesep, 'zFCS_', name, '.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = ( FCS - mean( FCS ) )/( std( FCS ) );
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );
        
end

end