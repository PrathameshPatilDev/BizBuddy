
import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

st.set_page_config(
    page_title="BizBuddy",
    page_icon="🛍️",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background-color: #0b1020;
        color: #f1f5f9;
    }

    [data-testid="stSidebar"] {
        background-color: #111827;
    }

    h1, h2, h3 {
        color: #e2e8f0;
    }

    [data-testid="stMetric"] {
        background-color: #151e32;
        padding: 18px;
        border-radius: 12px;
        border: 1px solid #26344f;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #111827;
        border-radius: 12px;
    }

    .stButton > button {
        background-color: #6366f1;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 18px;
    }

    .stButton > button:hover {
        background-color: #4f46e5;
        color: white;
        border: 1px solid #818cf8;
    }

    [data-testid="stChatMessage"] {
        border-radius: 12px;
    }

    hr {
        border-color: #26344f;
    }
</style>
""", unsafe_allow_html=True)



with st.sidebar:
    st.title("🛍️ BizBuddy")
    st.write("Small Business Assistant")
    st.divider()

    page = st.radio(
        "Navigation",
        ["Dashboard", "Products", "Sales", "AI Assistant"],
        index=0
    )

    st.divider()
    st.caption("BizBuddy Demo Project")

st.title("🛍️ BizBuddy")
st.write("Manage products and assist your customers with AI.")



products = [
    {
        "name": "Classic T-Shirt",
        "price": 499,
        "stock": 20,
        "category": "Clothing"
    },
    {
        "name": "Premium Cotton Shirt",
        "price": 799,
        "stock": 15,
        "category": "Clothing"
    },
    {
        "name": "Denim Jeans",
        "price": 1299,
        "stock": 12,
        "category": "Clothing"
    },
    {
        "name": "Casual Sneakers",
        "price": 1499,
        "stock": 8,
        "category": "Footwear"
    },
    {
        "name": "Sports Running Shoes",
        "price": 1999,
        "stock": 10,
        "category": "Footwear"
    },
    {
        "name": "Everyday Backpack",
        "price": 899,
        "stock": 10,
        "category": "Accessories"
    },
    {
        "name": "Leather Wallet",
        "price": 399,
        "stock": 25,
        "category": "Accessories"
    },
    {
        "name": "Classic Wrist Watch",
        "price": 1199,
        "stock": 7,
        "category": "Accessories"
    },
    {
        "name": "Wireless Earbuds",
        "price": 1799,
        "stock": 14,
        "category": "Electronics"
    },
    {
        "name": "Bluetooth Speaker",
        "price": 1299,
        "stock": 9,
        "category": "Electronics"
    },
    {
        "name": "Wireless Mouse",
        "price": 599,
        "stock": 18,
        "category": "Electronics"
    },
    {
        "name": "Mechanical Keyboard",
        "price": 2499,
        "stock": 6,
        "category": "Electronics"
    },
    {
        "name": "Stainless Steel Water Bottle",
        "price": 299,
        "stock": 30,
        "category": "Home & Lifestyle"
    },
    {
        "name": "Ceramic Coffee Mug",
        "price": 249,
        "stock": 22,
        "category": "Home & Lifestyle"
    },
    {
        "name": "Desk Lamp",
        "price": 699,
        "stock": 11,
        "category": "Home & Lifestyle"
    },
    
    {
        "name": "Smart Watch",
        "price": 2999,
        "stock": 0,
        "category": "Electronics"
    },
    {
        "name": "Premium Leather Jacket",
        "price": 3499,
        "stock": 0,
        "category": "Clothing"
    }

]


if "sales" not in st.session_state:
    st.session_state.sales = []


def ask_gemini(question, products):
    if client is None:
        return (
            "Gemini is not configured. "
            "Please check your local .env file."
        )

    product_details = ""

    for product in products:
        availability = (
            "In stock" if product["stock"] > 0
            else "Out of stock"
        )

        product_details += (
            f"Product: {product['name']}\n"
            f"Price: ₹{product['price']}\n"
            f"Stock quantity: {product['stock']}\n"
            f"Availability: {availability}\n"
            f"Category: {product['category']}\n\n"
        )

    prompt = f"""
You are BizBuddy, a friendly small-business assistant.

PRODUCT INFORMATION:
{product_details}

RULES:
1. Answer customers politely in simple language.
2. Use the product information above as the source of truth.
3. Never invent product names, prices, or stock quantities.
4. A product with stock zero is out of stock.
5. When asked for products under a budget, list matching
   products and clearly state their availability.
