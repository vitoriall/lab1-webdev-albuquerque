import streamlit as st
import info
import pandas as pd

st.title("My Portfolio")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(info.profile_picture, width=250)

with col2:
    st.header(info.full_name)
    st.write(info.about_me)

    # one column per tag so the badges sit side by side
    tag_columns = st.columns(len(info.interest_tags))
    for i in range(len(info.interest_tags)):
        with tag_columns[i]:
            st.badge(info.interest_tags[i])  #EXTRA

link_col1, link_col2, link_col3 = st.columns(3)

with link_col1:
    st.image(info.linkedin_image_url, width=40)
    st.link_button("LinkedIn", info.my_linkedin_url)  #EXTRA

with link_col2:
    st.image(info.github_image_url, width=40)
    st.link_button("GitHub", info.my_github_url)  #EXTRA

with link_col3:
    st.image(info.email_image_url, width=40)
    st.write(info.my_email_address)

st.divider()

st.header("Education")
for label, value in info.education_data.items():
    st.write("**" + label + ":** " + value)

st.divider()

st.header("Courses")
# dictionary of lists -> table
courses_table = pd.DataFrame(info.course_data)
courses_table.columns = ["Code", "Course", "Semester Taken", "Skills Learned"]
st.dataframe(courses_table, hide_index=True)

st.divider()

st.header("Experience")
# each value is a tuple, so it gets unpacked into bullets and image_path
for title, (bullets, image_path) in info.experience_data.items():
    with st.expander(title, expanded=True):  #EXTRA
        text_col, image_col = st.columns([2, 1])
        with text_col:
            for bullet in bullets:
                st.write(bullet)
        with image_col:
            st.image(image_path)

st.divider()

st.header("Projects")
for name, description in info.projects_data.items():
    st.subheader(name)
    st.write(description)

st.divider()

st.header("Programming Skills")
for skill, level in info.programming_data.items():
    icon = info.programming_icons[skill]
    st.progress(level, text=icon + " " + skill)

st.divider()

st.header("Languages")
for language, level in info.spoken_data.items():
    icon = info.spoken_icons[language]
    st.write(icon + " **" + language + ":** " + level)

st.divider()

st.header("Leadership")
for title, (bullets, image_path) in info.leadership_data.items():
    st.subheader(title)
    text_col, image_col = st.columns([2, 1])
    with text_col:
        for bullet in bullets:
            st.write(bullet)
    with image_col:
        st.image(image_path)

st.divider()

st.header("Activities")
for name, bullets in info.activity_data.items():
    st.subheader(name)
    for bullet in bullets:
        st.write(bullet)
