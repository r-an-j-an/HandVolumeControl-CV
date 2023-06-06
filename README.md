# Hand Volume Control - CV

This project controls the volume of the system using fingertips using OpenCV libraries.

## Description

The project consists of two Python scripts: `HANDTRACKINGMODULE.py` and `VolumeControl.py`. The `HANDTRACKINGMODULE.py` script is responsible for detecting and tracking the hand using the Mediapipe library. The `VolumeControl.py` script uses the hand tracking module to calculate the distance between the thumb and index finger tips and adjusts the system volume based on the distance.
## Screeshots:
![image](https://github.com/r-an-j-an/HandVolumeControl-CV/assets/100189617/ce126c2a-3afa-412e-8671-5b7d3bfac1b1)
![image](https://github.com/r-an-j-an/HandVolumeControl-CV/assets/100189617/c4f8aa99-6769-46de-9ce9-f7dfd287ade6)
![image](https://github.com/r-an-j-an/HandVolumeControl-CV/assets/100189617/eb430b94-81fa-4346-8f71-75d4ed107c61)
![image](https://github.com/r-an-j-an/HandVolumeControl-CV/assets/100189617/314daacf-e608-4fce-b86a-0e7f2c13449d)


## Prerequisites

Before running the scripts, make sure you have the following libraries installed:

- OpenCV
- Mediapipe
- Numpy
- Math
- comtypes
- pycaw

You can install these libraries using pip:

```bash
pip install opencv-python
pip install mediapipe 
pip install numpy 
pip install pycaw
```
## Usage

1.Run the VolumeControl.py script.
2.Place your hand in front of the camera, ensuring that your palm is facing the camera.
3.Adjust the volume by moving your thumb and index finger closer or farther apart.
4.The system volume will change based on the distance between your fingers.

## Contributers
-Aditya Ranjan
