# ...existing code...
# <VSCode.Cell id="#VSC-6011bf7c" language="python">
# import seaborn as sns
# </VSCode.Cell>

# --- Start of Streamlit App Code ---
import streamlit as st
from datetime import datetime
import json
import os # Import os module for path operations

# Define the path for the comments JSON file
COMMENTS_FILE = "comments.json"

# --- Functions to handle comments persistence ---
def load_comments():
    """Loads comments from a JSON file. If the file doesn't exist, returns default comments."""
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Default comments if the file doesn't exist
        return [
            {"name": "Anna L.", "comment": "Ecopure is amazing! My water bottle has never been cleaner, and I love that it's eco-friendly.", "date": "2025-09-28", "rating": 5},
            {"name": "Ben K.", "comment": "Finally, a cleaner that works without harsh chemicals. Highly recommend!", "date": "2025-10-01", "rating": 4},
            {"name": "Chloe P.", "comment": "The best way to keep my reusable bottles fresh. No weird aftertaste!", "date": "2025-10-05", "rating": 5},
            {"name": "David M.", "comment": "Good product, does what it says. A bit pricey but worth it for the eco-friendly aspect.", "date": "2025-10-08", "rating": 4}
        ]

def save_comments(comments_list):
    """Saves the current list of comments to a JSON file."""
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comments_list, f, indent=4, ensure_ascii=False)

# --- Page Configuration ---
st.set_page_config(
    page_title="Ecopure: Green Bottle Cleaner",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded" # Changed to 'expanded' to show sidebar by default
)

# --- Session State for Comments ---
# Load comments from the file when the app starts or session initializes
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# --- Header Section (Always visible, above sidebar and main content) ---
st.image("https://via.placeholder.com/150x150?text=Ecopure+Logo", width=100)
st.title("🌿 Ecopure: The Green Way to Clean Your Water Bottles")
st.markdown("""
    *Your trusted partner for a sparkling clean and eco-conscious hydration experience.*
    """)

# --- Sidebar Navigation ---
st.sidebar.header("Navigation")

# The "expand on hover" effect for symbols is not natively supported by Streamlit's radio buttons.
# We'll use emojis with text labels for clear navigation.
selected_page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "🛍️ Products", "🌟 Customer Reviews", "📞 Contact Us"],
    index=0 # Default to Home page
)

# --- Main Content Area based on Sidebar Selection ---
if selected_page == "🏠 Home":
    st.header("Welcome to Ecopure!")
    st.write("""
        Discover the revolutionary way to keep your reusable water bottles impeccably clean and fresh,
        all while being kind to our planet. Ecopure offers a powerful, plant-based solution designed
        for the modern eco-conscious individual.
        """)

    # About Ecopure Section
    st.subheader("About Our Mission")
    st.write("""
        At Ecopure, we are dedicated to providing an innovative and environmentally responsible solution
        for maintaining the hygiene of your reusable water bottles. Our unique formula is crafted
        to effectively eliminate stubborn residues, unpleasant odors, and harmful bacteria, ensuring
        your bottles are not just clean, but truly pristine.

        We are proud to emphasize our commitment to the planet: Ecopure is made with **100% plant-based ingredients**
        and features a **fully biodegradable formula**. This means you can enjoy a fresh, clean bottle
        without contributing to environmental pollution. Choose Ecopure for a healthier you and a healthier Earth.
        """)
    st.image("https://via.placeholder.com/700x350?text=Ecopure+Product+Image", caption="Ecopure Water Bottle Cleaner: Clean, Green, Pristine.", use_column_width=True)

    # Product Features Section
    st.subheader("Why Choose Ecopure?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🌱 Eco-Friendly Formula")
        st.write("Our cleaner is derived from natural, sustainable plant sources, ensuring zero harm to aquatic life or ecosystems.")
    with col2:
        st.markdown("### ✨ Superior Cleaning Power")
        st.write("Experience a deep clean that effortlessly removes grime, bacteria, and lingering odors, reaching every crevice of your bottle.")
    with col3:
        st.markdown("### 💧 Safe & Gentle")
        st.write("Completely free from harsh chemicals, phosphates, parabens, and artificial dyes. Safe for all bottle materials and your entire family.")

