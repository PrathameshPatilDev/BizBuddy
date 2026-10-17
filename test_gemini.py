
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY was not found in your .env file.")
else:
    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents="Reply with exactly: BizBuddy Gemini connection successful."
        )

        print("Gemini response:")
        print(response.text)

    except Exception as error:
        print("Gemini connection failed.")
        print("Error type:", type(error).__name__)
        print("Check your API key, model availability, and API access.")
