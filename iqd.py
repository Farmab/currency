import streamlit as st
import requests

# Function to fetch exchange rate from a global API
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # Global exchange rate API
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "IQD" in data["rates"]:
            return data["rates"]["IQD"]
        else:
            st.error("نرخی IQD له وەڵامەوە نەدۆزرایەوە.")
            return None
    except Exception as e:
        st.error(f"هەڵەیەک روویدا لە کێشانی نرخەکان: {e}")
        return None

# Streamlit app
st.set_page_config(page_title="گۆڕینی دراوە", page_icon="💱", layout="centered")

# Add custom CSS for background color
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #1e3c72, #2a5298);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💱 گۆڕینی دراوە: USD ↔ IQD")
st.markdown("ئەم بەرنامەیە بەکاربەرە بۆ بە ئاسانترین شێوە گۆڕینی نێوان **USD** و **IQD** بە پەیوەندی بە نرخە نوێیەکان.")

# Fetch the exchange rate
usd_to_iqd_rate = get_exchange_rate()

if usd_to_iqd_rate:
    st.markdown(f"### 📈 نرخەکانی نوێ: **1 USD = {usd_to_iqd_rate} IQD**")

    # Add some spacing
    st.markdown("---")

    # Input fields for conversion with improved layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("گۆڕینی USD بۆ IQD")
        usd_amount = st.number_input("بڕی USD بنووسە:", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        if st.button("گۆڕینی بۆ IQD"):
            iqd_result = usd_amount * usd_to_iqd_rate
            st.success(f"{usd_amount:.2f} USD = {iqd_result:.2f} IQD")

    with col2:
        st.subheader("گۆڕینی IQD بۆ USD")
        iqd_amount = st.number_input("بڕی IQD بنووسە:", min_value=0.0, value=0.0, step=1.0, format="%.2f")
        if st.button("گۆڕینی بۆ USD"):
            usd_result = iqd_amount / usd_to_iqd_rate
            st.success(f"{iqd_amount:.2f} IQD = {usd_result:.2f} USD")

    # Footer section
    st.markdown("---")
    st.markdown(
        "**پێشنیار:** نرخەکان بە شێوەی خۆکار نوێ دەکرێنەوە بە پەیوەندی بە داتای نوێیەکان لە API-یەکی بە بڕوا. بۆ گۆڕینی ڕاستەقینە، دڵنیابە لەوەی بڕەکانت ڕاستن.")

else:
    st.error("نەتوانرا نرخەکان بەدەستهێنن. تکایە دووبارە هەوڵ بدە.")
