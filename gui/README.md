
# Overview:
1. All the raw data comes as `.root` files from `/data4/e1039_data/online/sraw/`.

2. QTracker is always running, apparently. It detects if there's a new file in the above directory and performs reconstruction analysis on it. Where the fuck does it go?

# `.npy` Files:
Earlier, the reconstructed files were `.npy`-type. 

The fucking `.npz` files are annoying as shit. Basically, we have to memorize their structure:

They are rank-two matricies with the rows as `event number` and the columns corresponding to the kinematic/measured quantities.

# `.npz` Keys:

`file_output_data`: Contains most of the physics information.

`file_output_data`: WHo the fuck knows?

`file_output_data`: Who knows?

# `.npz` Column Values:

Column 28: Positive Muon $p_{x}$
Column 29: Positive Muon $p_{y}$
Column 30: Positive Muon $p_{z}$
Column 31: Negative Muon $p_{x}$
Column 32: Negative Muon $p_{y}$
Column 33: Negative Muon $p_{z}$