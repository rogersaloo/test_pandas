## Fake document detection
The small project involves detection of unsimilarities between two documents usually an original agiainst an edited document. The use case can be in detection of edited Id cards, changed numbers on entry sheets and with good training on the model a detection of changes in the signatures is also possible.

### Steps
1. Obtaining the image as an entry
2. checking the format and the size of the image as a comparison to the specifications used during training.
3. changing the chape or the size of the image if the specifications do not match the anticipated specs used for training.
4. Converting the image to grayscale as it is able to capture more metadata relating to the image in terms of marks and edges.
5. Checking for a similarity index between the image and the pretrainned original image.
6. Checking if the image matches a threshhold set for similarity.
7. Drawing bounding rectangles to various aspects of the image. the rectangles capture marks spots and shape of letters and objects within the image. Addionally grabing the contours obtained from drawing the bounding triangles.
8. Getting a plot of the diffence in the threshold between the original pre-trainned image and the image being tested for fakeness.
9. Finally a comparison of the similarity score based on the original image to determine if there were any tampering with the new image. 

### How to use the repository
1. clone the repository
2. If you are using pip create a virtual environment in the root folder ```pip install imutils```
3. Cd into the virtual environment ```source env_name/bin/activate```
4. Install the requirement ```pip install -r requirements.txt```