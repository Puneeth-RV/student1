from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def knn():
    # Load Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split dataset
    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train KNN (K = 5)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(x_train, y_train)

    # Predict
    y_pred = model.predict(x_test)

    # Accuracy
    print("Accuracy:", accuracy_score(y_test, y_pred))

    # Confusion Matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    # Classification Report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Compare K values
    print("\nAccuracy for Different K Values")
    for k in range(1, 11):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        pred = model.predict(x_test)
        print(f"K = {k} : {accuracy_score(y_test, pred):.2f}")

    # Predict New Sample
    sample = [[5.1, 3.5, 1.4, 0.2]]
    prediction = model.predict(sample)
    print("\nNew Sample Prediction:", iris.target_names[prediction][0])

knn()