# फाईलचे नाव: english_tutor.py
# काम: संपूर्ण वाक्याचे स्कॅनिंग करणे (Articles, Modals, Questions, Tenses)

import grammar_brain


def check_full_sentence(sentence):
    # वाक्यातील जास्तीची जागा काढणे आणि सर्व शब्द छोट्या लिपीत (lowercase) करणे
    words = sentence.strip().lower().split()

    if len(words) < 2:
        return False, "❌ कृपया किमान दोन शब्द टाका. (उदा. I am, What is)"

    feedback_list = []
    is_correct = True

    # ==========================================
    # टेस्ट १: Articles (a/an) चे नियम तपासणे
    # ==========================================
    for i in range(len(words) - 1):
        vowels = ["a", "e", "i", "o", "u"]
        if words[i] == "a" and words[i + 1][0] in vowels:
            feedback_list.append(
                f"🚩 Article चूक: '{words[i + 1]}' स्वराने (Vowel) सुरू होतो, त्यामुळे 'a' ऐवजी 'an' वापरा.")
            is_correct = False
        elif words[i] == "an" and words[i + 1][0] not in vowels:
            feedback_list.append(
                f"🚩 Article चूक: '{words[i + 1]}' व्यंजनाने (Consonant) सुरू होतो, त्यामुळे 'an' ऐवजी 'a' वापरा.")
            is_correct = False

    # ==========================================
    # टेस्ट २: Modal Verbs (can, will, should) तपासणे
    # ==========================================
    for i in range(len(words) - 1):
        if words[i] in ["can", "will", "should", "must", "could", "would", "may", "might"]:
            if words[i + 1] == "to":
                feedback_list.append(f"🚩 Modal चूक: '{words[i]}' नंतर 'to' लावत नाहीत.")
                is_correct = False

    # ==========================================
    # टेस्ट ३: वाक्याची रचना आणि Subject-Verb Agreement
    # ==========================================
    first_word = words[0]
    second_word = words[1]

    # प्रकार A: Wh- Question (उदा. What is...)
    if first_word in grammar_brain.parts_of_speech.get("wh_words", []):
        if second_word in grammar_brain.auxiliary_rules:
            feedback_list.append(
                f"✅ प्रश्नाची रचना बरोबर: '{first_word.capitalize()}' (Wh-word) + '{second_word}' (Auxiliary verb).")
        else:
            feedback_list.append(
                f"🚩 प्रश्नाची रचना चूक: '{first_word}' नंतर साह्यकारी क्रियापद (am/is/are/do/did) यायला हवे.")
            is_correct = False

    # प्रकार B: Yes/No Question (उदा. Is he...)
    elif first_word in grammar_brain.auxiliary_rules:
        if second_word in grammar_brain.all_subjects or second_word in grammar_brain.parts_of_speech.get("Noun",
                                                                                                         {}).get(
                "उदाहरणे", []):
            if second_word in grammar_brain.auxiliary_rules[first_word] or first_word in ["did", "had", "can", "will",
                                                                                          "could", "should", "must"]:
                feedback_list.append(
                    f"✅ Yes/No प्रश्न बरोबर: '{first_word.capitalize()}' सोबत '{second_word}' योग्य आहे.")
            else:
                feedback_list.append(f"🚩 Subject-Verb चूक: '{first_word.capitalize()}' सोबत '{second_word}' चालत नाही.")
                is_correct = False
        else:
            feedback_list.append(f"✅ वाक्य साह्यकारी क्रियापदाने सुरू झाले आहे: '{first_word.capitalize()}'.")

    # प्रकार C: साधे वाक्य (Normal Statement - उदा. He is...)
    else:
        if second_word in grammar_brain.auxiliary_rules:
            if first_word in grammar_brain.auxiliary_rules[second_word] or second_word in ["did", "had", "can", "will",
                                                                                           "could", "would", "should",
                                                                                           "must"]:
                feedback_list.append(
                    f"✅ Subject-Verb Agreement: '{first_word.capitalize()}' सोबत '{second_word}' अगदी बरोबर आहे.")
            else:
                feedback_list.append(f"🚩 Subject-Verb चूक: '{first_word.capitalize()}' सोबत '{second_word}' येत नाही.")
                is_correct = False

    # ==========================================
    # टेस्ट ४: Vocabulary (शब्दांच्या जाती ओळखणे)
    # ==========================================
    pos_found = []
    for w in words:
        for pos, details in grammar_brain.parts_of_speech.items():
            if type(details) == dict and "उदाहरणे" in details:
                if w in details["उदाहरणे"]:
                    pos_found.append(f"{w} ({pos})")
            elif type(details) == list:
                if w in details:
                    pos_found.append(f"{w} ({pos})")

    if pos_found:
        # डुप्लिकेट शब्द काढण्यासाठी set वापरला आहे
        unique_pos = ", ".join(list(set(pos_found)))
        feedback_list.append(f"📚 शब्दांच्या जाती (Parts of Speech): {unique_pos}")

    # ==========================================
    # फायनल रिपोर्ट तयार करणे
    # ==========================================
    if is_correct and len(feedback_list) == 0:
        final_feedback = "✅ वाक्य व्याकरणदृष्ट्या योग्य वाटत आहे!"
    elif is_correct:
        final_feedback = "✅ मुख्य व्याकरण बरोबर आहे!\n" + "-" * 30 + "\n" + "\n".join(feedback_list)
    else:
        final_feedback = "❌ वाक्यात काही चुका आहेत:\n" + "-" * 30 + "\n" + "\n".join(feedback_list)

    return is_correct, final_feedback