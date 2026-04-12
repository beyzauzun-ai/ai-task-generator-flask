import os
import sys
from dotenv import load_dotenv
from litellm import completion

def main():
    load_dotenv(override=True)

    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    print("Key son 6 karakter:", api_key[-6:] if api_key else "yok")
    if not api_key:
        print("GEMINI_API_KEY bulunamadı.")
        return

    topic = sys.argv[1].strip() if len(sys.argv) > 1 else "AI trends in 2026"

    prompt = f"""
Give a short summary about "{topic}" with 3 bullet points.
Keep it clear, simple, and readable.
"""

    try:
        response = completion(
            model="gemini/gemini-2.5-flash",
            api_key=api_key,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300,
        )

        content = response["choices"][0]["message"]["content"]
        print(content)

    except Exception as e:
        print(f"Agent hatası: {str(e)}")


if __name__ == "__main__":
    main()