# फाईलचे नाव: analytics_engine.py
import matplotlib.pyplot as plt
import progress_tracker


def show_analytics():
    # १. डेटाबेसमधून आकडेवारी मागवणे
    correct, incorrect = progress_tracker.get_stats()

    if correct == 0 and incorrect == 0:
        print("📊 आलेख काढण्यासाठी पुरेसा डेटा उपलब्ध नाही.")
        return

    # २. आलेखाची माहिती (Data Labels and Sizes)
    labels = [f'Correct ({correct})', f'Incorrect ({incorrect})']
    sizes = [correct, incorrect]
    colors = ['#00E676', '#FF5252']  # हिरवा आणि लाल रंग
    explode = (0.1, 0)  # बरोबर उत्तराचा भाग थोडा बाहेर काढणे

    # ३. आलेख तयार करणे (Plotting)
    plt.style.use('dark_background')  # डार्क थीमसाठी
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
           shadow=True, startangle=140, textprops={'fontsize': 12, 'color': 'white'})

    plt.title("🎓 My English Progress Report", fontsize=15, color='#FFD700')

    # ४. आलेख दाखवणे
    plt.show()


if __name__ == "__main__":
    show_analytics()