# फाईलचे नाव: progress_tracker.py
# काम: प्रगती TXT, CSV आणि आता SQL Database मध्ये सेव्ह करणे आणि स्क्रीनवर दाखवणे (Show)

import datetime
import csv  # CSV फाईल बनवण्यासाठी पायथनची सिस्टीम
import os  # फाईल आधीपासून आहे की नाही हे तपासण्यासाठी
import sqlite3  # 🌟 नवीन: SQL डेटाबेससाठी पायथनची इनबिल्ट सिस्टीम


# ==========================================
# 🌟 नवीन: डेटाबेस आणि टेबल तयार करणे (Setup)
# ==========================================
def setup_database():
    # डेटाबेस फाईलला कनेक्ट करणे
    conn = sqlite3.connect("english_database.db")
    cursor = conn.cursor()

    # जर 'study_records' नावाचे टेबल नसेल, तर ते बनवणे
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS study_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time TEXT,
            sentence TEXT,
            result TEXT,
            feedback TEXT
        )
    ''')
    conn.commit()
    conn.close()


# फाईल लोड होताच सर्वात आधी डेटाबेस तयार होईल
setup_database()


def save_my_progress(sentence, is_correct, feedback):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    if is_correct:
        status = "✅ right"
    else:
        status = "❌ CHUKLA"

    # ==========================================
    # १. TXT फाईलमध्ये सेव्ह करणे (वाचण्यासाठी)
    # ==========================================
    with open("my_study_record.txt", "a", encoding="utf-8") as txt_file:
        record_line = f"[{current_time}] वाक्य: '{sentence}' | निकाल: {status} | नियम: {feedback}\n"
        txt_file.write(record_line)

    # ==========================================
    # २. CSV फाईलमध्ये सेव्ह करणे (Excel साठी)
    # ==========================================
    csv_filename = "my_study_record.csv"
    file_exists = os.path.isfile(csv_filename)

    with open(csv_filename, "a", newline='', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # जर फाईल नवीन असेल, तर सर्वात वरती कॉलम्सची नावे (Headers) टाकणे
        if not file_exists:
            writer.writerow(["Date_Time", "Sentence", "Result", "Feedback"])

        # डेटा रोज (Rows) मध्ये टाकणे
        writer.writerow([current_time, sentence, status, feedback])

    # ==========================================
    # 🌟 ३. नवीन: SQL Database मध्ये सेव्ह करणे
    # ==========================================
    conn = sqlite3.connect("english_database.db")
    cursor = conn.cursor()

    # SQL ची 'INSERT' कमांड चालवणे
    cursor.execute('''
        INSERT INTO study_records (date_time, sentence, result, feedback) 
        VALUES (?, ?, ?, ?)
    ''', (current_time, sentence, status, feedback))

    conn.commit()
    conn.close()

    # print("💾 (प्रगती TXT, CSV आणि SQL Database मध्ये सेव्ह झाली आहे.)")  # हा मेसेज लपवला आहे जेणेकरून खिडकीत अडचण येऊ नये


# ==========================================
# ३. डेटा वाचून स्क्रीनवर दाखवणे (Show Function - Terminal साठी)
# ==========================================
def show_my_progress():
    print("\n" + "=" * 50)
    print("📊 तुझा आतापर्यंतचा अभ्यास (Study Report)")
    print("=" * 50)

    try:
        # आपण TXT फाईल वाचून ती स्क्रीनवर दाखवत आहोत
        with open("my_study_record.txt", "r", encoding="utf-8") as txt_file:
            content = txt_file.read()
            if content:
                print(content)
            else:
                print("अजून कोणताही अभ्यास सेव्ह केलेला नाही. प्रॅक्टिस सुरू कर!")
    except FileNotFoundError:
        print("मला कोणतीही जुनी फाईल सापडली नाही. तू अजून प्रॅक्टिस सुरू केलेली नाहीस.")

    print("=" * 50 + "\n")


print("📊 Advanced Progress Tracker लोड झाला आहे! (TXT + CSV + SQL)")


# progress_tracker.py च्या सर्वात खाली हे जोडा:

def get_stats():
    """डेटाबेसमधून बरोबर आणि चुकीच्या उत्तरांची संख्या मोजणे"""
    conn = sqlite3.connect("english_database.db")
    cursor = conn.cursor()

    # SQL मधील 'COUNT' वापरून मोजणी करणे
    cursor.execute("SELECT COUNT(*) FROM study_records WHERE result LIKE '%right%'")
    correct = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM study_records WHERE result LIKE '%CHUKLA%'")
    incorrect = cursor.fetchone()[0]

    conn.close()
    return correct, incorrect