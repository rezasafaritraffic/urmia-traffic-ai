
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='Urmia Traffic AI', layout='wide')
st.title('🚦 Urmia Traffic AI')

intersection = st.text_input("نام تقاطع:", "خیابان استاد برزگر و شهید باکری")
if st.button("شروع تحلیل و تنظیم چراغ‌ها"):
    st.success(f"تجزیه و تحلیل برای '{intersection}' انجام شد.")

    # Mock traffic data
    traffic_data = {
        "جهت": ["شمال", "جنوب", "شرق", "غرب"],
        "ترافیک": np.random.randint(50, 300, 4)
    }
    df = pd.DataFrame(traffic_data)

    # نمایش نمودار میله‌ای
    st.subheader("🔢 حجم ترافیک")
    st.bar_chart(df.set_index("جهت"))

    # زمان‌بندی فرضی چراغ‌ها
    green_times = np.round((df["ترافیک"] / df["ترافیک"].sum()) * 120, 1)  # مجموع ۲ دقیقه
    df["زمان چراغ سبز (ثانیه)"] = green_times

    # نمایش جدول
    st.subheader("⏱ زمان‌بندی پیشنهادی چراغ‌ها")
    st.table(df)

    # نمودار دایره‌ای
    st.subheader("🟢 سهم هر جهت از زمان سبز")
    fig, ax = plt.subplots()
    ax.pie(green_times, labels=df["جهت"], autopct="%1.1f%%", startangle=90)
    st.pyplot(fig)
