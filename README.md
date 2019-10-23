# Automotive-Headlights-Detection

A simple model to detect the presence of a vehicle in front (in two way street) using OpenCV Python 3.

**The model works by the following steps:**

1. Covert the image to grayscale
2. Blur the image
3. Set a thershold for the blurred image to remove low light component
4. Draw the outline of all remaining bright components
5. Compute the moment of images of the outline drawn
6. Using the moment to identify is the outline drawn is a headlight
7. Flag the image if car is found!
