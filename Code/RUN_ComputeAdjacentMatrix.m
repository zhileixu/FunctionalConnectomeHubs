function [ AdjacentMatrix ] = RUN_ComputeAdjacentMatrix( InputFile, Mask )

load( Mask );

Nii = nifti( InputFile );
VolumeCourse = reshape( double( Nii.dat ), [ Nii.dat.dim( 1, 1 )*Nii.dat.dim( 1, 2 )*Nii.dat.dim( 1, 3 ), Nii.dat.dim( 1, 4 ) ] )';

MaskCourse = VolumeCourse( :, MaskIndex );
MaskCourse = MaskCourse - repmat( mean( MaskCourse ), [ size( MaskCourse, 1 ), 1 ] );
MaskCourse = MaskCourse./repmat( std( MaskCourse, 0, 1 ), [ size( MaskCourse, 1 ), 1 ] );

AdjacentMatrix = MaskCourse'*MaskCourse/( size( MaskCourse, 1 ) - 1 );
AdjacentMatrix( isnan( AdjacentMatrix ) ) = 0;

end