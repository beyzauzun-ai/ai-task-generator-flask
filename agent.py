import os
import sys
import time
from dotenv import load_dotenv
from litellm import completion

def main() -> None:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("GEMINI_API_KEY bulunamadı.")
        return

    if len(sys.argv) > 1:
        topic = sys.argv[1]
    else:
        topic = "AI trends in 2026"

    prompt = f"Give a short summary about {topic} with 3 bullet points."

    print(f"Konu: {topic}")
    print("API isteği gönderiliyor...")

    response = None

    for i in range(3):
        try:
            response = completion(
                model="gemini/gemini-2.5-flash-lite",
                api_key=api_key,
                timeout=60,
                max_tokens=250,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            break
        except Exception:
            print("Tekrar deneniyor...", i + 1)
            time.sleep(5)

    if response is None:
        print("API şu anda cevap vermiyor. Lütfen biraz sonra tekrar deneyin.")
        return

    result = response["choices"][0]["message"]["content"]
    print(result)

    with open("AI_Trends_2026.md", "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    main()