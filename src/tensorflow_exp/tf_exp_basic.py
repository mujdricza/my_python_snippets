"""
Basic classification experiment.
"""
from typing import Any, Dict, List, Tuple
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report


def get_data(data_name: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, List[str]]:  # TODO check type
    if data_name == "fashion_mnist":
        dataset: tf.keras.dataset.Dataset = tf.keras.datasets.fashion_mnist  # TODO check type
        (train_items, train_labels), (test_items, test_labels) = dataset.load_data()
        train_items = train_items / 255.0  # normalize into [0,1]
        test_items = test_items / 255.0
        label_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
    else:
        raise ValueError("Unhandled dataset %s" % data_name)

    return train_items, train_labels, test_items, test_labels, label_names



def get_trainable_model() -> tf.keras.models.Model:

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation=tf.nn.relu),
        tf.keras.layers.Dense(10)
    ])
    return model


def get_probability_model(model: tf.keras.models.Model | None) -> tf.keras.models.Model:
    if model is None:
        model = get_trainable_model()
    probability_model = tf.keras.models.Sequential([
        model,
        tf.keras.layers.Softmax()
    ])
    return probability_model


def compile_model(model: tf.keras.models.Model) -> None:
    model.compile(
        optimizer="adam",  # TODO check also ok?: tf.keras.optimizers.AdamW(),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=["accuracy"]
    )


def learn_model(
    model: tf.keras.models.Model,
    train_items: np.ndarray,
    train_labels: np.ndarray,
    epochs: int = 10,
    verbosity: int | str = 2
) -> tf.keras.callbacks.History:
    history = model.fit(train_items, train_labels, epochs=epochs, verbose=verbosity)
    return history




def predict_data(
    probability_model: tf.keras.models.Model,
    items: np.ndarray,
    verbosity: int | str = 2
) -> np.ndarray:

    predictions: np.ndarray = probability_model.predict(items, verbose=verbosity)
    print(f"EMM {type(predictions)=}")
    return predictions


def predict_item(
    probability_model: tf.keras.models.Model,
    item: np.ndarray,
    true_label: np.ndarray,
) -> List:  # TODO check type
    predictions = probability_model(item)  # ?

    return predictions


def evaluate_data(
    model: tf.keras.models.Model,
    items: np.ndarray,
    labels: np.ndarray,
    verbosity: int | str = 2
) -> Dict[str, float]:

    # e.g. result_dict = {'accuracy': 0.9783999919891357, 'loss': 0.07219784706830978}
    # with return_dict=False (default): result = [0.07219784706830978, 0.9783999919891357]
    result_dict: Dict[str, float] = model.evaluate(items, labels, return_dict=True, verbose=verbosity)
    return result_dict


def evaluate_predictions(
    probability_model: tf.keras.models.Model,
    items: np.ndarray,
    labels: np.ndarray,
    label_names: List[str],
    verbosity: int | str = 2
) -> List[Dict[str, Any]]:
    predictions: np.ndarray = probability_model.predict(items, verbose=verbosity)
    assert len(items) == len(labels) == len(predictions)

    results = []
    for item, label_idx, prediction in zip(items, labels, predictions):
        pred_idx = np.argmax(prediction)
        expected_label = label_names[label_idx]
        predicted_label = label_names[pred_idx]
        #print(f"EMM {expected_label=}, {predicted_label=}")
        result = {
            "item": item,
            "expected_label": expected_label,
            "predicted_label": predicted_label,
            "prediction": prediction
        }
        results.append(result)

    exp_labels = [res["expected_label"] for res in results]
    prd_labels = [res["predicted_label"] for res in results]
    report = classification_report(exp_labels, prd_labels)
    return results, report


def main():
    # hyperparameters
    data_name: str = "fashion_mnist"
    epochs = 2
    verbosity = 2  # 2 == one line per batch or epoch

    # data
    train_items, train_labels, test_items, test_labels, label_names = get_data(data_name=data_name)
    print(f"Data: training: {len(train_items)}; test: {len(test_items)}")

    # model
    model = get_trainable_model()
    compile_model(model)
    model_history = learn_model(model, train_items, train_labels, epochs=epochs, verbosity=verbosity)
    model_params = model_history.params
    epoch_acc_and_loss = model_history.history
    print(f"Model trained for {epochs} epochs on dataset {data_name}.")
    print(f"Model parameters: {model_params}")
    print(f"Model accuracies per epoch: {epoch_acc_and_loss["accuracy"]}")
    print(f"Model losses per epoch: {epoch_acc_and_loss["loss"]}")

    # evaluation
    training_eval = evaluate_data(model, train_items, train_labels, verbosity=verbosity)
    test_eval = evaluate_data(model, test_items, test_labels, verbosity=verbosity)
    print(f"Training eval: {training_eval}")
    print(f"Test eval: {test_eval}")

    # prediction
    predictions = predict_data(model, test_items, verbosity=verbosity)
    prediction_results, classification_report = evaluate_predictions(
        probability_model=model, items=test_items, labels=test_labels, label_names=label_names, verbosity=verbosity)
    #print(f"Prediction results: {prediction_results}")
    print(f"Classification report:\n{classification_report}")


if __name__ == "__main__":
    main()
