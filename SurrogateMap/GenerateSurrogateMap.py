import numpy
from brainsmash.workbench.geo import volume
from brainsmash.mapgen.sampled import Sampled

coord_file = "\FunctionalConnectomeHubs\SurrogateMap\XYZ.txt"
output_dir = "\FunctionalConnectomeHubs\SurrogateMap"

filenames = volume(coord_file, output_dir)

brain_map = "\FunctionalConnectomeHubs\SurrogateMap\ZValue.txt"
gen = Sampled(x=brain_map, D=filenames['D'], index=filenames['index'], resample=True, n_jobs=6)
surrogate_maps = gen(n=1000)
numpy.savetxt( "\FunctionalConnectomeHubs\SurrogateMap\ZValue_Surrogate.txt", surrogate_maps, fmt="%10.6f", delimiter=",", header="")

brain_map = "\FunctionalConnectomeHubs\SurrogateMap\ZValue_NGS.txt"
gen = Sampled(x=brain_map, D=filenames['D'], index=filenames['index'], resample=True, n_jobs=6)
surrogate_maps = gen(n=1000)
numpy.savetxt( "\FunctionalConnectomeHubs\SurrogateMap\ZValue_NGS_Surrogate.txt", surrogate_maps, fmt="%10.6f", delimiter=",", header="")
