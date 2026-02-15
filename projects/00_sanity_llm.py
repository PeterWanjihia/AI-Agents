from litellm import completion
from src.config import load_settings

def extract_text(resp_dict: dict) -> str | None:
    choices = resp_dict.get("choices") or []
    if not choices:
        return None
    msg = (choices[0] or {}).get("message") or {}
    return msg.get("content")

def main():
    s = load_settings(".env")

    resp_obj = completion(
        model=s.model_fast,
        messages=[
            {"role": "system", "content": "Output exactly ONE short sentence of visible text. Never return empty output."},
            {"role": "user", "content": "Say hello and confirm you can respond."},
        ],
        temperature=s.temperature,
        max_tokens=80,
    )

    resp = resp_obj.model_dump()
    text = extract_text(resp)

    # If content is still None, print a useful hint (not a huge trace)
    if text is None:
        usage = resp.get("usage")
        print("No visible text returned. Usage:", usage)
    else:
        print(text)

if __name__ == "__main__":
    main()
