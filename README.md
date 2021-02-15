# MCM 2021 Problem C
RRS (Random Forest + ResNet-18 CNN + Spatial Distribution Reproduction Model) - A combined model to evaluate the accuracy of the Asian Giant Hornet sightings reported in Washington State.

## Overview
This repository is cloned from the private one my team used for MCM/ICM 2021. I removed data from MCM and the figures that we used in our paper. But the data could be downloaded by the following instructions and the codes that plots the figure is preserved.  
  
The [Initial Commit](https://github.com/garywei944/aris_mcm_2021_c/tree/5cf04fa1d67088fad1c19d29a501d4486924cecf) is the version of codes that I implemented during the competition.

## Import Data
Please unzip and put `2021_MCM_Problem_C_Data` and `2021_MCM_Problem_C_Data` folder under the root directory. No need to change the name of the 2 folders. The data could be download at the [MCM Website](https://www.comap.com/undergraduate/contests/mcm/contests/2021/problems/)

## Set up environment
In short, the only required packages are
* `anaconda`
* `pytorch`
* `opencv`
* `imbalanced-learn`  
  
We'll be all good if you have already installed these dependencies in your environment.

### Conda Environment
`conda` is strongly commended to make and maintain python virtual environments. It's quite easy to make a new virtual environment in the project folder with the provided environment file `environment.yml` and the following command:
```
conda env create -p venv -f environment.yml
```
***Important:** please check the `environment.yml` file and make necessary modification if you want to use GPU for this project.*

### Notes
* The project is developed and tested under Windows 10 Enterprise Build 19042 and Ubuntu 20.04. The scripts should be compatible with all UNIX distributions(including maxOS).
* `spec-files_win-64.txt` contains the specific version and build number of dependencies I used on Windows 10 64-bit, CUDA 11.2.

## Contribution
The math models and codes in this repository is proposed and implemented by me. Due to policy concerns, I didn't upload our submitted paper here, but the paper is also contributed by [Gavin Duan](https://github.com/GavinDuan513) and [Yichong Liu](https://github.com/YiChong-Liu).

## TODO
* Create a main Jupyter Notebook
* Reconstruct the pipeline scripts
* Add detailed explanation for the models
* Make figures to describe the model
