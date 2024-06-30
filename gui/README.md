
# Overview:
We divide the GUI up into several pieces in an effort to practice the separation of concerns. If you plan to contribute to this project, please follow our practice. (Currently, this practice is not even fully respected by myself, but we're working on fixing that.) The division is performed like so:

1. graphs
2. modules
3. statics
4. tabs
5. threads
6. widgets

## Graphs:

These are nothing more than reusable `pyqtgraph` components. You should treat them like you would a Vue.js component; think about reusing a single graph component for several tabs. All we are doing here is handling the logic of constructing a graph and populating it with data.

## Modules:

These are just functions that do calculations on data. You should probably not do a lot of calculations before 

## Statics:

Any variable that doesn't ever change should be called a "static variable." Please list them here.

## Tabs:

Only the `PyQT5` logic that goes into coding a particular tab should go here. In our case, that is mostly configuring the layout of a given tab. Remember: no calculations should go into these files.

## Threads:

Who knows what this is?

## Widgets:

Another annoying thing about `PyQT5`. If nothing else fits, it's probably a `PyQT5` widget, and should go here.

# `.npz` Keys:

The `.npz` filetype is a NumPy one. It is basically just a bunch of NumPy arrays all zipped up. We can use `np.load()` in code to unzip them. However, there are specific keys that you just have to know because we are not really in control of writing these `.npz` files. The relevant keys are:

## `file_output_data`:

`file_output_data`: Contains most of the physics information. There is substructure to this data. It's not actually clear at all what is happening, but here is our guess:

Every row in `file_output_data` corresponds to an event in a given spill. Then, every column of `file_output_data` corresponds to some relevant physics or computational quantity. Here is what we know according to an ancient QTracker README file:

(These are column numbers.)

1. Probability that the event has no reconstructable muons.
2. Probability that the event has one reconstructable muon.
3. Probability that the event has two reconstructable muons of the same sign.
4. Probability that the event has two reconstructable muons of opposite signs (dimuon classification).
5. Probability that the event has three reconstructable muons of the same sign.
6. Probability that the event has three reconstructable muons, two of the same sign, one of the opposite sign.
7. $p_{x}$ of the positive muon with no assumptions about where the vertex was (the vertex position).
8. $p_{y}$ of the positive muon with no assumptions about where the vertex was.
9. $p_{z}$ of the positive muon with no assumptions about where the vertex was.
10. $p_{x}$ of the negative muon with no assumptions about where the vertex was.
11. $p_{y}$ of the negative muon with no assumptions about where the vertex was.
12. $p_{z}$ of the negative muon with no assumptions about where the vertex was.
13. (?) Vertex $x-$ position of the dimuon pair with no assumptions about where the vertex was.
14. (?) Vertex $y-$ position of the dimuon pair with no assumptions about where the vertex was.
15. (?) Vertex $z-$ position of the dimuon pair with no assumptions about where the vertex was.
16. $p_{x}$ of the positive muon assuming the dimuon was produced along the beamline.
17. $p_{y}$ of the positive muon assuming the dimuon was produced along the beamline.
18. $p_{z}$ of the positive muon assuming the dimuon was produced along the beamline.
19. $p_{x}$ of the negative muon assuming the dimuon was produced along the beamline.
20. $p_{y}$ of the negative muon assuming the dimuon was produced along the beamline.
21. $p_{z}$ of the negative muon assuming the dimuon was produced along the beamline.
22. (?) Vertex $x-$ position of the dimuon pair assuming the dimuon was produced along the beamline.
23. (?) Vertex $y-$ position of the dimuon pair assuming the dimuon was produced along the beamline.
24. (?) Vertex $z-$ position of the dimuon pair assuming the dimuon was produced along the beamline.
25. $p_{x}$ of the positive muon with no assumptions about where the vertex was (the vertex position).
26. $p_{y}$ of the positive muon with no assumptions about where the vertex was.
27. $p_{z}$ of the positive muon with no assumptions about where the vertex was.
28. $p_{x}$ of the negative muon with no assumptions about where the vertex was.
29. $p_{y}$ of the negative muon with no assumptions about where the vertex was.
30. $p_{z}$ of the negative muon with no assumptions about where the vertex was.
31. $P(\text{dimuon originated in the dump})$
32. $P(\text{dimuon originated in the target})$
33. Run ID
34. Event ID
35. Spill ID
36. (?) Trigger bit
37. Target Position
38. (?) Turn ID
39. RFID
40-72. Intensity
73-76. Number of trigger roads
77-131. Number of hits per detector before timing cuts.

## `hit_matrix`:

This is an array of $N \times M$ matrices (array of arrays). The outermost index refers to the *event number*. Then, for every event number, we have a $N \times M$ matrix. The rows of the matrix refer to the *detector ID* and the columns refer to the *element ID* in that given detector ID. 

There is a subtlety in the data that allows us to fix the number $M$, but dealing with this in practice is a pain in the ass. It turns out that $M = 200$, or something close to that. That is because there are detectors with $200$ elements and no more. Those detectors have the most element IDs as any other detector. This means that, for a given detector ID, you are not guaranteed that it will have all $200$ element IDs; some detectors only have as many as $30$ element IDs. Nevertheless, becaue we like to make things difficult, columns corresponding to element IDs of given detectors are *still populated* with a number so that we can deal with a matrix-type datatype.

As an explicit example, let's say `detector_ID = 50`. It turns out that the 50th detector ID only has $100$ elements. This means that, for the next $100$ entries, `element_ID[100:200] = 0`; they are redundant entries.

## `Tracks`:
Who the fuck knows? Not I. Someone else please document this.