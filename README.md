# Japanese Kuzushiji Character Classification


## Getting Started
### Contents of Repository

* **images** is a directory containing images used in this README.
* **notebooks** is a directory containing Jupyter notebooks each for (1) preprocessing, (2) exploratory data analysis, (3) a baseline CNN model, (4a-c) transfer learning models, and (5) a fully convolutional network; as well as two modules of helper functions (`analysis_util.py` and `my_classes.py`).
* **presentation.pdf** contains my powerpoint presentation for a non-technical audience.


### Prerequisites

The standard packages for data analysis are required–NumPy, Pandas, and Matplotlib––as well as [scikit-learn](https://scikit-learn.org/stable/index.html#) and [Keras](https://keras.io/) for classification models. Below are examples of their installations using Anaconda.

```
$ conda install -c anaconda numpy
$ conda install pandas
$ conda install -c conda-forge matplotlib
$ conda install scikit-learn
$ conda install -c conda-forge keras
```

## Built With

[Jupyter Notebook](https://jupyter.org) - Documents containing live code and visualizations.

## Contributing

Due to the nature of the assignment, this project is not open to contributions. If, however, after looking at the project you'd like to give advice to someone new to the field and eager to learn, please reach out to me at [stephen.t.lanier@gmail.com].

## Author

**Stephen Lanier** <br/>
[GitHub](https://github.com/stlanier) <br/>
[LinkedIn](https://www.linkedin.com/in/stephen-lanier/)



## Acknowledgments

<a href="https://flatironschool.com"><img src="images/flatiron.png" width="80" height="40"  alt="Flatiron School Logo"/></a>
Special thanks to Jacob Eli Thomas, Victor Geislinger, and Jeff Herman, my instructors at [Flatiron School](https://flatironschool.com), for their encouragement, instruction, and guidance.

<a href="https://www.kaggle.com"><img src="images/kaggle.png" width="80" height="40"  alt="Kaggle Logo"/></a>
Thanks to [Kaggle](https://www.kaggle.com) for access to data from [Kuzushiji Recognition](https://www.kaggle.com/c/kuzushiji-recognition)
