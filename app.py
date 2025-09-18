from openai import OpenAI
import streamlit as st

# Initialize OpenAI client (it will pick up your API key from the environment variable)
client = OpenAI()

st.title("Gen AI Prototype 🚀")
st.write("Paste some startup info and get a quick AI-powered summary!")

# Input box
startup_info = st.text_area("Enter Startup Info:")

if st.button("Generate Summary"):
    st.write("✨ Thinking...")

    try:
        # Call OpenAI with the new syntax
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # fast + cheap model
            messages=[
                {"role": "system", "content": "You are a helpful AI that summarizes startup information."},
                {"role": "user", "content": startup_info}
            ],
            max_tokens=200
        )

        # Extract AI response
        summary = response.choices[0].message.content
        st.subheader("AI-Generated Summary:")
        st.write(summary)

    except Exception as e:
        st.error(f"Error: {e}")
