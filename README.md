# ☕ IstoriiBot

## 📌 Description

This bot was created for the customers of the "Istorii" Coffee Shop. Customers can:

- View the menu
- Check events
- Explore vacancies
- Provide feedback or offer cooperation

📢 All job applications, feedback, and cooperation offers are automatically sent to dedicated Telegram chats where the management team can conveniently interact with them.

## 🐍 Stack  
- Python 3  
- Aiogram  
- Pydantic  
- JSON  

## 💾 Installation  
1. 📂 **Clone the repository:**  
```bash
 git clone https://github.com/suchkovdaniil/IstoriiBot.git
```
2. 📁 **Navigate to the 'IstoriiBot' folder and then to 'src':**  
```bash
 cd IstoriiBot/src
```
3. 🌟 **Create and activate a virtual environment:**  
```bash
 python3 -m venv venv
 source venv/bin/activate
```
4. 📦 **Install the requirements from requirements.txt:**  
```bash
 pip install -r requirements.txt
```
5. 📝 **Create a '.env' file, open it with your preferred editor, and write:**  
```
 BOT_TOKEN=your_bot_token
```
6. 📄 **Create an empty 'users_data.json' file in 'src':**  
```bash
 touch users_data.json
```
7. 🚀 **Run the bot with the command:**  
```bash
 python3 main.py
```

## 💡 Improvement plans  
1. 📊 Add a database instead of a JSON file.  
2. 🛒 Integrate with the Evotor sales register and add the ability to view discounts.

