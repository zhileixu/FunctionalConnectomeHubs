require( xgboost )

AHBA <- read.table( "\\FunctionalConnectomeHubs\\AHBAprocessed\\AHBA1158x10027.csv", header = FALSE, sep = ',' )
Hub <- read.table( "\\FunctionalConnectomeHubs\\FigureS8\\FigureS8A\\Hub1158_Surrogate.csv", header = FALSE, sep = ',' )
HubTrain <- read.table( "\\FunctionalConnectomeHubs\\FigureS8\\FigureS8A\\Hub1158Train_Surrogate.csv", header = FALSE, sep = ',' )
HubTest <- read.table( "\\FunctionalConnectomeHubs\\FigureS8\\FigureS8A\\Hub1158Test_Surrogate.csv", header = FALSE, sep = ',' )

Fold <- 30
Step <- 0.05
OutputPath <- paste( "\\FunctionalConnectomeHubs\\FigureS8\\FigureS8A\\CV", sprintf( "%02d", Fold ), "Fold", sep="" )
dir.create( OutputPath )

for( RandSeed in 1:1000 )
{
	TrainData <- xgb.DMatrix( as.matrix( AHBA[unlist(HubTrain[RandSeed,]),] ), label = as.matrix( Hub[unlist(HubTrain[RandSeed,]), RandSeed] ) )
	
	CVModel <- xgb.cv( data = TrainData, nrounds = 1500, nfold = Fold, early_stopping_rounds = 50, prediction = TRUE, eta = Step, objective = "binary:logistic" )
	write.table( CVModel$pred, file = paste( OutputPath, "\\CV", sprintf( "%04d", RandSeed ), ".txt", sep="" ), row.names = FALSE, col.names = FALSE, quote = FALSE )
	write.table( CVModel$best_iteration, file = paste( OutputPath, "\\BestIteration", sprintf( "%04d", RandSeed ), ".txt", sep="" ), row.names = FALSE, col.names = FALSE, quote = FALSE )
	
	TrainModel <- xgboost( data = TrainData, nrounds = CVModel$best_iteration, eta = Step, objective = "binary:logistic" )
	Importance <- xgb.importance( model = TrainModel )
	write.table( Importance, file = paste( OutputPath, "\\Importance", sprintf( "%04d", RandSeed ), ".txt", sep="" ), row.names = FALSE, col.names = FALSE, quote = FALSE )
	
	TestData <- xgb.DMatrix( as.matrix( AHBA[unlist(HubTest[RandSeed,]),] ), label = as.matrix( Hub[unlist(HubTest[RandSeed,]), RandSeed] ) )
	Prediction <- predict( TrainModel, TestData )
	write.table( Prediction, file = paste( OutputPath, "\\Prediction", sprintf( "%04d", RandSeed ), ".txt", sep="" ), row.names = FALSE, col.names = FALSE, quote = FALSE )
}