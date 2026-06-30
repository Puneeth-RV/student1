import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score, confusion_matrix

def decision_tree():

    # Play Tennis Dataset
    data = {
        "Outlook": ["Sunny","Sunny","Overcast","Rain","Rain","Rain","Overcast","Sunny","Sunny","Rain","Sunny","Overcast","Overcast","Rain"],
        "Temperature": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
        "Humidity": ["High","High","High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
        "Windy": ["False","True","False","False","False","True","True","False","False","False","True","True","False","True"],
        "Play": ["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Encode categorical values
    le = LabelEncoder()
    for col in df.columns:
        df[col] = le.fit_transform(df[col])

    # Split features and target
    X = df.drop("Play", axis=1)
    y = df["Play"]

    # Train model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    # Predict
    y_pred = model.predict(X)

    # Accuracy
    print("Accuracy:")
    print(accuracy_score(y, y_pred))

    # Confusion Matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y, y_pred))

    # Predict new sample
    sample = [[2, 2, 1, 0]]
    prediction = model.predict(sample)

    if prediction[0] == 1:
        print("\nPrediction: Yes")
    else:
        print("\nPrediction: No")

    # Decision Tree
    print("\nDecision Tree:")
    print(export_text(model, feature_names=list(X.columns)))

    # Gini Index
    print("\nRoot Gini Index:", model.tree_.impurity[0])

decision_tree()