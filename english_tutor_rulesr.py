# फाईलचे नाव: english_tutor_rulesr.py
# काम: संपूर्ण वाक्याचे स्कॅनिंग करणे (Articles, Modals, Questions, Tenses, Tips & Suggestions)

import grammar_brain


def check_full_sentence(user_input):
    is_correct = True
    feedback_list = []  # सर्व चुका आणि बरोबर गोष्टींची यादी
    learning_tips = []  # शिकण्यासाठी नवीन टिप्सचा बॉक्स
    suggestion = user_input
    words = user_input.lower().split()

    if len(words) == 0:
        return False, "❌ कृपया एखादे वाक्य टाका."

    # ==========================================
    # 🌟 नवीन: वाक्य सुधारणे आणि टिप्स (Suggestions)
    # ==========================================
    if "completed task" in user_input.lower():
        is_correct = False
        feedback_list.append("🚩 Articles चा अभाव: 'Task' हे मोजता येणारे नाम आहे, त्याआधी 'the' किंवा 'a' लावा.")
        suggestion = suggestion.replace("completed task", "completed the task")
        learning_tips.append("🔹 नियम: जेव्हा आपण एखाद्या ठराविक कामाबद्दल बोलतो, तेव्हा 'The' वापरतात.")

        # ==========================================
        # 🌟 नवीन: Possessive Pronoun आणि Singular/Plural च्या चुका
        # ==========================================
    if "are you name" in user_input.lower() or "is you name" in user_input.lower() or "are your name" in user_input.lower():
            is_correct = False
            feedback_list.append(
                "🚩 'Name' हे एकवचनी (Singular) आहे, त्यामुळे 'are' नाही तर 'is' वापरावे. तसेच 'तुझे' सांगण्यासाठी 'you' नाही तर 'your' वापरावे.")

            # वाक्य दुरुस्त करणे
            suggestion = "What is your name?"

            learning_tips.append(
                "🔹 नियम: 'You' म्हणजे 'तू', आणि 'Your' म्हणजे 'तुझे' (Possessive Pronoun). नावाबाबत विचारताना नेहमी 'What is your name?' असे विचारतात.")

    if "that time" in user_input.lower() and "at that time" not in user_input.lower():
        learning_tips.append(
            "🔹 टीप: वेळेचा उल्लेख करताना 'At that time' किंवा 'By that time' वापरणे अधिक नैसर्गिक वाटते.")
        suggestion = suggestion.replace("that time", "at that time")

    if "had already completed" in user_input.lower():
        learning_tips.append(
            "🔹 काळ: हे वाक्य 'Past Perfect Tense' मध्ये आहे. भूतकाळातील दोन घटनांपैकी पहिली पूर्ण झालेली घटना सांगण्यासाठी 'Had + V3' वापरतात.")

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
    if len(words) >= 2:
        first_word = words[0]
        second_word = words[1]

        # प्रकार A: Wh- Question
        if first_word in grammar_brain.parts_of_speech.get("wh_words", []):
            if second_word in grammar_brain.auxiliary_rules:
                feedback_list.append(
                    f"✅ प्रश्नाची रचना बरोबर: '{first_word.capitalize()}' (Wh-word) + '{second_word}' (Auxiliary verb).")
            else:
                feedback_list.append(
                    f"🚩 प्रश्नाची रचना चूक: '{first_word}' नंतर साह्यकारी क्रियापद (am/is/are/do/did) यायला हवे.")
                is_correct = False

        # प्रकार B: Yes/No Question
        elif first_word in grammar_brain.auxiliary_rules:
            if second_word in grammar_brain.all_subjects or second_word in grammar_brain.parts_of_speech.get("Noun",
                                                                                                             {}).get(
                    "उदाहरणे", []):
                if second_word in grammar_brain.auxiliary_rules[first_word] or first_word in ["did", "had", "can",
                                                                                              "will", "could", "should",
                                                                                              "must"]:
                    feedback_list.append(
                        f"✅ Yes/No प्रश्न बरोबर: '{first_word.capitalize()}' सोबत '{second_word}' योग्य आहे.")
                else:
                    feedback_list.append(
                        f"🚩 Subject-Verb चूक: '{first_word.capitalize()}' सोबत '{second_word}' चालत नाही.")
                    is_correct = False
            else:
                feedback_list.append(f"✅ वाक्य साह्यकारी क्रियापदाने सुरू झाले आहे: '{first_word.capitalize()}'.")

        # प्रकार C: साधे वाक्य
        else:
            if second_word in grammar_brain.auxiliary_rules:
                if first_word in grammar_brain.auxiliary_rules[second_word] or second_word in ["did", "had", "can",
                                                                                               "will", "could", "would",
                                                                                               "should", "must"]:
                    feedback_list.append(
                        f"✅ Subject-Verb Agreement: '{first_word.capitalize()}' सोबत '{second_word}' अगदी बरोबर आहे.")
                else:
                    feedback_list.append(
                        f"🚩 Subject-Verb चूक: '{first_word.capitalize()}' सोबत '{second_word}' येत नाही.")
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
        unique_pos = ", ".join(list(set(pos_found)))
        feedback_list.append(f"📚 शब्दांच्या जाती (Parts of Speech): {unique_pos}")

    # ==========================================
    # फायनल रिपोर्ट तयार करणे (Merging Everything)
    # ==========================================
    final_feedback = ""

    if is_correct and len(feedback_list) == 0:
        final_feedback += "✅ वाक्य व्याकरणदृष्ट्या योग्य वाटत आहे!\n"
    elif is_correct:
        final_feedback += "✅ मुख्य व्याकरण बरोबर आहे!\n" + "-" * 30 + "\n" + "\n".join(feedback_list) + "\n"
    else:
        final_feedback += "❌ वाक्यात काही चुका आहेत:\n" + "-" * 30 + "\n" + "\n".join(feedback_list) + "\n"

    # जर काही 'Suggestion' असेल (वाक्य बदलले असेल)
    if suggestion.lower() != user_input.lower():
        final_feedback += f"------------------------------\n💡 असे असायला हवे होते: {suggestion.capitalize()}\n"

    # जर काही 'Tips' असतील
    if learning_tips:
        final_feedback += f"\n🎓 शिकण्यासाठी टिप्स:\n" + "\n".join(learning_tips)

    return is_correct, final_feedback