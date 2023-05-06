from typing import Any, List, Optional

from classification_model.processing.validation import TitanicDataInputSchema
from pydantic import BaseModel


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str
    predictions: List[float]


class MultipleTitanicDataInputs(BaseModel):
    inputs: List[TitanicDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "pclass": 1,
                        "name": "Allen, Miss. Elisabeth Walton",
                        "sex": "female",
                        "age": 29,
                        "sibsp": 0,
                        "parch": 0,
                        "ticket": 24160,
                        "fare": 211.3375,
                        "cabin": "B5",
                        "embarked": "S",
                        "boat": 2,
                        "body": 1,
                        "home.dest": "Cherbourg",
                    }
                ]
            }
        }
