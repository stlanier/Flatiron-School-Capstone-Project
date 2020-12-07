import numpy as np
import keras

class DataGenerator(keras.utils.Sequence):
    'Generates data for Keras'
    def __init__(self, list_IDs, imgs, labels, batch_size=1, n_channels=1,
                 n_classes=514, shuffle=False):
        'Initialization'
        self.imgs = imgs
        self.labels = labels
        self.list_IDs = list_IDs
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.shuffle = shuffle
        self.on_epoch_end()

    def __len__(self):
        'Denotes the number of batches per epoch'
        return len(self.list_IDs)

    def __getitem__(self, index):
        'Generate one batch of data'
        # Generate indexes of the batch
        # indexes = self.indexes[index]

        # Find list of IDs
        ID = self.list_IDs[index]

        # Generate data
        X, y = self.__data_generation(ID)

        return X, y

    def on_epoch_end(self):
        'Updates indexes after each epoch'
        self.indexes = np.arange(len(self.list_IDs))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __data_generation(self, ID):
        'Generates data containing batch_size samples' 
        dim = self.imgs[ID].size
        X = np.asarray(self.imgs[ID]).reshape(*dim, 1)
        y = self.labels[ID]


        return X, keras.utils.to_categorical(y, num_classes=self.n_classes)
