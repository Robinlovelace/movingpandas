# MovingPandas

MovingPandas implements a Trajectory class and corresponding methods based on **GeoPandas**.

You can try MovingPandas in a MyBinder notebook - no installation required: 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/anitagraser/movingpandas/master)

## Introduction 

Common Simple Features-based data models where trajectories consist of geometries with timestamps can be readily implemented in GIS environments, but they suffer from a lack of support for the temporal dimension, such as functions for duration and speed.

In stark contrast, the Pandas data analysis library has been developed with a strong focus on time series. By choosing Pandas data structures (1D series and 2D DataFrames) as a base for MovingPandas, we gain access to the library’s built-in functionality, including: flexible indexing on timestamps and other column types; memory-efficient sparse data structures for data that is mostly missing or mostly constant; an integrated ‘group by’ engine for aggregating and transforming datasets, and moving window statistics (rolling mean, rolling standard deviation, etc.).

GeoPandas extends the data types that can be used in Pandas DataFrames, thus creating GeoDataFrames. Geometric operations on these spatial data types are performed by Shapely. Geopandas further depends on Fiona for file access (which enables direct reading of GeoDataFrames from common spatial file formats, such as GeoPackage or Shapefile), and descartes and matplotlib for plotting.

MovingPandas uses the following terminology. A *trajectory* is, or more correctly has, a time-ordered series of geometries. These
geometries and associated attributes are stored in a GeoDataFrame *df*. Furthermore, a trajectory can have a *parent* trajectory and can itself be the parent of successive trajectories. Raw unsegmented streams of movement data, as well as semantically meaningful subsections or other subsections, can therefore be represented as trajectories. Depending on the use case, the trajectory object can access a point-based or a line-based representation of its data. (Source: [0])

## Installation

Use the following steps to run the notebooks locally on your machine:

1. Install Anaconda
2. Clone the movingpandas repository
3. In Anaconda Navigator | Environments | Import select the movingpandas environment.yml from the cloned directory:

![image](https://user-images.githubusercontent.com/590385/62143367-2db14c00-b2f0-11e9-8cb9-fb7993b7f62e.png)

4. Wait until the environment is ready, then change to the Home tab and install Jupyter notebooks into the movingpandas environment
5. Launch Jupyter notebooks and navigate to the cloned directory to execute them
6. Now you can run the notebooks, experiment with the code and adjust them to your own data

## Publications

[0] Graser, A. (2019). MovingPandas: Efficient Structures for Movement Data in Python. GI_Forum ‒ Journal of Geographic Information Science 2019, 1-2019, 54-68. doi:10.1553/giscience2019_01_s54. URL: https://www.austriaca.at/rootcollection?arp=0x003aba2b
