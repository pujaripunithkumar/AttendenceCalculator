import streamlit as st

# 🎓 Main Titles
st.title("Attendance Calculator")
st.subheader("Don't give up - Your life doesn't end here")
st.markdown("### Hi, Students 👋")

# 🎓 Branches and Subjects
branches = {
    "CSE (AI-ML)": ["DPSD", "Data Structures", "AI-ML", "Java", "Maths","IOT"],
    "CSE (AIDS)": ["DPSD", "Data Structures", "AIDS", "Java", "Maths","IOT"],
    "CSE (Core)": ["DPSD", "Data Structures", "OS", "Java", "Maths","IOT"],
    "CSE (Cyber Security)": ["DPSD", "Data Structures", "Cyber Security", "Java", "Maths","IOT"],
    "ECE": ["Signals & Systems", "Analog Electronics", "Digital Logic", "Maths", "Network Theory","IOT"],
    "EEE": ["Electrical Machines", "Power Systems", "Digital Logic", "Maths", "Control Systems","IOT"]
}

# Select branch and subject
branch = st.selectbox("Select your Branch", list(branches.keys()))
subject = st.selectbox("Select Subject", branches[branch])

# Input attendance details
total_classes = st.number_input("Enter Total Classes", min_value=1, step=1)
attended_classes = st.number_input("Enter Attended Classes", min_value=0, step=1)

if st.button("Calculate Attendance"):
    percentage = (attended_classes / total_classes) * 100
    st.markdown(f"## 📊 Your Attendance for {subject} in {branch} is: *{percentage:.2f}%*")

    if percentage >= 75:
        st.success("🎉 Congratulations! You are safe ✅")
    else:
        shortage = (0.75 * total_classes) - attended_classes
        st.error(f"⚠ You need to attend at least {int(shortage)} more classes!")
        st.info("💡 Proverb: 'The expert in anything was once a beginner.'")

st.markdown("---")
st.markdown("💖 Made with love (Punith)", unsafe_allow_html=True)