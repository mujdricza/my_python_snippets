"""
https://www.datacamp.com/de/tutorial/the-cross-entropy-loss-function-in-machine-learning
"""
import math
import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import tensorflow as tf
import torch

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def generate_random_data(class_number: int = 2) -> tuple[np.ndarray, ...]:
     # create random training data
    X, y = make_classification(
        n_samples=10000,
        n_informative=10,
        n_classes=class_number,
        random_state=2022
    )

    # split into train and test
    X_new, X_test = X[:9000, :], X[9000:, ]
    y_new, y_test = y[:9000], y[9000:]

    X_train, X_val, y_train, y_val = train_test_split(
        X_new, y_new,
        test_size=0.3
    )
    print(f"Train data: {X_train.shape}\n\
    Train labels: {y_train.shape}\n\
    Test data: {X_test.shape}\n\
    Test labels: {y_test.shape}")

    """
    Train data: (6300, 20)
    Train labels: (6300,)
    Test data: (1000, 20)
    Test labels: (1000,)
    """
    return X_train, X_val, X_test, y_train, y_val, y_test


def build_model_tf(X_train: np.ndarray) -> tf.keras.Sequential:
    # building and training model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10,
                              input_shape=(X_train.shape[1],),
                              activation="relu"),
        tf.keras.layers.Dense(10,
                              activation="relu"),
        tf.keras.layers.Dense(1, activation="sigmoid")
    ])

    model.compile(
        loss="binary_crossentropy", # loss function here
        optimizer="adam",
        metrics=["accuracy"])

    return model


def fit_model_tf(
    tf_model: tf.keras.Model,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    epochs: int = 20
):
    history = tf_model.fit(X_train, y_train, epochs=epochs, validation_data=[X_val, y_val], verbose=0)
    return history


def plot_results_tf(tf_history):
    # plotting the loss of the models
    fig, ax = plt.subplots(figsize=(8,5))

    plt.plot(tf_history.history['loss'])
    plt.plot(tf_history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.xticks(np.arange(0,20, step=1))
    plt.legend(['train', 'val'], loc='upper right')
    # plt.show()
    plt.savefig(os.path.join(THIS_DIR, "tf_model_loss.png"))


def prepare_data_for_pytorch(X_train, X_val, X_test, y_train, y_val, y_test):
    # convert numpy arrays to tensors
    X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
    X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
    X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
    y_train_tensor = torch.tensor(y_train, dtype=torch.float32).reshape(-1, 1)
    y_val_tensor = torch.tensor(y_val, dtype=torch.float32).reshape(-1, 1)
    y_test_tensor = torch.tensor(y_test, dtype=torch.float32).reshape(-1, 1)
    return X_train_tensor, X_val_tensor, X_test_tensor, y_train_tensor, y_val_tensor, y_test_tensor


def build_model_pytorch(X_train: torch.Tensor) -> torch.nn.Module:

    # build the model
    input_dim = X_train.shape[1]
    hidden_dim = 10
    output_dim = 1

    model = torch.nn.Sequential(
        torch.nn.Linear(input_dim, hidden_dim),
        torch.nn.ReLU(),
        torch.nn.Linear(hidden_dim, hidden_dim),
        torch.nn.ReLU(),
        torch.nn.Linear(hidden_dim, output_dim),
        torch.nn.Sigmoid(),
    )

    print(model)

    """
    Sequential(
      (0): Linear(in_features=20, out_features=10, bias=True)
      (1): ReLU()
      (2): Linear(in_features=10, out_features=10, bias=True)
      (3): ReLU()
      (4): Linear(in_features=10, out_features=1, bias=True)
      (5): Sigmoid()
    )
    """
    return model


def fit_model_pytorch(
    pytorch_model,
    X_train,
    y_train,
    X_val,
    y_val,
    epochs: int = 20
) -> tuple[list[float], ...]:

    loss_fn = torch.nn.BCELoss()  # use binary cross entropy as criterion
    optimizer = torch.optim.Adam(pytorch_model.parameters(), lr=0.001)

    m = math.ceil(epochs*0.1) # for printing epoch status
    train_losses = []
    val_losses = []

    # https://docs.pytorch.org/tutorials/beginner/pytorch_with_examples.html
    for t in range(epochs):
        # Forward pass: Compute predicted y by passing x to the model
        y_pred_train = pytorch_model(X_train)
        y_pred_val = pytorch_model(X_val)

        # Compute and print loss
        loss_train = loss_fn(y_pred_train, y_train)
        if t % m == min(m-1, 0):
            print(t, loss_train.item())
        train_losses.append(loss_train.tolist())
        loss_val = loss_fn(y_pred_val, y_val)
        val_losses.append(loss_val.tolist())

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss_train.backward()
        optimizer.step()

    print(f"Result: {pytorch_model}")
    return train_losses, val_losses


def plot_results_pytorch(train_loss, val_loss):
    # plotting the loss of the models
    fig, ax = plt.subplots(figsize=(8,5))
    plt.plot(train_loss)
    plt.plot(val_loss)
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.xticks(np.arange(0,20, step=1))
    plt.legend(['train', 'val'], loc='upper right')
    # plt.show()
    plt.savefig(os.path.join(THIS_DIR, "pytorch_model_loss.png"))


def main_tf(data: tuple[np.ndarray, ...], epochs: int) -> None:
    print(f"TF experiment")
    X_train, X_val, X_test, y_train, y_val, y_test = data
    print(f"Data: {X_train.shape=}, {X_val.shape=}, {X_test.shape=}")
    tf_model = build_model_tf(X_train)
    print(f"Model: {tf_model}")
    tf_history = fit_model_tf(tf_model, X_train, y_train, X_val, y_val, epochs)
    print(f"Model trained with {epochs} epochs.")
    plot_results_tf(tf_history)
    print(f"Output written to {THIS_DIR}.")


def main_pytorch(data: tuple[np.ndarray, ...], epochs: int) -> None:
    print(f"PT experiment")
    X_train, X_val, X_test, y_train, y_val, y_test = data
    X_train, X_val, X_test, y_train, y_val, y_test = prepare_data_for_pytorch(X_train, X_val, X_test,y_train, y_val, y_test)
    print(f"Data: {X_train.shape=}, {X_val.shape=}, {X_test.shape=}")
    pytorch_model = build_model_pytorch(X_train)
    print(f"Model: {pytorch_model}")
    train_losses, val_losses = fit_model_pytorch(pytorch_model, X_train, y_train, X_val, y_val, epochs)
    print(f"Model trained with {epochs} epochs.")
    plot_results_pytorch(train_losses, val_losses)
    print(f"Output written to {THIS_DIR}.")


if __name__ == "__main__":
    data = generate_random_data()
    epochs = 200
    main_tf(data, epochs)
    main_pytorch(data, epochs)
