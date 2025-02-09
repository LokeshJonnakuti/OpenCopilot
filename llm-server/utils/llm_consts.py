import os
from typing import TypedDict

EXPERIMENTAL_FEATURES_ENABLED = os.getenv("EXPERIMENTAL_FEATURES_ENABLED", "NO")
SYSTEM_MESSAGE_PROMPT = "system_message_prompt"
SUMMARIZATION_PROMPT = "summarization_prompt"
X_App_Name = "X-App-Name"

class VsThresholds(TypedDict):
    api_score_threshold: float
    flows_score_threshold: float
    kb_score_threshold: float

vs_thresholds: VsThresholds = {
    "api_score_threshold": float(os.getenv("API_SCORE_THRESHOLD", "0.25")),
    "flows_score_threshold": float(os.getenv("FLOWS_SCORE_THRESHOLD", "0.75")),
    "kb_score_threshold": float(os.getenv("KB_SCORE_THRESHOLD", "0.75"))    
}


model_env_var = "CHAT_MODEL"