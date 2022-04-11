function RUN_GSL( InputFile, OutputFile )

[ OutputPath, name ] = fileparts( OutputFile );

if ~exist( [ OutputPath, filesep, 'zGSL', filesep, 'zGSL_', name, '.nii' ], 'file' )
    
    GRETNAPath  = fileparts( which( 'gretna.m' ) );
    GSMsk       = [ GRETNAPath, filesep, 'Mask', filesep, 'BrainMask_3mm.nii' ];
    GSMsk       = spm_vol( GSMsk );
    GSMsk       = spm_read_vols( GSMsk );
    GSMsk       = GSMsk(:) > 0.5;
    
    load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask.mat' );
    
    Nii = nifti( InputFile );
    VolumeCourse = reshape( double( Nii.dat ), [ Nii.dat.dim( 1, 1 )*Nii.dat.dim( 1, 2 )*Nii.dat.dim( 1, 3 ), Nii.dat.dim( 1, 4 ) ] )';
    
    GlobalSignal = mean( VolumeCourse( :, GSMsk ), 2 );
    MaskCourse = VolumeCourse( :, MaskIndex );
    
    PoolCourse = [ MaskCourse, GlobalSignal ];
    PoolCourse = PoolCourse - repmat( mean( PoolCourse ), [ size( PoolCourse, 1 ), 1 ] );
    PoolCourse = PoolCourse./repmat( std( PoolCourse, 0, 1 ), [ size( PoolCourse, 1 ), 1 ] );
    
    GSL = PoolCourse'*PoolCourse( :, end )/( size( PoolCourse, 1 ) - 1 );
    GSL( isnan( GSL ) ) = 0;
    GSL = GSL( 1:end - 1 );
    
    load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask_Header.mat' );
    Header.dt( 1 ) = 16;
    
    mkdir( [ OutputPath, filesep, 'GSL' ] );
    
    Header.fname = [ OutputPath, filesep, 'GSL', filesep, 'GSL_', name, '.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = GSL;
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );
    
    mkdir( [ OutputPath, filesep, 'zGSL' ] );
    
    Header.fname = [ OutputPath, filesep, 'zGSL', filesep, 'zGSL_', name, '.nii' ];
    Volume = double( MaskIndex );
    Volume( MaskIndex ) = 0.5*log( ( 1 + GSL )./( 1 - GSL ) );
    Volume = reshape( Volume, Header.dim( 1, 1 ), Header.dim( 1, 2 ), Header.dim( 1, 3 ) );
    spm_write_vol( Header, Volume );

end