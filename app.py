import streamlit as st
import sqlite3

def create_db():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, grade TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY, name TEXT, subject TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS marks (id INTEGER PRIMARY KEY, student_id INTEGER, subject TEXT, marks INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY, student_id INTEGER, date TEXT, status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, sender TEXT, receiver TEXT, message TEXT)''')
    conn.commit()
    conn.close()

def add_student(name, age, grade):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    conn.close()

def add_teacher(name, subject):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO teachers (name, subject) VALUES (?, ?)", (name, subject))
    conn.commit()
    conn.close()

def add_marks(student_id, subject, marks):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO marks (student_id, subject, marks) VALUES (?, ?, ?)", (student_id, subject, marks))
    conn.commit()
    conn.close()

def add_attendance(student_id, date, status):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)", (student_id, date, status))
    conn.commit()
    conn.close()

def send_message(sender, receiver, message):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (sender, receiver, message) VALUES (?, ?, ?)", (sender, receiver, message))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def view_teachers():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT * FROM teachers")
    data = c.fetchall()
    conn.close()
    return data

def view_marks(student_id):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT subject, marks FROM marks WHERE student_id = ?", (student_id,))
    data = c.fetchall()
    conn.close()
    return data

def view_attendance(student_id):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT date, status FROM attendance WHERE student_id = ?", (student_id,))
    data = c.fetchall()
    conn.close()
    return data

def view_messages():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT sender, receiver, message FROM messages")
    data = c.fetchall()
    conn.close()
    return data

def main():
    st.title("🏫 School Management System")
    menu = ["🏠 Home", "👨‍🎓 Add Student", "👩‍🏫 Add Teacher", "📜 Add Marksheet", "📆 Add Attendance", "💬 Send Message", "👀 View Students", "👀 View Teachers", "📄 View Marksheet", "📋 View Attendance", "📩 View Messages"]
    choice = st.sidebar.selectbox("📌 Menu", menu)
    
    create_db()
    
    if choice == "🏠 Home":
        st.subheader("Welcome to the School Management System 🎓")
    elif choice == "👨‍🎓 Add Student":
        st.subheader("Add Student 🏫")
        name = st.text_input("Student Name")
        age = st.number_input("Age", min_value=5, max_value=20, step=1)
        grade = st.text_input("Grade")
        if st.button("Add Student ✅"):
            add_student(name, age, grade)
            st.success("Student added successfully! 🎉")
    elif choice == "👩‍🏫 Add Teacher":
        st.subheader("Add Teacher 👩‍🏫")
        name = st.text_input("Teacher Name")
        subject = st.text_input("Subject")
        if st.button("Add Teacher ✅"):
            add_teacher(name, subject)
            st.success("Teacher added successfully! 🎉")
    elif choice == "📜 Add Marksheet":
        st.subheader("Add Marksheet 📝")
        student_id = st.number_input("Student ID", min_value=1, step=1)
        subject = st.text_input("Subject")
        marks = st.number_input("Marks", min_value=0, max_value=100, step=1)
        if st.button("Add Marksheet ✅"):
            add_marks(student_id, subject, marks)
            st.success("Marks added successfully! 🎉")
    elif choice == "📆 Add Attendance":
        st.subheader("Add Attendance 📅")
        student_id = st.number_input("Student ID", min_value=1, step=1)
        date = st.date_input("Date")
        status = st.selectbox("Status", ["Present", "Absent"])
        if st.button("Add Attendance ✅"):
            add_attendance(student_id, str(date), status)
            st.success("Attendance recorded! ✅")
    elif choice == "💬 Send Message":
        st.subheader("Send Message 💌")
        sender = st.text_input("Sender")
        receiver = st.text_input("Receiver")
        message = st.text_area("Message")
        if st.button("Send Message ✅"):
            send_message(sender, receiver, message)
            st.success("Message sent successfully! 📩")
    elif choice == "📄 View Marksheet":
        st.subheader("View Marksheet 📑")
        student_id = st.number_input("Student ID", min_value=1, step=1)
        if st.button("Show Marks 📊"):
            marks = view_marks(student_id)
            for subject, mark in marks:
                st.write(f"📚 {subject}: {mark} marks")
    elif choice == "📋 View Attendance":
        st.subheader("View Attendance 📆")
        student_id = st.number_input("Student ID", min_value=1, step=1)
        if st.button("Show Attendance 📜"):
            attendance = view_attendance(student_id)
            for date, status in attendance:
                st.write(f"📅 {date}: {status}")
    elif choice == "📩 View Messages":
        st.subheader("View Messages 💌")
        messages = view_messages()
        for sender, receiver, message in messages:
            st.write(f"✉️ {sender} ➡️ {receiver}: {message}")

if __name__ == "__main__":
    main()

