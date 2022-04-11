function RUN_SeedBasedFC( InputFile, OutputFile, Seed )

SeedNumber = numel( Seed( :, 1 ) );
[ OutputPath, name ] = fileparts( OutputFile  );
if ~exist( [ OutputPath, filesep, 'SeedBasedFC_', name, '.mat' ], 'file' )
    load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask.mat' );
    
    Nii = nifti( InputFile );
    VolumeCourse = reshape( double( Nii.dat ), [ Nii.dat.dim( 1, 1 )*Nii.dat.dim( 1, 2 )*Nii.dat.dim( 1, 3 ), Nii.dat.dim( 1, 4 ) ] )';
    MaskCourse = VolumeCourse( :, MaskIndex );
    
    SeedSignal = zeros( numel( MaskCourse( :, 1 ) ), SeedNumber );
    for SeedIndexTemp = 1:SeedNumber
        SeedSignal( :, SeedIndexTemp ) = mean( VolumeCourse( :, Seed( SeedIndexTemp, : ).*MaskIndex' > 0.5 ), 2 );
    end
    
    PoolCourse = [ MaskCourse, SeedSignal ];
    PoolCourse = zscore( PoolCourse );
    
    SeedBasedFC = PoolCourse( :, 1:end - SeedNumber )'*PoolCourse( :, end - SeedNumber + 1:end )/( size( PoolCourse, 1 ) - 1 );
    SeedBasedFC( isnan( SeedBasedFC ) ) = 0;
    
    mkdir( OutputPath );
    save( [ OutputPath, filesep, 'SeedBasedFC_', name, '.mat' ], 'SeedBasedFC' );
end

end