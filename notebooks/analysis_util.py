import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_classes(y):
  return [list(i).index(max(i)) for i in y]


def visualize_training_results(results):
    history = results.history
    plt.figure()
    plt.plot(history['val_loss'])
    plt.plot(history['loss'])
    plt.legend(['val_loss', 'loss'])
    plt.title('Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.show()
    
    plt.figure()
    plt.plot(history['val_acc'])
    plt.plot(history['acc'])
    plt.legend(['val_acc', 'acc'])
    plt.title('Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.show()


def misclass_report(y_true, y_hat, dummy_to_unicode):
  trues = list(set(y_true))
  misclassifications = {}
  for char in trues:
    misclassifications[char] = []
  for result in zip(y_true, yhat_test):
    if result[0] != result[1]:
      misclassifications[result[0]] += [result[1]]
  for char in misclassifications:
    misclassifications[char] = sorted(misclassifications[char])
    misclassifications[char] = [dummy_to_unicode[i] for i in misclassifications[char]]
    misclassifications[char] = ['rare' if i=='rare' else chr(int(i[2:], 16)) for i in misclassifications[char]]
  return misclassifications