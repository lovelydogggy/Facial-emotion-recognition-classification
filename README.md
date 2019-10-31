# Project: Can you recognize the emotion from an image of a face? 

### **Project summary**:  
+ In this project, we created an classification program that can recognize emotion from an image of a face. We 1) employed NMF and PCA as dimensionality reduction technique to improve classification accuracy and reduce model runtime, 2) implemented GBM as basline model, 3) implemented random forest, SVM and neural network, specifically, there are two parts in the neural network model, firstly we train a binary classification model, then for each category we train different models to classify corresponding emotions and 3) evaluated the performance gain of your proposed improvement against the baseline. We utilized tensorflow in python for improved model.
+ The accuracy rate for binary classifier and multiclass classifier in baseline GBM model are 0.65 and 0.37 respectively.For the improved SVM model the accuracy rate are 0.98 and 0.56 respectively, and the neural network model are 0.98 and 0.63 respectively, which are better than the baseline models.

