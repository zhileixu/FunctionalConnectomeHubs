function RUN_PoolMeasurement( InputFile, OutputFile, SubjectList, IDLength )

load( '/FunctionalConnectomeHubs/BrainMask/GrayMatter_WithoutCER_Mask.mat' );
VoxelNumber = sum( MaskIndex > 0.5 );

if ~exist( [ OutputFile, '.mat' ], 'file' )
    SubjectNumber = length( SubjectList );
    Measurement = zeros( SubjectNumber, VoxelNumber );
    
    for SubjectIndex = 1:SubjectNumber
        Nii = nifti( [ InputFile, '_', num2str( SubjectList( SubjectIndex ), [ '%.', IDLength, 'd' ] ), '.nii' ] );
        Nii = Nii.dat(:);
        Measurement ( SubjectIndex, : ) = Nii( MaskIndex );
    end
    
    save( [ OutputFile, '.mat' ], 'Measurement', '-v7.3' );
end

end