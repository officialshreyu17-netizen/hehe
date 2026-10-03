import streamlit as st
import random
import time

# Page Config
st.set_page_config(page_title="Happy Boyfriend Day! ❤️", page_icon="💖", layout="centered")

# Secret Password Gateway
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 Top Secret Access")
    st.write("#### Enter the secret code to unlock your gift:")
    
    password = st.text_input("Hint: Our special date (DDMM)", type="password")
    
    if st.button("Unlock 🔑"):
        if password == "0612":  # Secret password
            st.session_state["authenticated"] = True
            st.balloons()
            st.rerun()
        else:
            st.error("Wrong password! Try again cutie 😄")
    st.stop()

# --- MAIN CONTENT AFTER UNLOCKING ---

st.title("❤️ Happy Boyfriend Day! ❤️")
st.write("A custom coded gift just for you 💻✨")

st.divider()

# Feature 1: "Jaan Ho Meri" Audio/Video Player
st.header("🎶 You are for me like this song: Jaan Ho Meri")
st.write("Press play before exploring the page! 👇")

# Direct YouTube Shorts Video Embed
st.video("https://www.youtube.com/watch?v=GWjKQsEt8QE")

st.divider()

# Feature 2: Interactive Love Meter
st.header("⚡ Relationship Compatibility Test")
name = st.text_input("Enter your name:", "Best Boyfriend Ever")

if st.button("Calculate Compatibility 💘"):
    with st.spinner("Analyzing love stars... ✨"):
        time.sleep(1)
        st.success(f"💖 Result: **10000000000% Match!** {name} is officially the best boyfriend in the world! 🥰")

st.divider()

# Feature 3: Our Special Memories
st.header("📸 Our Memories")

col1, col2 = st.columns(2)

with col1:
    st.subheader("First Meet at Kalka Ji 🛕")
    st.write("Jahan tumne mujhe pehli hi baar mein bina baat ke  daant lagayi thi! 😂 Par seriously, wo daant aur wo din hamesha special rahega. ❤️")

with col2:
    st.subheader("Favourite Thing happens 🌸")
    st.write("Hum Jab iskon gaaye the aur voh aapka earring lena aur pehnana then voh baat chit. 🙏✨")

st.divider()

# Feature 4: Interactive Reason Generator
st.header("🎲 Why You're The Best")

reasons = [
    "Aap meri har bakwas baat dhyan se sunte ho.",
    "Aapki smile dekhte hi mera sara stress gayab ho jata hai.",
    "Tumhare sath ghoomne jati hu toh voh care aur voh dhyan rakhna aaye haaye.",
    "Tumhari Bakwas merko bhut aachi lagti hai personally lekin ab shant kyu ho gaye ho please pahle jaise ho jao pls!",
    "Aap humesha mera sabse bada supporter  ho.",
    "Aapse din mei 5 min aaache se baat ho jaaye toh best din voh like jisme mein aapki baak baak sunti hu."
]

if st.button("Click for a Reason Why I Love You 💌"):
    with st.spinner("Finding a reason..."):
        time.sleep(0.4)
        selected_reason = random.choice(reasons)
        st.info(f"👉 {selected_reason}")

st.divider()

# Feature 5: Quick Quiz
st.header("🧩 How Well Do You Know Us?")
q1 = st.radio("Who is the dramatic one in this relationship?", ["You", "Me", "Both of us"])

if st.button("Submit Answer 🎯"):
    if q1 == "Me":
        st.write("Correct answer! 10/10 😂❤️")
    else:
        st.write("Hmm, debatable... but I still love you! 🤪")

st.divider()

# Final Note
st.subheader("💌 A Small Note For You")
st.write("""
Thank you for being you, for handling my mood swings, and for making everyday feel a bit brighter. 
Happy Boyfriend Day! Love you loads! 💖
""")
