import streamlit as st
import pickle
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Scholarship Recommendation System",
    page_icon="🎓",
    layout="wide"
)

# Load Data
df = pickle.load(open("schoolrship.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# Recommendation Function
def recommend(scholarship_name):
    index = df[df['Scholarship Name'] == scholarship_name].index[0]

    distances = similarity[index]

    scholarship_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in scholarship_list:
        recommendations.append(df.iloc[i[0]])

    return recommendations


# Title
st.title("🎓 Scholarship Recommendation System")
st.markdown("Get similar scholarships based on your selected scholarship.")

# Dropdown
scholarship_list = df['Scholarship Name'].unique()

selected_scholarship = st.selectbox(
    "Select a Scholarship",
    scholarship_list
)

# Button
if st.button("Recommend Scholarships"):

    recommendations = recommend(selected_scholarship)

    st.subheader("Recommended Scholarships")

    for rec in recommendations:

        with st.container():
            st.markdown("---")

            st.markdown(f"### {rec['Scholarship Name']}")

            if 'Amount' in df.columns:
                st.write(f"💰 **Amount:** {rec['Amount']}")

            if 'Location' in df.columns:
                st.write(f"📍 **Location:** {rec['Location']}")

            if 'Years' in df.columns:   
                st.write(f"📅 **Years:** {rec['Years']}")

            if 'Description' in df.columns:
                st.write("📝 **Description:**")
                st.write(rec['Description'])
