# Project: Can you recognize the emotion from an image of a face? 

### **Project summary**:  
+ In this project, we created an classification program that can recognize emotion from an image of a face. We 1) employed NMF and PCA as dimensionality reduction technique to improve classification accuracy and reduce model runtime, 2) implemented GBM as basline model, 3) implemented random forest, SVM and neural network, specifically, there are two parts in the neural network model, firstly we train a binary classification model, then for each category we train different models to classify corresponding emotions and 4) evaluated the performance gain of your proposed improvement against the baseline. We utilized tensorflow in python for improved model.

+ The accuracy rate for binary classifier (to classify simple or compound emotion) in baseline GBM model is 65%.For the improved SVM model the accuracy rate is 98%, and the neural network model is 96%, which are better than the baseline models.

+ Using the binary label we created above, we conduct simple emotion classification and compound emotion classification respectively. For the improved SVM model, the accuracy rates are 75% and 46%; while in GBM and Random Forest they improve to 85%, 57% and 83%, 55%. Using votingclassifier containing GBM and Random Forest leads to 85% and 60%, which achiving an overall accuracy of 69.2%. The neural network models would continously cause 88% and 63% accuracy, and 71% for overall accuracy.

