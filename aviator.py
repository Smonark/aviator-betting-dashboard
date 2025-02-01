import time
import random
import matplotlib.pyplot as plt
import telegram
from telegram.ext import Updater, CommandHandler
import firebase_admin
from firebase_admin import credentials, db

# Telegram Bot Setup
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"
bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

# Firebase Setup
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred, {"databaseURL": "YOUR_FIREBASE_DATABASE_URL"})

# Risk Variables
total_bets = 0
total_wins = 0
total_losses = 0
profit = 0

# Risk Calculation Function
def analyze_risk():
    global total_bets, total_wins, total_losses, profit
    win_probability = total_wins / total_bets if total_bets > 0 else 0
    loss_probability = total_losses / total_bets if total_bets > 0 else 0
    risk_level = "LOW"

    if loss_probability > 0.5:
        risk_level = "HIGH"
        alert_message = f"⚠️ High Risk Alert! Loss Probability: {loss_probability * 100:.2f}%"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=alert_message)
    
    return win_probability, loss_probability, risk_level

# Simulating Betting Data
def simulate_betting():
    global total_bets, total_wins, total_losses, profit
    for _ in range(100):  # Simulating 100 rounds
        total_bets += 1
        outcome = random.choice(["win", "loss"])
        if outcome == "win":
            total_wins += 1
            profit += random.randint(10, 50)
        else:
            total_losses += 1
            profit -= random.randint(10, 50)
        
        # Live Risk Calculation
        win_rate, loss_rate, risk = analyze_risk()
        print(f"Round {total_bets}: Win Rate = {win_rate:.2f}, Loss Rate = {loss_rate:.2f}, Risk = {risk}")

        # Save to Firebase
        db.reference("betting_data").push({
            "round": total_bets,
            "win_rate": win_rate,
            "loss_rate": loss_rate,
            "risk": risk,
            "profit": profit
        })
        
        time.sleep(1)  # Simulating real-time delay

# Graph Visualization
def plot_performance():
    rounds = list(range(1, total_bets + 1))
    win_rates = [total_wins / i if i > 0 else 0 for i in rounds]
    loss_rates = [total_losses / i if i > 0 else 0 for i in rounds]

    plt.figure(figsize=(10, 5))
    plt.plot(rounds, win_rates, label="Win Rate", color="green")
    plt.plot(rounds, loss_rates, label="Loss Rate", color="red")
    plt.axhline(y=0.5, color='orange', linestyle='--', label="Risk Threshold")
    plt.xlabel("Rounds")
    plt.ylabel("Probability")
    plt.title("Live Betting Performance")
    plt.legend()
    plt.show()

# Start Simulation
simulate_betting()
plot_performance()
  
