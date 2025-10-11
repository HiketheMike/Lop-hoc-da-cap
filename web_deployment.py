import streamlit as st
from datetime import datetime
import json # Added for JSON operations
import os   # Added for path operations

# Define the path for the comments JSON file
COMMENTS_FILE = "comments.json"

# --- Inject custom CSS for gradient background ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

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

# --- Sidebar Content ---
st.sidebar.image("https://via.placeholder.com/100x100?text=Logo", width=80) # Smaller logo for sidebar
st.sidebar.title("Ecopure")
st.sidebar.markdown("---") # Separator

st.sidebar.header("Navigation")
selected_page = st.sidebar.radio(
    "Go to",
    ["Home", "Products", "Customer Reviews", "Contact Us"],
    index=0
)
st.sidebar.markdown("---") # Separator

st.sidebar.subheader("Quick Contact")
st.sidebar.info("Email: info@ecopure.com\nPhone: +1 (800) 555-0123")

st.sidebar.subheader("Follow Us")
st.sidebar.markdown("""
    <div style="display: flex; justify-content: space-around; margin-top: 10px;">
        <a href="https://facebook.com/ecopure" target="_blank" style="color: white; text-decoration: none;">
            <img src="https://img.icons8.com/ios-filled/30/000000/facebook-new.png" alt="Facebook"/>
        </a>
        <a href="https://instagram.com/ecopure" target="_blank" style="color: white; text-decoration: none;">
            <img src="https://img.icons8.com/ios-filled/30/000000/instagram-new.png" alt="Instagram"/>
        </a>
        <a href="https://twitter.com/ecopure" target="_blank" style="color: white; text-decoration: none;">
            <img src="https://img.icons8.com/ios-filled/30/000000/twitter.png" alt="Twitter"/>
        </a>
    </div>
    """, unsafe_allow_html=True)


# --- Main Content Area based on Sidebar Selection ---
if selected_page == "🏠 Home":
    st.header("Welcome to Ecopure!")
    st.write("""
        Discover the revolutionary way to keep your reusable water bottles impeccably clean and fresh,
        all while being kind to our planet. Ecopure offers a powerful, plant-based solution designed
        for the modern eco-conscious individual.
        """)

    # About Ecopure Section using st.expander
    with st.expander("Learn More About Our Mission"):
        st.subheader("About Our Mission") # Subheader inside expander
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

    # Product Features Section using st.expander
    with st.expander("Why Choose Ecopure?"):
        st.subheader("Why Choose Ecopure?") # Subheader inside expander
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("#### 🌱 Plant-Based")
            st.write("Made with natural, eco-friendly ingredients.")
        with col2:
            st.markdown("#### ✨ Sparkling Clean")
            st.write("Removes odors and residues effectively.")
        with col3:
            st.markdown("#### 🌍 Earth-Friendly")
            st.write("Biodegradable formula, safe for the planet.")

elif selected_page == "🛍️ Products":
    st.header("Our Products")
    st.write("Explore our range of eco-friendly cleaning solutions designed for your sustainable lifestyle.")

    # Using st.container for each product for better visual separation
    with st.container(border=True): # border=True adds a visual border around the container
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
            st.success("500ml Bottle added to cart!")

    st.markdown("---") # Add a separator between products

    with st.container(border=True): # border=True adds a visual border around the container
        st.subheader("Ecopure Travel-Size Cleaner - 100ml Spray")
        st.image("https://via.placeholder.com/400x400?text=Ecopure+100ml+Spray", caption="Ecopure 100ml Spray", width=250)
        st.metric(label="Price", value="$5.99")
        st.markdown("""
            Perfect for on-the-go freshness! This compact spray bottle is ideal for quick cleans
            when you're traveling or at the gym.
            *   **Volume:** 100ml
            *   **Ingredients:** 100% Plant-based, Biodegradable
            *   **Best for:** Travel, quick refreshes
            """)
        if st.button("🛒 Add 100ml Spray to Cart"):
            st.success("100ml Spray added to cart!")

elif selected_page == "🌟 Customer Reviews":
    st.header("What Our Customers Say")
    st.write("Hear directly from the Ecopure community about their experiences.")
    st.markdown("---")

    # Calculate and display average rating
    if st.session_state.comments:
        avg_rating = sum(c['rating'] for c in st.session_state.comments) / len(st.session_state.comments)
        st.subheader(f"Average Rating: {avg_rating:.1f} ⭐")
    else:
        st.subheader("No reviews yet. Be the first to leave one!")

    st.markdown("---")

    # Display comments using st.expander
    for i, comment_data in enumerate(st.session_state.comments):
        with st.expander(f"**{comment_data['name']}** - {'⭐' * comment_data['rating']} ({comment_data['date']})"):
            st.write(comment_data['comment'])

    st.subheader("Leave Your Own Comment")
    # Wrap the form in an expander to keep the page cleaner
    with st.expander("Click here to leave a comment and rating"):
        with st.form("comment_form", clear_on_submit=True):
            user_name = st.text_input("Your Name")
            user_comment = st.text_area("Your Comment")
            user_rating = st.slider("Your Rating", 1, 5, 5)
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
                    save_comments(st.session_state.comments)
                    st.success("Thank you for your comment!")
                    st.experimental_rerun() # Rerun to show new comment
                else:
                    st.error("Please fill in your name and comment.")

elif selected_page == "📞 Contact Us":
    st.header("Contact Our Customer Service")
    st.write("Have questions about Ecopure, your order, or just want to say hello? We're here to help!")
    st.markdown("---")

    st.subheader("Send Us a Message")
    with st.form("contact_form", clear_on_submit=True):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email")
        contact_message = st.text_area("Your Message")
        contact_submitted = st.form_submit_button("Send Message")

        if contact_submitted:
            if contact_name and contact_email and contact_message:
                st.success(f"Thank you, {contact_name}! Your message has been sent.")
                # In a real app, you would send this email/message to a backend service
            else:
                st.error("Please fill in all fields.")

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