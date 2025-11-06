import joblib
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math


def main():
    # Load dataset
    data = fetch_california_housing(as_frame=True)
    X = data.frame[data.feature_names]
    y = data.frame['MedHouseVal']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Simple pipeline: scaler + RF
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    print("Training model...")
    pipeline.fit(X_train, y_train)

    # Evaluate
    preds = pipeline.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    rmse = math.sqrt(mse)
    print(f"✅ Test RMSE: {rmse:.4f}")

    # Save pipeline (scaler + model)
    joblib.dump({
        "pipeline": pipeline,
        "feature_names": data.feature_names
    }, "pipeline.pkl")

    print("🎉 Model trained and saved successfully as pipeline.pkl")


if __name__ == "__main__":
    main()
