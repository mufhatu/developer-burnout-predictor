from pydantic import BaseModel

class DeveloperMetrics(BaseModel):
    age: float
    experience_years: float
    daily_work_hours: float
    sleep_hours: float
    caffeine_intake: float
    bugs_per_day: float
    commits_per_day: float
    meetings_per_day: float
    screen_time: float
    exercise_hours: float
    stress_level: float

class PredictionResult(BaseModel):
    burnout_level : str
    confidence: float