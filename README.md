# Augmented Reality Lipstick

This is an AR application that applies lipstick on the user's face using the webcam feed. It works by detecting face landmarks and masking the lip region, then applying a color there.  

![python_lipstick](https://user-images.githubusercontent.com/60410055/147869939-0eefced7-d0c6-478d-a38a-8f68cfeec706.gif)


Dlib's face detection algorithms are utlized in addition to OpenCV for computer vision and image processing methods. This application was a test for me to get familiar with Dlib, but I decided to do my full project in C++ with OpenGL to achieve greater control over the graphics pipeline, and create a face mesh with custom textures.  
  
Check out the real project here: https://github.com/somxr/ar-facemesh-opengl-dlib
