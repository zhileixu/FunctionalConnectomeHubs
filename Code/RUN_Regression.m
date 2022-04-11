function RUN_Regression( InputFile, OutputFile, CohortIndex )

if ~exist( [ OutputFile, '.mat' ], 'file' )
    
    load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask.mat' );
    load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask_Header.mat' );
    Header.dt( 1 ) = 16;
    
    VoxelNumber = sum( MaskIndex > 0.5 );
    
    load( '/FunctionalConnectomeHubs/CohortList.mat' );
    load( '/FunctionalConnectomeHubs/Participant_Update.mat' );
    
    Beta        = zeros( 1, VoxelNumber );
    BetaAge     = zeros( 1, VoxelNumber );
    BetaGender  = zeros( 1, VoxelNumber );
    SE          = zeros( 1, VoxelNumber );
    SEAge       = zeros( 1, VoxelNumber );
    SEGender    = zeros( 1, VoxelNumber );
    P           = zeros( 1, VoxelNumber );
    PAge        = zeros( 1, VoxelNumber );
    PGender     = zeros( 1, VoxelNumber );
    Residual    = zeros( CohortList{ CohortIndex, 4 }, VoxelNumber );
    
    Measurement = load( InputFile );
    Temp        = fieldnames( Measurement );
    Measurement = Measurement.( Temp{ 1 } );
    
    Age = Participant_Update.Age( CohortList{ CohortIndex, 5 }:CohortList{ CohortIndex, 6 } );
    Gender = double( Participant_Update.Gender( CohortList{ CohortIndex, 5 }:CohortList{ CohortIndex, 6 } ) == 'Male' );
    Gender = 2*Gender - 1;
    
    if min( sum( Gender > 0 ),  sum( Gender < 0 ) ) > 0.5
        for VoxelIndex = 1:VoxelNumber
            
            stats = regstats( Measurement( :, VoxelIndex ), [ Age - mean( Age ), Gender ], 'linear', { 'tstat', 'r' } );
            
            Beta( VoxelIndex )          = stats.tstat.beta( 1 );
            BetaAge( VoxelIndex )       = stats.tstat.beta( 2 );
            BetaGender( VoxelIndex )    = stats.tstat.beta( 3 );
            SE( VoxelIndex )            = stats.tstat.se( 1 );
            SEAge( VoxelIndex )         = stats.tstat.se( 2 );
            SEGender( VoxelIndex )      = stats.tstat.se( 3 );
            P( VoxelIndex )             = stats.tstat.pval( 1 );
            PAge( VoxelIndex )          = stats.tstat.pval( 2 );
            PGender( VoxelIndex )       = stats.tstat.pval( 3 );
            Residual( :, VoxelIndex )   = stats.r;
            
        end
        DFE = stats.tstat.dfe;
    else
        for VoxelIndex = 1:VoxelNumber
            
            stats = regstats( Measurement( :, VoxelIndex ), Age - mean( Age ), 'linear', { 'tstat', 'r' } );
            
            Beta( VoxelIndex )          = stats.tstat.beta( 1 );
            BetaAge( VoxelIndex )       = stats.tstat.beta( 2 );
            SE( VoxelIndex )            = stats.tstat.se( 1 );
            SEAge( VoxelIndex )         = stats.tstat.se( 2 );
            P( VoxelIndex )             = stats.tstat.pval( 1 );
            PAge( VoxelIndex )          = stats.tstat.pval( 2 );
            Residual( :, VoxelIndex )   = stats.r;
            
        end
        BetaGender( : ) = nan;
        SEGender( : ) = nan;
        PGender( : ) = nan;
        DFE = stats.tstat.dfe;
    end
    
    save( [ OutputFile, '.mat' ], 'Beta', 'BetaAge', 'BetaGender', 'SE', 'SEAge', 'SEGender', 'P', 'PAge', 'PGender', 'Residual', 'DFE' );
    
    
    Header.fname = [ OutputFile, '_Beta.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = Beta(:);
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );
    
    Header.fname = [ OutputFile, '_SE.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = SE(:);
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );
    
end

end