6. If asked about delivery, returns, refunds, or business
   contact details, do not invent the store's real policies.
   Explain that the customer should contact the business.
7. Never claim that a payment, order, or refund was completed.
8. If you do not know an answer, say so honestly.

CUSTOMER QUESTION:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )

        if response.text:
            return response.text

        return "I couldn't generate an answer. Please try again."

    except Exception as error:
        return (
            "Sorry, BizBuddy couldn't connect to its AI service. "
            f"Error type: {type(error).__name__}. "
            "Please check your connection and API configuration."
        )



if page == "Dashboard":
    st.subheader("📊 Business Dashboard")

    col1, col2, col3 = st.columns(3)

    available = sum(
        1 for product in products if product["stock"] > 0
    )

    with col1:
        st.metric("Total Products", len(products))

    with col2:
        st.metric("Products In Stock", available)

    with col3:
        st.metric("Out of Stock", len(products) - available)

    st.divider()
    st.subheader("Featured Products")

    for product in products:
        with st.container(border=True):
            st.write(f"**{product['name']}**")
            st.write(f"Price: ₹{product['price']}")

            if product["stock"] > 0:
                st.success(f"{product['stock']} units available")
            else:
                st.warning("Currently out of stock")


elif page == "Products":
    st.subheader("🛍️ Product Catalogue")

    search = st.text_input("Search products", placeholder="Enter a product name")

    filtered_products = [
        product for product in products
        if search.lower() in product["name"].lower()
    ]

    for product in filtered_products:
        with st.container(border=True):
            st.write(f"**{product['name']}**")
            st.write(f"Price: ₹{product['price']}")
            st.write(f"Category: {product['category']}")
            st.write(f"Stock: {product['stock']}")

            if product["stock"] > 0:
                st.success("Available")
            else:
                st.warning("Out of stock")

    if not filtered_products:
        st.info("No matching products found.")



elif page == "Sales":
    st.subheader("💰 Sales & Inventory Management")

    product_names = [product["name"] for product in products]

    st.markdown("### Update Stock")

    selected_stock_product = st.selectbox(
        "Select product to restock",
        product_names,
        key="restock_product"
    )

    stock_to_add = st.number_input(
        "Quantity to add",
        min_value=1,
        step=1,
        key="stock_quantity"
    )

    if st.button("Add Stock"):
        for product in products:
            if product["name"] == selected_stock_product:
                product["stock"] += stock_to_add
                st.success(
                    f"Added {stock_to_add} units to {product['name']}."
                )
                break

    st.divider()
    st.markdown("### Record a Sale")

    selected_sale_product = st.selectbox(
        "Select product sold",
        product_names,
        key="sale_product"
    )

    quantity_sold = st.number_input(
        "Quantity sold",
        min_value=1,
        step=1,
        key="sale_quantity"
    )

    if st.button("Record Sale"):
        for product in products:
            if product["name"] == selected_sale_product:
                if quantity_sold > product["stock"]:
                    st.error("Not enough stock available.")
                else:
                    product["stock"] -= quantity_sold

                    sale = {
                        "product": product["name"],
                        "quantity": quantity_sold,
                        "revenue": product["price"] * quantity_sold
                    }

                    st.session_state.sales.append(sale)

                    st.success(
                        f"Sale recorded! Revenue: ₹{sale['revenue']}"
                    )
                break

    st.divider()
    st.markdown("### Sales History")

    if st.session_state.sales:
        total_revenue = sum(
            sale["revenue"] for sale in st.session_state.sales
        )

        st.metric("Total Recorded Revenue", f"₹{total_revenue}")

        for sale in st.session_state.sales:
            st.write(
                f"{sale['product']} — "
                f"Quantity: {sale['quantity']} — "
                f"Revenue: ₹{sale['revenue']}"
            )
    else:
        st.info("No sales have been recorded yet.")


elif page == "AI Assistant":
    st.subheader("💬 BizBuddy AI Assistant")
    st.write("Ask questions about products and business support.")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input("Ask BizBuddy a question...")

    if question:
        st.session_state.chat_history.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("BizBuddy is thinking..."):
                answer = ask_gemini(question, products)
            st.write(answer)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

    if st.session_state.chat_history:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()


    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    question = st.chat_input(
        "Ask BizBuddy a question..."
    )

    if question:
        st.session_state.chat_history.append(
            {"role": "user", "content": question}
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            with st.spinner("BizBuddy is thinking..."):
                answer = ask_gemini(question, products)

            st.write(answer)

        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )

    if st.session_state.chat_history:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()
