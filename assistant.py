import webbrowser
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def execute(command):

    command = command.lower()

    if "youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "chatgpt" in command:
        webbrowser.open("https://chatgpt.com")
        return "Opening ChatGPT"

    elif "google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    response = model.generate_content(command)

    return response.text