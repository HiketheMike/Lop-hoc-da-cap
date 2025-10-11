# ...existing code...
# <VSCode.Cell id="#VSC-6011bf7c" language="python">
# import seaborn as sns
# </VSCode.Cell>

# --- Start of Streamlit App Code ---
import streamlit as st
from datetime import datetime

# --- Page Configuration ---
# This function sets up the overall look and feel of your Streamlit app in the browser.
# It defines the browser tab title, an icon, and the layout of the content.
st.set_page_config(
    page_title="Ecopure: Green Bottle Cleaner", # Title for the browser tab
    page_icon="🌿", # An emoji or URL to an image for the tab icon
    layout="centered", # 'centered' (default) or 'wide' for content width
    initial_sidebar_state="collapsed" # 'auto', 'expanded', or 'collapsed' for the sidebar
)

# --- Session State for Comments ---
# Streamlit applications re-run from top to bottom every time a user interacts with a widget.
# `st.session_state` is crucial for storing and persisting variables (like our comments list)
# across these reruns, so data isn't lost.
if 'comments' not in st.session_state:
    st.session_state.comments = [
        {"name": "Anna L.", "comment": "Ecopure is amazing! My water bottle has never been cleaner, and I love that it's eco-friendly.", "date": "2025-09-28"},
        {"name": "Ben K.", "comment": "Finally, a cleaner that works without harsh chemicals. Highly recommend!", "date": "2025-10-01"},
        {"name": "Chloe P.", "comment": "The best way to keep my reusable bottles fresh. No weird aftertaste!", "date": "2025-10-05"}
    ]

# --- Header Section ---
# This section introduces your product and brand.
# Use st.image for your logo. Replace the URL with your actual logo image if you have one.
st.image("https://via.placeholder.com/150x150?text=Ecopure+Logo", width=100)
st.title("🌿 Ecopure: The Green Way to Clean Your Water Bottles")
st.markdown("""
    *Your trusted partner for a sparkling clean and eco-conscious hydration experience.*
    """)

# --- About Ecopure Section ---
# Provide a detailed description of your product, emphasizing its "green" aspects.
st.header("About Ecopure")
st.write("""
    At Ecopure, we are dedicated to providing an innovative and environmentally responsible solution
    for maintaining the hygiene of your reusable water bottles. Our unique formula is crafted
    to effectively eliminate stubborn residues, unpleasant odors, and harmful bacteria, ensuring
    your bottles are not just clean, but truly pristine.

    We are proud to emphasize our commitment to the planet: Ecopure is made with **100% plant-based ingredients**
    and features a **fully biodegradable formula**. This means you can enjoy a fresh, clean bottle
    without contributing to environmental pollution. Choose Ecopure for a healthier you and a healthier Earth.
    """)
# Replace the URL with an actual product image.
st.image("https://via.placeholder.com/700x350?text=Ecopure+Product+Image", caption="Ecopure Water Bottle Cleaner: Clean, Green, Pristine.", use_column_width=True)

# --- Product Features Section ---
# Highlight key benefits and features using columns for a clean layout.
st.header("Why Choose Ecopure?")
col1, col2, col3 = st.columns(3) # Creates three columns for side-by-side content
with col1:
    st.subheader("🌱 Eco-Friendly Formula")
    st.write("Our cleaner is derived from natural, sustainable plant sources, ensuring zero harm to aquatic life or ecosystems.")
with col2:
    st.subheader("✨ Superior Cleaning Power")
    st.write("Experience a deep clean that effortlessly removes grime, bacteria, and lingering odors, reaching every crevice of your bottle.")
with col3:
    st.subheader("💧 Safe & Gentle")
    st.write("Completely free from harsh chemicals, phosphates, parabens, and artificial dyes. Safe for all bottle materials and your entire family.")

# --- Buy Now Section (Simulated) ---
# This section simulates a product purchase without actual payment processing.
st.header("Get Your Ecopure Today!")
st.subheader("Ecopure Water Bottle Cleaner - 500ml Bottle")
st.metric(label="Price", value="$12.99", delta="-5% Today Only!") # `delta` adds a small indicator for price changes
st.write("Invest in the longevity and hygiene of your reusable water bottles with Ecopure. A small step for a big impact!")

# A simulated "Add to Cart" button. When clicked, it shows a success message.
if st.button("🛒 Add to Cart"):
    st.success("Product 'Ecopure Water Bottle Cleaner' added to your cart! (This is a simulated purchase for demonstration purposes.)")
    st.balloons() # A fun visual effect for success

# --- Customer Testimonials/Comments Section ---
# Display existing comments and allow users to add new ones.
st.header("What Our Customers Say")
st.markdown("---") # A horizontal line for separation
for comment_data in st.session_state.comments:
    st.markdown(f"**{comment_data['name']}** on *{comment_data['date']}*")
    st.info(f"\"{comment_data['comment']}\"") # `st.info` displays text in an informational box
    st.markdown("---")

st.subheader("Leave Your Own Comment")
# `st.form` groups input widgets and a submit button. It ensures that the form's
# logic only runs when the submit button is pressed, and `clear_on_submit=True`
# automatically clears the input fields after submission.
with st.form("comment_form", clear_on_submit=True):
    user_name = st.text_input("Your Name", max_chars=50)
    user_comment = st.text_area("Your Comment", max_chars=500)
    submitted = st.form_submit_button("Submit Comment")
    if submitted:
        if user_name and user_comment:
            new_comment = {
                "name": user_name,
                "comment": user_comment,
                "date": datetime.now().strftime("%Y-%m-%d") # Get current date
            }
            st.session_state.comments.append(new_comment) # Add new comment to session state
            st.success("Thank you for your comment! It has been added to the list.")
            # `st.experimental_rerun()` forces the app to re-run immediately,
            # which is necessary here to display the newly added comment without
            # requiring another user interaction.
            st.rerun()
        else:
            st.warning("Please enter both your name and comment before submitting.")

# --- Customer Service / Contact Us Section (Simulated) ---
# A mock contact form for customer inquiries.
st.header("Contact Our Customer Service")
st.write("Have questions about Ecopure, your order, or just want to say hello? We're here to help!")

with st.form("contact_form", clear_on_submit=True):
    contact_name = st.text_input("Your Name", max_chars=50)
    contact_email = st.text_input("Your Email", help="We'll use this to get back to you.")
    contact_subject = st.text_input("Subject", max_chars=100)
    contact_message = st.text_area("Your Message", max_chars=1000)
    contact_submitted = st.form_submit_button("Send Message")
    if contact_submitted:
        if contact_name and contact_email and contact_message:
            st.success(f"Thank you, {contact_name}! Your message regarding '{contact_subject}' has been sent. We will get back to you at {contact_email} shortly. (This is a simulated message send.)")
        else:
            st.warning("Please fill in all required fields (Name, Email, Message).")

# --- Footer ---
# A simple footer with copyright and contact information.
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: gray; font-size: small;'>
        &copy; 2025 Ecopure. All rights reserved. | Email: <a href='mailto:info@ecopure.com' style='color: gray;'>info@ecopure.com</a> | Follow us on social media!
    </p>
    """, unsafe_allow_html=True) # `unsafe_allow_html=True` allows rendering raw HTML
# --- End of Streamlit App Code ---