elif selected_page == "🛍️ Products":
    st.header("Our Products")
    st.write("Explore our range of eco-friendly cleaning solutions designed for your sustainable lifestyle.")

    st.subheader("Ecopure Water Bottle Cleaner - 500ml Bottle")
    st.image("https://via.placeholder.com/400x400?text=Ecopure+500ml+Bottle", caption="Ecopure 500ml Bottle", width=250)
    st.metric(label="Price", value="$12.99", delta="-5% Today Only!")
    st.markdown("""
        Our flagship product! This 500ml bottle provides ample solution for months of sparkling clean
        bottles. Its concentrated formula means a little goes a long way.
        *   **Volume:** 500ml
        *   **Ingredients:** 100% Plant-based, Biodegradable
        *   **Best for:** Daily cleaning, deep sanitization
        """)
    if st.button("🛒 Add 500ml Bottle to Cart"):
        st.success("Product 'Ecopure Water Bottle Cleaner (500ml)' added to your cart! (Simulated)")
        st.balloons()

    st.markdown("---")

    st.subheader("Ecopure Travel Size Cleaner - 100ml Spray")
    st.image("https://via.placeholder.com/200x200?text=Ecopure+Travel+Spray", caption="Ecopure 100ml Travel Spray", width=150)
    st.metric(label="Price", value="$5.99")
    st.markdown("""
        Perfect for on-the-go freshness! This compact spray bottle is ideal for quick cleans
        during travel, at the gym, or in the office.
        *   **Volume:** 100ml
        *   **Ingredients:** 100% Plant-based, Biodegradable
        *   **Best for:** Quick refreshes, travel
        """)
    if st.button("🛒 Add Travel Spray to Cart"):
        st.success("Product 'Ecopure Travel Size Cleaner (100ml)' added to your cart! (Simulated)")
        st.balloons()

elif selected_page == "🌟 Customer Reviews":
    st.header("What Our Customers Say")
    st.write("Hear directly from the Ecopure community about their experiences.")
    st.markdown("---")

    # Calculate and display average rating
    if st.session_state.comments:
        total_ratings = sum(c['rating'] for c in st.session_state.comments if 'rating' in c)
        num_rated_comments = sum(1 for c in st.session_state.comments if 'rating' in c)
        if num_rated_comments > 0:
            average_rating = total_ratings / num_rated_comments
            stars = "⭐" * int(round(average_rating))
            st.subheader(f"Overall Customer Rating: {stars} ({average_rating:.1f}/5.0)")
        else:
            st.subheader("No ratings yet.")
    else:
        st.subheader("No comments or ratings yet.")

    st.markdown("---")

    for comment_data in st.session_state.comments:
        rating_stars = "⭐" * comment_data.get('rating', 0) # Display stars based on rating
        st.markdown(f"**{comment_data['name']}** {rating_stars} on *{comment_data['date']}*")
        st.info(f"\"{comment_data['comment']}\"")
        st.markdown("---")

    st.subheader("Leave Your Own Comment")
    with st.form("comment_form", clear_on_submit=True):
        user_name = st.text_input("Your Name", max_chars=50)
        user_comment = st.text_area("Your Comment", max_chars=500)
        user_rating = st.slider("Your Rating", min_value=1, max_value=5, value=5, help="Rate your experience from 1 (Poor) to 5 (Excellent)")
        submitted = st.form_submit_button("Submit Comment")
        if submitted:
            if user_name and user_comment:
                new_comment = {
                    "name": user_name,
                    "comment": user_comment,
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "rating": user_rating
                }
                st.session_state.comments.append(new_comment)
                save_comments(st.session_state.comments) # Save comments to file
                st.success("Thank you for your comment and rating! It has been added to the list.")
                st.rerun()
            else:
                st.warning("Please enter both your name and comment before submitting.")

elif selected_page == "📞 Contact Us":
    st.header("Contact Our Customer Service")
    st.write("Have questions about Ecopure, your order, or just want to say hello? We're here to help!")
    st.markdown("---")

    st.subheader("Send Us a Message")
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

    st.markdown("---")
    st.subheader("Other Ways to Reach Us")
    st.markdown("""
        **Email:** info@ecopure.com  
        **Phone:** +1 (800) 555-0123 (Mon-Fri, 9 AM - 5 PM EST)  
        **Address:** 123 Green Street, Eco City, EC 12345
        """)
    st.markdown("---")
    st.subheader("Follow Us")
    st.markdown("""
        [Facebook](https://facebook.com/ecopure) |
        [Instagram](https://instagram.com/ecopure) |
        [Twitter](https://twitter.com/ecopure)
        """)

# --- Footer (Always visible, below main content) ---
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: gray; font-size: small;'>
        &copy; 2025 Ecopure. All rights reserved. | Email: <a href='mailto:info@ecopure.com' style='color: gray;'>info@ecopure.com</a>
    </p>
    """, unsafe_allow_html=True)
# --- End of Streamlit App Code ---