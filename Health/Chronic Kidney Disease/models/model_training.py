import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(data, target_column):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    
    X = X.select_dtypes(include=['number'])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    print(f'Accuracy: {accuracy_score(y_test, predictions)}')
    print(classification_report(y_test, predictions))
    
    return model