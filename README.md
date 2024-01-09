# Financial Portfolio Management System

## Overview

This project is a Financial Portfolio Management System built using FastAPI for the backend and Streamlit for the frontend. It provides users with the ability to manage and analyze their investment portfolios, supporting various financial instruments such as stocks, bonds, and cryptocurrencies.

### Features

- **User Authentication:** Secure user authentication using JSON Web Tokens (JWT).
- **Portfolio Management:** CRUD operations for managing portfolios and assets.
- **Real-time Market Data:** Integration with external APIs (e.g., Alpha Vantage) for fetching real-time market data.
- **Portfolio Analytics:** Calculation of various portfolio analytics metrics, including total value, asset allocation, and historical performance.
- **Responsive UI:** User-friendly and responsive dashboard implemented using Streamlit.

## Setup

### Prerequisites

- Python 3.7 or higher
- Pip package manager

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/financial-portfolio-management.git
    cd financial-portfolio-management
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On Linux/Mac:**

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the FastAPI backend:**

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI server at http://localhost:8000.

2. **Open a new terminal and start the Streamlit frontend:**

    ```bash
    streamlit run app.py
    ```

    This will launch the Streamlit app at http://localhost:8501.

3. **Access the Streamlit app in your web browser and interact with the Financial Portfolio Management System.**

## Usage

- **Login:** Enter your credentials to log in and access your portfolio.
- **Portfolio Management:** Add, update, or delete assets in your portfolio.
- **Analytics:** View portfolio analytics, historical performance, and market data.
- **Real-time Updates:** Experience real-time updates and push notifications for portfolio changes.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
