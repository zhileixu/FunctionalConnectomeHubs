function [ REMA ] = RUN_REMA( Beta, SE )

SiteNumber = size( SE, 1 );
df = SiteNumber - 1;

REMA.Vi = SE.^2;
REMA.Wi = 1./REMA.Vi;

REMA.Q = sum( REMA.Wi.*Beta.^2 ) - ( ( sum( REMA.Wi.*Beta ) ).^2 )./( sum( REMA.Wi ) );
REMA.TSquare = max( ( REMA.Q - df )./( sum( REMA.Wi ) - ( sum( REMA.Wi.^2 ) )./( sum( REMA.Wi ) ) ), 0 );
REMA.ISquare = max( ( REMA.Q - df )./REMA.Q, 0 );

REMA.ViStar = REMA.Vi + REMA.TSquare( ones( SiteNumber, 1 ), : );
REMA.WiStar = 1./REMA.ViStar;

REMA.MStar = ( sum( REMA.WiStar.*Beta ) )./( sum( REMA.WiStar ) );
REMA.VMStar = 1./( sum( REMA.WiStar ) );
REMA.SE_MStar = REMA.VMStar.^0.5;

end