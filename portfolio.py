import streamlit as st

# Set the page title
st.set_page_config(page_title="Student Portfolio", page_icon="🎓", layout="wide")

# Side navigation 
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Customize Profile", "Contact", "Testimonials"])

# Home Section 
if page == "Home":
    st.title("🎓 Student Portfolio")
    
    # Profile picture upload
    uploaded_image = st.file_uploader("Upload profile picture", type=['png', 'jpg', 'jpeg'])
    if uploaded_image is not None:
        st.image(uploaded_image, caption='Profile Pic', width=150)
    else: 
        st.image("person.jpg.", caption='Default Profile Picture', width=150)
    
    # User Editable Student Details
    name = st.text_input("Your Name", "Karigirwa henriette")
    location = st.text_input("Location", "Musanze, Rwanda")
    field_of_study = st.text_input("Field of Study", "Software Engineering")
    university = st.text_input("University", "INES-Ruhengeri")
    
    st.write(f"😎 {name}")
    st.write(f"📍 {location}")
    st.write(f"📚 {field_of_study}")
    st.write(f"🏫 {university}")
    
    # CV Upload & Download
    uploaded_cv = st.file_uploader("Upload your CV (PDF)", type=['pdf'])
    if uploaded_cv is not None:
        with open("assets/uploaded_cv.pdf", "wb") as f:
            f.write(uploaded_cv.getbuffer())
        st.success("CV uploaded successfully!")
    
    with open("Karigirwa. CV.pdf", "rb") as file:
        st.download_button(label="📄 Download My Resume", data=file, file_name="My_Resume.pdf")
    
    # "Deep Me" Button for More Information
    if st.button("🔍 Deep Me"):
        st.subheader("Personal Information")
        st.write("- *Full Name:* Karigirwa henriette")
        st.write("- *Date of Birth:* 21/06/2001")
        st.write("- *Nationality:* Rwandan")
        st.write("- *Gender:* female")
        st.write("- *Marital Status:* Single")
        st.write("- *Email:* henriettek.16@gmail.com")
        st.write("- *Phone:* 0786910365")
        st.write("- *Residence:* Kigali, Gasabo, Kimihurura")

# Projects Page
elif page == "Projects":
    st.title("💻 Projects")
    
    with st.expander("📊 AI-Based Loan Evaluation System (Final Year Project)"):
        st.write("*Project Type:* Individual Dissertation")
        st.write("*Description:* Developed an AI-powered system to evaluate loan eligibility using OCR and data analysis.")
        st.write("*Technologies:* Python, TensorFlow, Django, PostgreSQL")
        st.write("[GitHub Repository](https://github.com/henriette03/loan-evaluation)")
    
    with st.expander("📡 Hospital Management System (Year 3 Project)"):
        st.write("*Project Type:* Group Assignment")
        st.write("*Description:* A web-based platform for managing hospital operations including patient records, doctor appointments, and ambulance services.")
        st.write("*Technologies:* HTML, CSS, JavaScript, PHP, MariaDB")
    
    with st.expander("🛍 E-Commerce Platform (Year 2 Project)"):
        st.write("*Project Type:* Individual Project")
        st.write("*Description:* Built an e-commerce website where users can buy and sell products online.")
        st.write("*Technologies:* React, Firebase, Node.js")

# Skills Page
elif page == "Skills":
    st.title("📊 Skills & Achievements")
    st.write("Here are my technical and soft skills.")
    
    st.write("### Programming Languages")
    st.progress(80)
    st.write("Python")
    st.progress(70)
    st.write("JavaScript")
    st.progress(85)
    st.write("SQL")
    
    st.write("### Web Development")
    st.progress(75)
    st.write("HTML, CSS, React, Flask")
    
    st.write("### Certifications & Achievements")
    st.write("✔ Completed Google Data Analytics Certification")
    st.write("✔Alx Software engineering programme with a secialized in Front-end")

# Customize Profile Page
elif page == "Customize Profile":
    st.title("🛠 Customize Your Profile")
    st.write("Modify your details dynamically.")
    bio = st.text_area("Write your bio", "I am passionate about AI and Web Development.")
    skills = st.text_area("List your skills", "Python, JavaScript, SQL, React, Flask")
    if st.button("Save Changes"):
        st.success("Profile updated successfully!")

# Contact Page
elif page == "Contact":
    st.title("📩 Contact Me")
    st.write("Get in touch via email or social media.")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        st.success("Message sent successfully!")
    
    st.write("📧 Email: henriettek.@gmail.com")
    st.write("📱 Phone: 0786910365")
    st.write("🔗 [LinkedIn](linkedin.com/in/karigirwa-henriette-404063265)")
    st.write("🔗 [GitHub](https://github.com/henriette03)")

# Testimonials Page
elif page == "Testimonials":
    st.title("🗣 Testimonials")
    st.write("What others say about me.")
    st.write("- 'henriette is an excellent problem solver and has great coding skills!' - Dr. Theodore")
    st.write("- 'His final year project was innovative and impactful!' -Mrs. Queen")
    new_testimonial = st.text_area("Write a testimonial about me")
    if st.button("Submit Testimonial"):
        st.success("Thank you for your feedback!")