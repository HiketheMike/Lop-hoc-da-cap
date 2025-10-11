import streamlit as st
from datetime import datetime
import json
import os

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
    initial_sidebar_state="expanded"
)

# --- Session State for Comments ---
if 'comments' not in st.session_state:
    st.session_state.comments = load_comments()

# --- Header Section (Always visible, above sidebar and main content) ---
st.image("pictures/big_icon.png", width=300)
st.title("🌿 Ecopure: Where Clean Meets Green") # Updated title to reflect combined theme
st.markdown("""
    *Your trusted partner for a sparkling clean and eco-conscious hydration experience.*
    """)

# --- Sidebar Content ---
st.sidebar.title("Navigation")
st.sidebar.markdown(
    """
    <style>
    [data-testid="stRadio"] {
        padding: 10px;
        background-color: #459cc3;
        border-radius: 5px;
        margin-bottom: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
selected_page = st.sidebar.radio(
    "Go to",
    ["About Us", "Products", "Customer Reviews", "Contact Us"], # Removed "Home", kept "About Us"
    index=0
)
st.sidebar.markdown("---")


st.sidebar.subheader("Quick Contact")
st.sidebar.markdown(
    """
    <div style="padding: 10px; background-color: #459cc3; border-radius: 5px; margin-bottom: 5px; color: white;">
        Email: info@ecopure.com<br>
        Phone: +1 (800) 555-0123
    </div>
    """,
    unsafe_allow_html=True
)


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
if selected_page == "About Us": # Combined "Home" and "About Us" content here
    st.header("Welcome to EcoPure: Where Clean Meets Green")
    st.write("""
        Discover the revolutionary way to keep your reusable water bottles impeccably clean and fresh,
        all while being kind to our planet. Ecopure offers a powerful, plant-based solution designed
        for the modern eco-conscious individual.
        """)

    # Content from original "Home" section
    with st.expander("Learn More About Our Mission"):
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
        st.image("https://via.placeholder.com/700x350?text=Ecopure+Product+Image", caption="Ecopure Water Bottle Cleaner: Clean, Green, Pristine.", use_container_width=True)

    with st.expander("Why Choose Ecopure?"):
        st.subheader("Why Choose Ecopure?")
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

    # Content from original "About Us" section
    st.markdown("---") # Separator for visual distinction
    st.subheader("Our Story and Vision")
    st.write("""
        At EcoPure, we are driven by a mission to foster a healthier planet and a healthier you.
        We believe in sustainable living, and that starts with the small choices we make every day,
        like reusing our water bottles. But reusing shouldn't mean compromising on hygiene.
        """)

    with st.expander("The Problem We're Solving"):
        st.subheader("The Problem We're Solving")
        st.markdown("""
            The growing concern over plastic waste in Vietnam highlights the urgent need for sustainable solutions.
            While reusable water bottles are a step in the right direction, they come with their own challenges:
            *   **Bacterial Growth:** Many reusable water bottles harbor high levels of bacteria, often far exceeding safe limits,
                leading to potential health risks and unpleasant odors.
            *   **Cleaning Difficulties:** Narrow-mouth designs and intricate crevices make thorough cleaning with manual brushes
                or hand washing nearly impossible, leaving behind residues and biofilms where microbes thrive.
            *   **Lack of Public Facilities:** The absence of specialized bottle cleaning equipment in public spaces like schools,
                offices, and gyms often leads users to skip or rush cleaning, accelerating bacterial growth.
            *   **User Habits:** A significant portion of users do not rinse their bottles daily, contributing to the hygiene problem.
            """)

    with st.expander("Our Solution: Innovation for a Cleaner Future"):
        st.subheader("Our Solution: Innovation for a Cleaner Future")
        st.markdown("""
            EcoPure offers an innovative and eco-friendly solution to these challenges:
            *   **Effective Cleaning:** Our bottle washers utilize water pressure for quick and effective cleaning,
                ensuring superior hygiene compared to traditional methods.
            *   **Promoting Reuse:** We empower users to confidently reuse their bottles multiple times a day,
                knowing they are hygienically clean, thereby supporting sustainable lifestyles and reducing disposable plastic waste.
            *   **Accessibility & Convenience:** Designed for both individual and shared spaces, EcoPure machines
                can be installed in homes, offices, gyms, and public areas, making bottle hygiene accessible to everyone.
            *   **Optional Upgrades:** For environments requiring the highest hygiene standards (e.g., schools, hospitals, cafes),
                we offer optional drying and sterilization functions.
            *   **Eco-Friendly Operation:** Our standard models operate without electricity, relying on water pressure or mechanical parts,
                which reduces equipment and electricity costs, aligning with our green mission.
            """)
        st.image("https://via.placeholder.com/700x350?text=EcoPure+Solution+Image", caption="EcoPure: Innovative Bottle Cleaning for a Sustainable Lifestyle", use_container_width=True)

    with st.expander("Our Goals"):
        st.subheader("Our Goals")
        st.markdown("""
            Our primary goals at EcoPure are:
            *   **Environmental Impact:** Significantly reduce plastic waste by promoting the widespread adoption of reusable bottles and providing effective cleaning solutions.
            *   **Public Health:** Improve public hygiene by ensuring reusable bottles are consistently clean and free from harmful bacteria.
            *   **Innovation:** Continuously develop and refine our bottle washing technology to offer the most efficient, convenient, and eco-friendly solutions on the market.
            *   **Community Engagement:** Partner with educational institutions and green organizations to raise awareness about sustainable practices and bottle hygiene.
            *   **Market Leadership:** Establish EcoPure as the leading provider of innovative bottle cleaning solutions in Vietnam and explore opportunities for international expansion.
            """)
        st.image("https://via.placeholder.com/700x350?text=EcoPure+Goals+Image", caption="Driving Sustainability and Hygiene", use_container_width=True)


elif selected_page == "Products":
    st.header("Our Products: EcoPure Bottle Washing Machines")
    st.write("Discover our range of innovative, eco-friendly bottle washing machines designed for various needs and environments.")

    # Product 1: Standard
    with st.container(border=True):
        st.subheader("EcoPure Standard")
        st.image("https://via.placeholder.com/400x400?text=EcoPure+Standard", caption="EcoPure Standard Model", width=250)
        st.metric(label="Price", value="$359.99 (8 million VND)")
        st.markdown("""
            **Function:** 1 tap, No drying function.
            **Description:** A single-tap bottle washer, compact and easy to use, without a drying function.
            **Target Customer:** Ideal for households, small offices, or businesses looking for a simple, cost-effective solution.
            """)
        if st.button("🛒 Add Standard to Cart"):
            st.success("EcoPure Standard added to cart!")

    st.markdown("---")

    # Product 2: Standard Air
    with st.container(border=True):
        st.subheader("EcoPure Standard Air")
        st.image("https://via.placeholder.com/400x400?text=EcoPure+Standard+Air", caption="EcoPure Standard Air Model", width=250)
        st.metric(label="Price", value="$489.99 (12 million VND)")
        st.markdown("""
            **Function:** 1 tap, Drying Function included.
            **Description:** A single-tap bottle washer with an added drying function, enabling quick drying after cleaning for faster, more hygienic use.
            **Target Customer:** Perfect for offices, school cafeterias, cafes, or consumers who need a multi-functional and efficient product.
            """)
        if st.button("🛒 Add Standard Air to Cart"):
            st.success("EcoPure Standard Air added to cart!")

    st.markdown("---")

    # Product 3: Double
    with st.container(border=True):
        st.subheader("EcoPure Double")
        st.image("https://via.placeholder.com/400x400?text=EcoPure+Double", caption="EcoPure Double Model", width=250)
        st.metric(label="Price", value="$439.99 (11 million VND)")
        st.markdown("""
            **Function:** 2 taps, No drying function.
            **Description:** A two-tap bottle washer, ideal for cleaning multiple bottles at once, designed for shared places.
            **Target Customer:** Suitable for larger organizations, universities, or businesses that need to clean multiple bottles simultaneously.
            """)
        if st.button("🛒 Add Double to Cart"):
            st.success("EcoPure Double added to cart!")

    st.markdown("---")

    # Product 4: Double Air
    with st.container(border=True):
        st.subheader("EcoPure Double Air")
        st.image("https://via.placeholder.com/400x400?text=EcoPure+Double+Air", caption="EcoPure Double Air Model", width=250)
        st.metric(label="Price", value="$589.99 (15 million VND)")
        st.markdown("""
            **Function:** 2 taps, Drying Function included.
            **Description:** A two-tap bottle washer with drying capability, perfect for high-traffic public spaces or businesses.
            **Target Customer:** Best for large enterprises, public areas like universities, offices, gyms, or cafes that require fast and efficient bottle cleaning for many people.
            """)
        if st.button("🛒 Add Double Air to Cart"):
            st.success("EcoPure Double Air added to cart!")


elif selected_page == "Customer Reviews":
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

    # Display comments in styled boxes
    for i, comment_data in enumerate(st.session_state.comments):
        st.markdown(
            f"""
            <div style="background-color: #e0f2f7; padding: 15px; border-radius: 8px; margin-bottom: 15px; border: 1px solid #459cc3;">
                <p style="font-weight: bold; color: #2c3e50; margin-bottom: 5px;">
                    {comment_data['name']} - {'⭐' * comment_data['rating']} ({comment_data['date']})
                </p>
                <p style="color: #34495e;">{comment_data['comment']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("Leave Your Own Comment")
    with st.container(border=True):
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
                    st.experimental_rerun()
                else:
                    st.error("Please fill in your name and comment.")


elif selected_page == "Contact Us":
    st.header("Contact Our Customer Service")
    st.write("Have questions about Ecopure, your order, or just want to say hello? We're here to help!")
    st.markdown("---")

    st.subheader("Send Us a Message")
    with st.form("contact_form", clear_on_submit=True):
        contact_name = st.text_input("Your Name")
        contact_email = st.text_input("Your Email")
        contact_subject = st.text_input("Subject")
        contact_message = st.text_area("Your Message")
        contact_submitted = st.form_submit_button("Send Message")

        if contact_submitted:
            if contact_name and contact_email and contact_subject and contact_message:
                st.success(f"Thank you, {contact_name}! Your message regarding '{contact_subject}' has been sent.")
            else:
                st.error("Please fill in all fields.")

    st.markdown("---")
    st.subheader("Other Ways to Reach Us")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            **Email:** info@ecopure.com  
            **Phone:** +1 (800) 555-0123  
            **Address:** 123 Green Street, Eco City, EC 12345
            """)
        st.subheader("Business Hours")
        st.markdown("""
            **Monday - Friday:** 9:00 AM - 5:00 PM EST  
            **Saturday:** 10:00 AM - 2:00 PM EST  
            **Sunday:** Closed
            """)

    with col2:
        st.subheader("Our Location")
        st.image("https://via.placeholder.com/300x200?text=Map+Location", caption="Our Office Location", use_column_width=True)
        st.markdown("[View on Google Maps](https://www.google.com/maps/search/123+Green+Street,+Eco+City,+EC+12345)")

    st.markdown("---")
    st.subheader("Frequently Asked Questions (FAQs)")
    with st.expander("What are Ecopure products made of?"):
        st.write("Ecopure products are made with 100% plant-based, biodegradable ingredients, ensuring an effective and eco-friendly clean.")
    with st.expander("Are Ecopure products safe for all water bottles?"):
        st.write("Yes, our formula is designed to be safe and effective for all types of reusable water bottles, including stainless steel, glass, and plastic.")
    with st.expander("How often should I clean my water bottle?"):
        st.write("For optimal hygiene, we recommend cleaning your water bottle daily, especially if you use it frequently or for beverages other than water.")
    with st.expander("Do you offer international shipping?"):
        st.write("Currently, we ship within the United States and Canada. We are working on expanding our international shipping options soon!")


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