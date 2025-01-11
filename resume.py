import streamlit as st
import os

# Helper function to generate resume text
def generate_resume(data):
    resume = f"""
    =================================================
                           {data['name'].upper()}
    =================================================

    Contact Information:
    ---------------------
    Email: {data['email']}
    Phone: {data['phone']}
    {"LinkedIn: " + data['linkedin'] if data['linkedin'] else ""}
    {"GitHub: " + data['github'] if data['github'] else ""}

    Objective:
    ----------
    {data['objective']}

    Education:
    ----------
    {"\n".join(data['education'])}

    Skills:
    -------
    {", ".join([skill.strip() for skill in data['skills']])}

    Experience:
    -----------
    {"\n\n".join(data['experience'])}

    Certifications:
    ----------------
    {"\n".join(data['certifications']) if data['certifications'] else "None"}
    =================================================
    """
    return resume.strip()

# Main app function
def app():
    st.set_page_config(page_title="Resume Builder", page_icon="📝", layout="wide")

    # Page header
    st.title("📝 Resume Builder")
    st.markdown(
        """
        Welcome to the **Resume Builder**! Fill out your details below to create a professional resume in just minutes. 
        Once completed, you can preview and download your resume.
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    # Form to collect resume data
    with st.form("resume_form", clear_on_submit=True):
        st.subheader("Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="John Doe")
            email = st.text_input("Email Address", placeholder="john.doe@example.com")
            phone = st.text_input("Phone Number", placeholder="+123456789")
        with col2:
            linkedin = st.text_input("LinkedIn Profile (optional)", placeholder="https://linkedin.com/in/username")
            github = st.text_input("GitHub Profile (optional)", placeholder="https://github.com/username")

        st.subheader("Objective")
        objective = st.text_area("Write a short objective for your resume", placeholder="Your career goals and aspirations.")

        st.subheader("Education")
        education = []
        num_education = st.number_input("Number of Educational Entries", min_value=1, max_value=10, step=1, value=1)
        for i in range(num_education):
            st.markdown(f"**Entry {i + 1}**")
            degree = st.text_input(f"Degree for Entry {i + 1}", placeholder="Bachelor of Science in Computer Science")
            institution = st.text_input(f"Institution for Entry {i + 1}", placeholder="Harvard University")
            year = st.text_input(f"Year of Graduation for Entry {i + 1}", placeholder="2025")
            education.append(f"{degree}, {institution} ({year})")

        st.subheader("Skills")
        skills = st.text_area(
            "Enter your skills (separated by commas)",
            placeholder="Python, Data Analysis, Machine Learning, Communication, etc.",
        ).split(",")

        st.subheader("Experience")
        experience = []
        num_experience = st.number_input("Number of Experience Entries", min_value=1, max_value=10, step=1, value=1)
        for i in range(num_experience):
            st.markdown(f"**Entry {i + 1}**")
            job_title = st.text_input(f"Job Title for Entry {i + 1}", placeholder="Software Engineer")
            company = st.text_input(f"Company for Entry {i + 1}", placeholder="Google")
            duration = st.text_input(f"Duration for Entry {i + 1}", placeholder="Jan 2021 - Present")
            job_desc = st.text_area(f"Job Description for Entry {i + 1}", placeholder="Your key responsibilities and achievements.")
            experience.append(f"{job_title} at {company} ({duration})\n   - {job_desc}")

        st.subheader("Certifications")
        certifications = []
        num_certifications = st.number_input("Number of Certification Entries", min_value=0, max_value=10, step=1, value=0)
        for i in range(num_certifications):
            st.markdown(f"**Entry {i + 1}**")
            cert = st.text_input(f"Certification for Entry {i + 1}", placeholder="Certified Data Scientist")
            org = st.text_input(f"Issued By (Organization) for Entry {i + 1}", placeholder="IBM")
            certifications.append(f"{cert}, issued by {org}")

        submitted = st.form_submit_button("Generate Resume")

    # Process and display the resume
    if submitted:
        if not name or not email or not phone or not objective:
            st.error("Please fill out all required fields (Name, Email, Phone, and Objective).")
        else:
            # Collect data
            data = {
                "name": name,
                "email": email,
                "phone": phone,
                "linkedin": linkedin,
                "github": github,
                "objective": objective,
                "education": education,
                "skills": skills,
                "experience": experience,
                "certifications": certifications,
            }

            # Generate resume text
            resume_text = generate_resume(data)

            # Display resume preview
            st.divider()
            st.subheader("Your Generated Resume")
            st.text(resume_text)

            # Provide a download button
            st.download_button(
                label="Download Resume as Text File",
                data=resume_text,
                file_name=f"{name.replace(' ', '_')}_Resume.txt",
                mime="text/plain",
            )

# Run the app
if __name__ == "__main__":
    app()

