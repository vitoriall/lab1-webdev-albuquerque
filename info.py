# data for my portfolio (no streamlit code in here)

full_name = "Vitória Albuquerque"

# about me
profile_picture = "Images/profile.jpeg"
home_picture = "Images/gatech.jpg"
about_me = (
    "Hi! I'm Vitória, a Computer Engineering student at Georgia Tech, originally from "
    "Fortaleza, Ceará, in Northeast Brazil. I like building products and using technology "
    "to open doors for other students, whether that's through machine learning research, "
    "software testing, or a social project for public-school students."
)

interest_tags = ["Machine Learning", "Product", "Education"]

# links
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://cdn-icons-png.flaticon.com/256/25/25231.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

my_linkedin_url = "https://www.linkedin.com/in/vitoria-albuquerque-tech"
my_github_url = "https://github.com/vitoriall"
my_email_address = "vitoriaalbuquerquestudent@gmail.com"

education_data = {
    "Degree": "Bachelor of Science in Computer Engineering",
    "Institution": "Georgia Institute of Technology",
    "Location": "Atlanta, GA",
    "Graduation Date": "Expected 2030",
    "GPA": "In progress (first semester)",
}

# every list has the same length, item 0 is course 0
course_data = {
    "code": ["CS 1301"],
    "names": ["Intro to Computing"],
    "semester_taken": ["1st"],
    "skills": ["Python, loops, and Streamlit"],
}

# title -> (bullet points, image path)
experience_data = {
    "Product Intern at iFood": (
        [
            "- Worked in a product role on the out-of-home dining team of a Brazilian food-delivery company",
            "- Learned how product, design, and engineering teams work together to decide what to build",
            "- Practiced turning user problems into clear features and priorities",
        ],
        "Images/ifood.jpg",
    ),
    "QA Intern at Nextek Sistemas": (
        [
            "- Tested software to find bugs before it reached users",
            "- Wrote clear bug reports so developers could reproduce and fix problems",
        ],
        "Images/nextek.jpg",
    ),
    "Machine Learning Researcher at RAITec/UFC and IFCE": (
        [
            "- Did machine learning research with university research groups in Ceará",
            "- Learned how to run experiments, test ideas, and explain results",
        ],
        "Images/research.jpg",
    ),
    "English Teacher at Melos English School": (
        [
            "- Taught English online to students at a school based in Recife",
            "- Practiced explaining hard ideas in a simple, patient way",
        ],
        "Images/teaching.jpeg",
    ),
}

projects_data = {
    "Ceará Beach Quiz": "An interactive quiz (the Quiz page of this app) that asks six questions and matches you "
                        "with a beach in Ceará: Praia do Futuro, Jericoacoara, Canoa Quebrada, or Cumbuco.",
    "This Portfolio": "A multi-page web app built with Streamlit for CS 1301 and deployed online.",
    "COJU Relaunch (future goal)": "Relaunching COJU with a virtual focus on financial education for public-school students.",
}

# skill -> level from 0 to 100
programming_data = {
    "Python": 80,
    "Machine Learning": 60,
    "Software Testing": 55,
}

programming_icons = {
    "Python": "🐍",
    "Machine Learning": "🤖",
    "Software Testing": "🧪",
}

spoken_icons = {
    "Portuguese": "🇧🇷",
    "English": "🇺🇸",
}

spoken_data = {
    "Portuguese": "Native",
    "English": "Fluent",
}

leadership_data = {
    "Co-founder of COJU": (
        [
            "- Co-founded a social initiative that offered job-market workshops and short technical and arts courses to public-school students",
            "- Built a community with significant reach among students",
            "- Now planning a relaunch focused on virtual financial education",
        ],
        "Images/coju.jpg",
    ),
}

activity_data = {
    "Behring Foundation Scholar": [
        "- Selected for a four-year scholarship to study at Georgia Tech",
    ],
}
