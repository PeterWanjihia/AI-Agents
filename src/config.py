import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass(frozen=True)
class Settings:
    provider: str
    api_key: str
    model_fast: str
    model_smart: str
    temperature: float
    max_steps: int

def load_settings(env_file: str = ".env") -> Settings:
    load_dotenv(env_file)

    provider = os.getenv("PROVIDER", "gemini").strip().lower()
    temperature = float(os.getenv("TEMPERATURE", "0"))
    max_steps = int(os.getenv("MAX_STEPS", "12"))

    if provider == "gemini":
        api_key = os.getenv("GEMINI_API_KEY", "").strip()
        model_fast = os.getenv("GEMINI_MODEL_FAST", "gemini/gemini-2.5-flash").strip()
        model_smart = os.getenv("GEMINI_MODEL_SMART", "gemini/gemini-3-pro").strip()
        if not api_key:
            raise RuntimeError("Missing GEMINI_API_KEY in .env")
        return Settings(provider, api_key, model_fast, model_smart, temperature, max_steps)

    raise RuntimeError(f"Unsupported provider: {provider}")
