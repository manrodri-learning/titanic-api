import numpy as np
import pandas as pd
from fastapi.testclient import TestClient
from sklearn.metrics import accuracy_score


def test_always_pass() -> None:
    assert True


# skip this test
# @pytest.mark.skip(reason="this test is not ready yet")
def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    expected_no_predictions = len(payload["inputs"])

    # When
    response = client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200

    prediction_data = response.json()
    assert prediction_data["predictions"]

    assert prediction_data["errors"] is None
    predictions = prediction_data.get("predictions")
    assert isinstance(predictions, np.ndarray)
    assert isinstance(predictions[0], np.int64)
    assert prediction_data.get("errors") is None
    assert len(predictions) == expected_no_predictions

    _predictions = list(predictions)
    y_true = test_data["survived"]
    accuracy = accuracy_score(_predictions, y_true)
    assert accuracy > 0.7
