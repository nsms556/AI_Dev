# There are a lot of files here...what am I looking at?
This assignment contains 3 types of files:
  1. `*.ipynb`: This is where all the assignment problems, as well as most of my solutions, live.
  2. `cs231/`: This is where all the helper python files live. Some of the notebooks require use to modify/implement functions, within this directory, as part of our solution.  
  3. `assignment1.md`: This is the original assignment handout.

# More on each of the ipynbs
The ipynbs are meant to be completed in the following order:
  1. `knn.ipynb`: Implement a **k-Nearest Neighbor** classifier. Train the classifier on the **CIFAR10** dataset. Hyperparameter is tuned using a **grid search** which is evaluated with **k-fold cross validation**.
  2. `svm.ipynb`: Implement a **Support Vector Machine** classifier. Train the classifier on the **CIFAR10** dataset with **Stochastic Graidient Descent**. Hyperparameters are tuned using a **grid search** which is evaluated with **holdout cross validation**.
  3. `softmax.ipynb`: Implement a **Softmax** classifier. Train the classifier on the **CIFAR10** dataset using **Stochastic Gradient Descent**. Hyperparameters are tuned using a **random search** which is evaluated with **holdout cross validation**.
  4. `two_layer_net.ipynb`: Implement a two layer **Neural Network** classifier. Train the classifier on the **CIFAR10** dataset using **Stochastic Gradient Descent with momentum**. Hyperparameters are tuned using a **random search** which is evaluated with **holdout cross validation**.
  5. `features.ipynb`: Train a **Support Vector Machine** and **Neural Network** classifier on the **CIFAR10** dataset. Rather than training on pixel values, train the classifiers on **extracted features**; for each image, compute the **Histogram of Oriented Gradients** as well as a **color histogram** using the hue channel in HSV color space.
