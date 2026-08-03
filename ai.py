import time
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_response(prompt): 
    prompt = prompt

    interaction = client.interactions.create(
            model=os.getenv("GOOGLE_MODEL"),
            input=prompt
        )
    print("\n" + interaction.output_text)

def main() :
    print("Welcome to the AI prompt interface. Press Ctrl+C to exit.")

    while True:
        try :
            get_response(input("\nEnter your prompt: "))
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
