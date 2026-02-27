# फाईलचे नाव: gui_main.py
# काम: Dark Mode UI, भाषांतर, आणि आता थेट SQL डेटाबेसमधून रिपोर्ट दाखवणे!

import tkinter as tk
from tkinter import messagebox
import english_tutor
import progress_tracker
from deep_translator import GoogleTranslator
import sqlite3  # 🌟 नवीन: डेटाबेस वाचण्यासाठी आपण हे टूल खिडकीतही बोलावले


def check_grammar(event=None):
    user_input = entry_sentence.get().strip().lower()

    if user_input == "" or user_input == "":
        messagebox.showwarning("Warning", "❌ कृपया एखादे वाक्य टाका.")
        return

    try:
        marathi_meaning = GoogleTranslator(source='en', target='mr').translate(user_input)
        translation_text = f"📝 तुमचे वाक्य: {user_input.capitalize()}\n🌐 मराठी अर्थ: {marathi_meaning}\n" + "-" * 55 + "\n"
    except Exception as e:
        translation_text = f"📝 तुमचे वाक्य: {user_input.capitalize()}\n🌐 (मराठी अर्थ बघण्यासाठी इंटरनेट चालू असणे आवश्यक आहे)\n" + "-" * 55 + "\n"

    is_correct, feedback = english_tutor.check_full_sentence(user_input)
    progress_tracker.save_my_progress(user_input, is_correct, feedback)

    final_output = translation_text + feedback

    text_result.delete(1.0, tk.END)

    lines = final_output.split('\n')
    for line in lines:
        if "📝" in line:
            text_result.insert(tk.END, line + "\n", "cyan_text")
        elif "🌐" in line:
            text_result.insert(tk.END, line + "\n", "yellow_text")
        elif "✅" in line:
            text_result.insert(tk.END, line + "\n", "green_text")
        elif "🚩" in line or "❌" in line:
            text_result.insert(tk.END, line + "\n", "red_text")
        elif "📚" in line:
            text_result.insert(tk.END, line + "\n", "blue_text")
        elif "-" in line:
            text_result.insert(tk.END, line + "\n", "gray_text")
        else:
            text_result.insert(tk.END, line + "\n", "white_text")

    entry_sentence.delete(0, tk.END)
    on_focusout(None)


# ==========================================
# 🌟 नवीन 'Show Report' लॉजिक (SQL SELECT)
# ==========================================
def show_progress():
    try:
        # १. रस्ता जोडणे (Connection)
        conn = sqlite3.connect("english_database.db")
        cursor = conn.cursor()

        # २. SQL कमांड चालवणे: 'study_records' टेबलमधून सगळा डेटा (SELECT) घेऊन ये
        cursor.execute("SELECT date_time, sentence, result FROM study_records")

        # ३. fetchall(): गाडीतून सगळा डेटा काढून 'records' नावाच्या बॉक्समध्ये (List) टाकणे
        records = cursor.fetchall()

        conn.close()  # काम झाल्यावर रस्ता बंद करणे

        text_result.delete(1.0, tk.END)

        # जर बॉक्स रिकामा असेल (डेटा नसेल)
        if len(records) == 0:
            text_result.insert(tk.END, "🗄️ डेटाबेसमध्ये अजून कोणताही अभ्यास सेव्ह केलेला नाही.", "yellow_text")
        else:
            text_result.insert(tk.END, "🗄️ तुझा SQL डेटाबेस रिपोर्ट (Live):\n", "cyan_text")
            text_result.insert(tk.END, "-" * 55 + "\n", "gray_text")

            # ४. लूप फिरवून एक-एक रेकॉर्ड खिडकीत दाखवणे
            for row in records:
                date_time = row[0]
                sentence = row[1]
                result = row[2]

                # रिपोर्टचे डिझाईन
                record_line = f"🕒 {date_time} | 📝 {sentence} | {result}\n"

                # बरोबर असेल तर हिरवा रंग, चूक असेल तर लाल रंग
                if "✅" in result:
                    text_result.insert(tk.END, record_line, "green_text")
                else:
                    text_result.insert(tk.END, record_line, "red_text")

            text_result.insert(tk.END, "-" * 55 + "\n", "gray_text")

    except Exception as e:
        text_result.delete(1.0, tk.END)
        text_result.insert(tk.END, f"❌ डेटाबेस एरर: {e}\n(कदाचित तू अजून एकही वाक्य टाकलेले नाही)", "red_text")


