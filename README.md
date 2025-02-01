# aviator-betting-dashboard
- **Live Risk Analysis**: Calculates win/loss probabilities and alerts on high-risk scenarios. - **Telegram Notifications**: Sends alerts when risk thresholds are exceeded. - **Graph Visualization**: Displays live betting performance over time. - **Cloud Storage**: Data is saved to Firebase for analysis.  
# Aviator Betting Dashboard with Live Risk Alerts

This project simulates betting in the **Aviator Game** with **live risk analysis**, **profit tracking**, and **Telegram bot notifications**. 

## Features:
- **Live Risk Analysis**: Calculates win/loss probabilities and alerts on high-risk scenarios.
- **Telegram Notifications**: Sends alerts when risk thresholds are exceeded.
- **Graph Visualization**: Displays live betting performance over time.
- **Cloud Storage**: Data is saved to Firebase for analysis.

## Prerequisites:
- Python 3.x
- Google Chrome & ChromeDriver
- Telegram Bot Token

## Installation:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/aviator-betting-dashboard.git
    cd aviator-betting-dashboard
    ```

2. **Install Dependencies**:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Setup Telegram Bot**:
    - Go to **BotFather** on Telegram and create a new bot. Get your **Bot Token** and **Chat ID**.
    - Replace `YOUR_BOT_TOKEN` and `YOUR_CHAT_ID` in the `aviator.py` script.

4. **Firebase Setup**:
    - Create a Firebase project and configure the Realtime Database.
    - Download the `firebase_config.json` file and place it in the project directory.
    - Replace `YOUR_FIREBASE_DATABASE_URL` in the `aviator.py` script with your Firebase database URL.

5. install requirements.txt
# CREATE PYTHON ENVIRONMENT
   python3 -m venv venv
# load the environment
   source venv/bin/activate
   
 # Run 
   pip install -r requirements.txt

5. **Run the Script**:
    ```bash
    python3 aviator.py
    ```

6. **Optional**: For better visualization, you can view the graph showing **win/loss rates** over time.

## License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
