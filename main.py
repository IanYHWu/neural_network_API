import numpy as np
import NN_api
import matplotlib.pyplot as plt


def main():

    # load in data and apply appropriate transformations
    training_data = np.load('data/fashion-train-imgs.npz')
    training_labels = np.load('data/fashion-train-labels.npz')
    validation_data = np.load('data/fashion-dev-imgs.npz')
    validation_labels = np.load('data/fashion-dev-labels.npz')

    training_data = np.reshape(training_data, (784, 12000)).T
    training_labels = np.reshape(training_labels, (-1, 1))
    validation_data = np.reshape(validation_data, (784, 1000)).T
    validation_labels = np.reshape(validation_labels, (-1, 1))

    # plt.imshow(training_data[8].reshape((28, 28)), cmap='gray')
    # plt.show()

    model = NN_api.Dense()  # initialise network
    # add layers (input: 784 -> hidden relu: 128 -> hidden relu: 32 -> output sigmoid: 1)
    model.add_layer('relu', 784, 128)
    model.add_layer('relu', 128, 32)
    model.add_layer('sigmoid', 32, 1)
    # compile and then fit to training data
    model.set_name('128_32_1_test')
    model.compile(optimiser='gradient_descent', loss='MSE', metric='binary_accuracy', learning_rate=0.01)
    results = model.fit(input_data=training_data, labels=training_labels, epochs=50, batch_size=12, validate=True,
                        validation_data=validation_data, validation_labels=validation_labels, save_data=True)

    # # code for hyperparameter tuning
    # tune_model = NN_api.Dense()  # initialise network and add layers
    # tune_model.add_layer('relu', 784, 256)
    # tune_model.add_layer('relu', 256, 32)
    # tune_model.add_layer('relu', 32, 8)
    # tune_model.add_layer('sigmoid', 8, 1)
    #
    # tuner = NN_api.GridSearchTuner()  # create tuner object
    # tuner.set_model(tune_model)  # set model for tuner object
    # tuner.learning_rate_grid([0.01, 0.1])  # provide grid for learning rate
    # tuner.batch_size_grid([1, 12000])  # provide grid for batch size
    # # perform grid search!
    # tuner.search(training_data=training_data, labels=training_labels, validation_data=validation_data,
    #              validation_labels=validation_labels, epochs=10, optimiser='gradient_descent', loss='MSE',
    #              metric='binary_accuracy')
    # print(tuner.get_best_params())


if __name__ == '__main__':
    main()