# वॉटरमार्कचे लॉजिक
def on_entry_click(event):
    if entry_sentence.get() == '':
        entry_sentence.delete(0, "end")
        entry_sentence.config(fg='#FFFFFF')


def on_focusout(event):
    if entry_sentence.get() == '':
        entry_sentence.insert(0, '')
        entry_sentence.config(fg='#888888')


# डार्क डिझाईन
root = tk.Tk()
root.title("🌌 Advanced English Mastery (SQL Database Connected)")
root.geometry("750x850")
root.config(bg="#121212")

lbl_title = tk.Label(root, text="🎓 English Mastery AI", font=("Segoe UI", 24, "bold"), bg="#121212", fg="#00E676")
lbl_title.pack(pady=20)

frame_hints = tk.LabelFrame(root, text=" 💡 इंग्रजी व्याकरणाचे महत्त्वाचे नियम (Rules) ", font=("Segoe UI", 12, "bold"),
                            bg="#1E1E1E", fg="#FFD700", padx=20, pady=15, bd=2)
frame_hints.pack(pady=10, fill="x", padx=40)

hints_text = (
    "🔹 To Be (अस्तित्व): I am, He/She/It is, We/They are | भूतकाळ: was, were\n"
    "🔹 To Have (मालकी): He/She/It has, I/We/They have | भूतकाळ: had (सर्वांसोबत)\n"
    "🔹 To Do (कृती): He/She/It does, I/We/They do | भूतकाळ: did (सर्वांसोबत)\n"
    "🔹 Collective Nouns (समूह): Group, Team, Family हे एकवचनी असतात. (उदा. Team is playing)\n"
    "🔹 Articles: a, e, i, o, u (स्वरांच्या) आधी 'an' लावा. बाकी ठिकाणी 'a' लावा.\n"
    "🔹 Modals: can, will, should नंतर कधीही 'to' लावू नका. (उदा. I can go)"
)
lbl_hints = tk.Label(frame_hints, text=hints_text, font=("Segoe UI", 12), bg="#1E1E1E", fg="#E0E0E0", justify="left")
lbl_hints.pack(anchor="w")

entry_sentence = tk.Entry(root, font=("Segoe UI", 16), width=45, bg="#2D2D2D", fg="#888888", insertbackground="white",
                          relief="flat")
entry_sentence.insert(0, '')
entry_sentence.bind('<FocusIn>', on_entry_click)
entry_sentence.bind('<FocusOut>', on_focusout)
entry_sentence.pack(pady=25, ipady=8)

root.bind('<Return>', check_grammar)

frame_buttons = tk.Frame(root, bg="#121212")
frame_buttons.pack(pady=10)

btn_check = tk.Button(frame_buttons, text="Check Grammar ✅", font=("Segoe UI", 13, "bold"), bg="#00C853", fg="white",
                      activebackground="#00E676", padx=25, pady=10, borderwidth=0, cursor="hand2",
                      command=check_grammar)
btn_check.grid(row=0, column=0, padx=20)

# 🌟 बटनाचे नाव बदलले आहे!
btn_show = tk.Button(frame_buttons, text="Show Report (SQL) 🗄️", font=("Segoe UI", 13, "bold"), bg="#2962FF",
                     fg="white", activebackground="#448AFF", padx=25, pady=10, borderwidth=0, cursor="hand2",
                     command=show_progress)
btn_show.grid(row=0, column=1, padx=20)

text_result = tk.Text(root, font=("Consolas", 14), height=14, width=65, bg="#1E1E1E", fg="#FFFFFF", relief="flat",
                      padx=20, pady=20)
text_result.pack(pady=25)

# रंगांचे टॅग्स
text_result.tag_config("cyan_text", foreground="#00E5FF", font=("Consolas", 15, "bold"))
text_result.tag_config("yellow_text", foreground="#FFD700", font=("Consolas", 14, "bold"))
text_result.tag_config("green_text", foreground="#00E676")
text_result.tag_config("red_text", foreground="#FF5252")
text_result.tag_config("blue_text", foreground="#40C4FF")
text_result.tag_config("white_text", foreground="#FFFFFF")
text_result.tag_config("gray_text", foreground="#555555")

root.mainloop()