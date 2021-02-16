# NAPPN 2021 Conference PlantCV virtual workshop materials

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/danforthcenter/plantcv-nappn2021-workshop.git/main)

This repository contains materials used in the PlantCV workshop (February 16, 2021 from 8:30am to 11:00am CST) in the 2021 NAPPN Annual Conference (https://www.nappn2021.org/).

## Image analysis in Python with PlantCV

This workshop aims to provide a virtual, hands-on, and interactive introduction to image analysis with Python and PlantCV (https://plantcv.danforthcenter.org/). Participants will utilize interactive coding environments in the cloud (Jupyter notebooks) to gain hands-on experience with importing and working with image data in Python using PlantCV and other open-source tools. The learning goals of the workshop are: 1) participants will gain an understanding of image data structure and the primary tools available in Python to work with image data; 2) participants will learn how to use PlantCV to build image analysis workflows; 3) participants will learn how to process image data in parallel using PlantCV workflows; and 4) participants will gain a brief introduction to visualizing phenotypic measurements extracted from a PlantCV workflow analysis.

### Agenda

1. Introduction
2. Working with images in Python
3. Develop PlantCV image analysis workflows
4. Parallel image analysis
5. Visualization of phenotypic measurements

**Presenters**: [Malia Gehan](https://www.danforthcenter.org/our-work/principal-investigators/malia-gehan/),
[Haley Schuhl](https://twitter.com/HaleySchuhl),
and [Noah Fahlgren](https://www.danforthcenter.org/our-work/principal-investigators/noah-fahlgren/)

**Project website**: https://plantcv.danforthcenter.org/

**Twitter**: [@plantcv](https://twitter.com/plantcv)

### Detailed outline

1. The `START_HERE.ipynb` is a Jupyter notebook template for building a PlantCV workflow.
We will start here and fill it out together. `completed_multi_plant_notebook.ipynb` is
a completed workflow that you can use as a reference or if you follow the workshop
afterwards.
2. We will use the Terminal to convert the finished workflow into a Python script using
the command `jupyter nbconvert --to python START_HERE.ipynb`.
3. We will edit the Python script to polish it into a functioning workflow script.
`completed_multi_plant_notebook.py` is included as a reference.
4. We will use the notebook `parallel_configuration.ipynb` to create a configuration
template and use Jupyter's text editor to edit it. `multi-plant-analysis.config` is
included as a reference.
5. We will use the Terminal to run our workflow on the full image dataset using the
command `plantcv-workflow.py --config multi-plant-analysis.config`.
6. The output of running PlantCV on the full dataset is included in `multi-plant-results.json`.
7. We will convert the JSON output file to comma-separated (CSV) format using the
Terminal and the command `plantcv-utils.py json2csv -j multi-plant-results.json -c results`.
8. We will use the notebook `plot_results.ipynb` to visualize the results.

## Citations
Veley KM, Berry JC, Fentress SJ, Schachtman DP, Baxter I, Bart R. 2017. High-throughput profiling and analysis of plant responses over time to abiotic stress. Plant direct 1:e00023. DOI: [10.1002/pld3.23](https://doi.org/10.1002/pld3.23).

Gehan MA, Fahlgren N, Abbasi A, Berry JC, Callen ST, Chavez L, Doust AN, Feldman MJ, Gilbert KB, Hodge JG, Hoyer JS, Lin A, Liu S, Lizárraga C, Lorence A, Miller M, Platon E, Tessman M, Sax T. 2017. PlantCV v2: Image analysis software for high-throughput plant phenotyping. PeerJ 5:e4088. DOI: [10.7717/peerj.4088](https://doi.org/10.7717/peerj.4088).

Fahlgren N, Feldman M, Gehan MA, Wilson MS, Shyu C, Bryant DW, Hill ST, McEntee CJ, Warnasooriya SN, Kumar I, Ficor T, Turnipseed S, Gilbert KB, Brutnell TP, Carrington JC, Mockler TC, Baxter I. 2015. A versatile phenotyping system and analytics platform reveals diverse temporal responses to water availability in Setaria. Molecular Plant 8:1520–1535. DOI: [10.1016/j.molp.2015.06.005](https://doi.org/10.1016/j.molp.2015.06.005).
