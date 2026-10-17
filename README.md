# BizBuddy — AI-Powered Small Business Assistant

BizBuddy is a Python-based small business assistant that helps businesses manage product information, monitor inventory, record sales, and answer customer questions using Google's Gemini AI.

## Features

- **Business Dashboard:** View product counts and stock availability.
- **Product Catalogue:** Browse and search products across multiple categories.
- **Inventory Management:** Add stock and track product availability.
- **Sales Management:** Record sales and calculate revenue.
- **AI Customer Assistant:** Ask questions about products, prices, stock, and availability.
- **Interactive Interface:** Built with Streamlit for a simple, user-friendly experience.

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- `google-genai`
- `python-dotenv`

## Setup and Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies.
4. Create a `.env` file in the project root.
5. Add your Gemini API key to `.env`.
6. Run the application.

Example `.env` entry:

`GEMINI_API_KEY=your_gemini_api_key_here`

Install the packages used by the application:

`pip install streamlit google-genai python-dotenv`

Start BizBuddy:

`streamlit run app.py`

## Demo Products

The application includes sample products from clothing, footwear, accessories, electronics, and home and lifestyle categories, including products that are out of stock.

## Future Improvements

- Persistent database storage for products and sales
- Sales analytics and charts
- Product management through a database
- Customer FAQ management
- Deployment to a public web URL

## Security

Never commit API keys, `.env` files, or other secrets to GitHub.

## Disclaimer

BizBuddy is an educational portfolio project using sample business data. It does not process real payments or complete real customer orders.