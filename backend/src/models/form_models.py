from pydantic import BaseModel, ConfigDict
from typing import List, Optional

class FormSubmission(BaseModel):
    model_config = ConfigDict(strict=True)

    # Client info
    name: str
    date_of_birth: str
    email: str
    phone: str
    age: int
    weight: float
    height: float
    notes: Optional[str] = ''

    # Health status
    previous_injuries: Optional[str] = ''
    active_injuries: Optional[str] = ''
    medications: Optional[str] = ''
    pain_points: Optional[str] = ''

    # Training history
    prior_training_types: Optional[str] = ''
    motivation_text: Optional[str] = ''

    # Goals
    goals: Optional[List[str]] = []

    # VO2max
    test_type: Optional[str] = ''
    result: Optional[float] = 0.0
    vo2max_group: Optional[str] = ''

    # Reflection
    why_test: Optional[str] = ''
    result_reaction: Optional[str] = ''
    training_use_intent: Optional[str] = ''
    should_prioritize: Optional[str] = ''
