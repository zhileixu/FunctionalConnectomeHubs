##
FunctionalConnectomeHubs

Date 11/4/2022

First revision date 30/7/2022

E-mail: zhileixu@163.com

##
This repository provides code and source data that support the findings of the article entitled "Mapping Consistent, Reproducible, and Transcriptionally Relevant Functional Connectome Hubs of the Human Brain" by Xu et al.

A preprint of the article is available at https://doi.org/10.1101/2021.11.29.470494

##
AHBAprocessed Folder:

The preprocessed AHBA dataset, downloaded from https://doi.org/10.6084/m9.figshare.6852911

##
BrainMask Folder: 

The gray matter mask used in the article.

##
BrainSpanAtlas Folder:

The normalized BrainSpan Atlas dataset, downloaded from http://brainspan.org/static/download.html

##
Code Folder:

1. Resting-state Functional MRI Preprocessing:
	
	PIPE_Preproces.m
	
	RUN_Preproces.m

2. Functional Connectivity Strength (FCS):
	
	PIPE_FCS.m
	
	RUN_FCS.m
	
	RUN_ComputeAdjacentMatrix.m
	
	PIPE_Regression.m
	
	RUN_PoolMeasurement.m
	
	RUN_Regression.m

3. Random-Effects Meta-Analysis:
	
	PIPE_MetaAnalysis.m
	
	RUN_MetaAnalysis.m
	
	RUN_REMA.m

4. Mapping Seed-to-Whole-Brain Connectivity Profiles of Brain Hubs:
	
	PIPE_SeedBasedFC.m
	
	RUN_SeedBasedFC.m

5. Global Signal Localization (GSL):
	
	PIPE_GSL.m
	
	RUN_GSL.m

##
SurrogateMap Folder: 

Code for generating surrogate maps of the hub distribution map in Figure 2B and Figure S9A.

##
Figure Folder: 

Code, source NIfTI file, and source data of the Figures 1 to 6 and Figures S1 to S11 in the article.
