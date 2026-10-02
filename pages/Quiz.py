import streamlit as st

# beach -> (image, description)
beach_data = {
    "Praia do Futuro": (
        "Images/futuro.jpg",
        "Fortaleza's lively city beach, with big waves and beach bars (barracas) serving fresh seafood "
        "while forró plays. You love energy, music, and great food with your friends.",
    ),
    "Jericoacoara": (
        "Images/jericoacoara.jpg",
        "A small village of sand streets, giant dunes, and famous sunsets. You love calm, "
        "nature, and adventures that are worth the long trip.",
    ),
    "Canoa Quebrada": (
        "Images/canoa.jpg",
        "A relaxed village with red cliffs, craft shops, and a busy street full of live music at night. "
        "You love culture, art, and slow evenings.",
    ),
    "Cumbuco": (
        "Images/cumbuco.jpg",
        "A windy beach close to Fortaleza, famous for kitesurfing, dune buggies, and lagoons. "
        "You love sports, speed, and a day full of action.",
    ),
}

st.title("Which Beach in Ceará Are You?")
st.image("Images/quiz_banner.jpg")
st.write("Answer six questions and I will match you with one of four beaches in Ceará, Brazil.")

st.subheader("Meet the beaches")
beach_columns = st.columns(4)
position = 0
for beach_name, (image_path, description) in beach_data.items():
    with beach_columns[position]:
        st.image(image_path, caption=beach_name)
    position = position + 1

st.divider()

# all the questions go inside one form, nothing runs until the button is clicked
with st.form("beach_quiz"):  #NEW
    q1 = st.radio(  #NEW
        "1. How would you like to start your beach day?",
        [
            "Coconut water at a beach bar with live music",
            "Sunrise in a hammock, with no plans",
            "Exploring cliffs and craft shops",
            "Checking the wind for a sports session",
        ],
    )

    q2 = st.selectbox(  #NEW
        "2. Which Ceará food do you choose for lunch?",
        [
            "Caranguejo (crab)",
            "Grilled fish with baião de dois",
            "Tapioca with coalho cheese",
            "Pastel with sugarcane juice",
        ],
    )

    q3 = st.multiselect(  #NEW
        "3. Pick everything you would love to do:",
        [
            "Dance forró",
            "Eat at a beach bar (barraca)",
            "Watch the sunset from a giant dune",
            "Sleep in a hammock by the sea",
            "Buy handmade crafts",
            "Walk along red cliffs",
            "Ride a dune buggy",
            "Try kitesurfing",
        ],
    )

    q4 = st.slider("4. From 0 (total relaxation) to 10 (total adventure), how adventurous are you?", 0, 10, 5)  #NEW

    q5 = st.number_input("5. How many days can you stay?", min_value=1, max_value=15, value=3, step=1)  #NEW

    q6 = st.radio(  #NEW
        "6. What is your plan for the night?",
        [
            "A beach bar with forró",
            "Looking at the stars on the sand",
            "A street full of bars and live music",
            "Going to bed early to be ready for the wind",
        ],
    )

    submitted = st.form_submit_button("See my beach")  #NEW

# answer -> beach
q1_points = {
    "Coconut water at a beach bar with live music": "Praia do Futuro",
    "Sunrise in a hammock, with no plans": "Jericoacoara",
    "Exploring cliffs and craft shops": "Canoa Quebrada",
    "Checking the wind for a sports session": "Cumbuco",
}

q2_points = {
    "Caranguejo (crab)": "Praia do Futuro",
    "Grilled fish with baião de dois": "Jericoacoara",
    "Tapioca with coalho cheese": "Canoa Quebrada",
    "Pastel with sugarcane juice": "Cumbuco",
}

q3_points = {
    "Dance forró": "Praia do Futuro",
    "Eat at a beach bar (barraca)": "Praia do Futuro",
    "Watch the sunset from a giant dune": "Jericoacoara",
    "Sleep in a hammock by the sea": "Jericoacoara",
    "Buy handmade crafts": "Canoa Quebrada",
    "Walk along red cliffs": "Canoa Quebrada",
    "Ride a dune buggy": "Cumbuco",
    "Try kitesurfing": "Cumbuco",
}

q6_points = {
    "A beach bar with forró": "Praia do Futuro",
    "Looking at the stars on the sand": "Jericoacoara",
    "A street full of bars and live music": "Canoa Quebrada",
    "Going to bed early to be ready for the wind": "Cumbuco",
}

# the result only shows after the form is submitted
if submitted:
    scores = {"Praia do Futuro": 0, "Jericoacoara": 0, "Canoa Quebrada": 0, "Cumbuco": 0}

    scores[q1_points[q1]] += 2
    scores[q2_points[q2]] += 2
    scores[q6_points[q6]] += 2

    for activity in q3:
        scores[q3_points[activity]] += 1

    if q4 <= 3:
        scores["Praia do Futuro"] += 1
        scores["Canoa Quebrada"] += 1
    elif q4 <= 6:
        scores["Canoa Quebrada"] += 1
        scores["Jericoacoara"] += 1
    else:
        scores["Jericoacoara"] += 1
        scores["Cumbuco"] += 1

    if q5 <= 2:
        scores["Praia do Futuro"] += 1
        scores["Cumbuco"] += 1
    elif q5 <= 4:
        scores["Canoa Quebrada"] += 2
    else:
        scores["Jericoacoara"] += 2

    # best beach, the first one wins if there is a tie
    best_beach = ""
    best_score = -1
    for beach_name, score in scores.items():
        if score > best_score:
            best_score = score
            best_beach = beach_name

    total_points = sum(scores.values())
    percent = round(best_score / total_points * 100)

    st.header("Your beach is " + best_beach + "!")
    st.image(beach_data[best_beach][0])
    st.write(beach_data[best_beach][1])
    st.metric("Share of your answers that point to this beach", str(percent) + "%")  #NEW
    st.balloons()  #NEW
    st.toast("Enjoy " + best_beach + "!")  #EXTRA

    st.subheader("Your points for every beach")
    for beach_name, score in scores.items():
        st.write("**" + beach_name + ":** " + str(score))
