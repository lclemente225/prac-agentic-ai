import os
from dotenv import load_dotenv
from google import genai
def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    print("checkpoint 1")
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="""Why is the sky blue?"""
    )
    print("checkpoint 2")
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("response is malformed")
        return

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    return

main()