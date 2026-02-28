# फाईलचे नाव: english_tutor.py
import os
from dotenv import load_dotenv

# 🌟 नवीन लायब्ररी इम्पोर्ट करण्याची पद्धत
from google import genai

# .env फाईलमधून सिक्रेट्स लोड करा
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# 🌟 नवीन पद्धतीने AI Client चालू करणे
client = genai.Client(api_key=API_KEY)


def check_full_sentence(user_input):
    try:
        # AI ला दिलेली कडक ऑर्डर (Prompt Engineering)
        prompt = f"""
        Act as an expert English grammar tutor for a Marathi speaker.
        Analyze this English sentence: "{user_input}"

        Respond EXACTLY in the following format:

        If the sentence is 100% grammatically correct:
        ✅ मुख्य व्याकरण बरोबर आहे!
        📚 शब्दांच्या जाती (Parts of Speech): [Identify POS for each word in English]

        If the sentence has grammar mistakes:
        ❌ वाक्यात काही चुका आहेत:
        ------------------------------
        🚩 [Explain the exact mistake in simple Marathi]
        📚 शब्दांच्या जाती (Parts of Speech): [Identify POS for each word]
        ------------------------------
        💡 असे असायला हवे होते: [Write the fully corrected English sentence]

        🎓 शिकण्यासाठी टिप्स:
        🔹 [Explain the grammar rule behind the mistake in simple Marathi]
        """

        # 🌟 नवीन पद्धतीने गुगलच्या सर्व्हरला रिक्वेस्ट पाठवणे
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )

        ai_text = response.text

        # वाक्य बरोबर आहे की नाही हे AI च्या उत्तरातून ओळखणे
        is_correct = "✅" in ai_text

        return is_correct, ai_text

    except Exception as e:
        return False, f"❌ AI शी कनेक्ट करताना एरर आला. इंटरनेट किंवा API Key तपासा.\nError: {e}"