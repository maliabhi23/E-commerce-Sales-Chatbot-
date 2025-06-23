# 🛍️ E-commerce Sales Chatbot

An AI-powered chatbot built with **Flask** and **Google Gemini (Generative AI)** that helps users interact with your e-commerce platform by answering queries like product recommendations or category-based searches.

---

## 🚀 Features

- 🤖 AI Chatbot using **Gemini API**
- 🧠 Understands natural language like "I need a laptop" or "Find me a book"
- 🔎 Suggests product search URLs
- 🌐 RESTful API with Flask backend
- 🧪 Tested using **Postman**
- 🔐 Securely manages API keys using `.env`

---

## 📁 Project Structure
```
E-commerce-Sales-Chatbot/
│
├── .env # Stores Gemini API key (not shared)
├── app.py # Main Flask app with chatbot route
├── chatbot.py # Gemini-based chatbot logic
├── requirements.txt # Dependencies
└── README.md # You're here!
```


---

## 🛠️ Setup Instructions

### 1. 🔃 Clone the repo

```bash
git clone https://github.com/yourusername/E-commerce-Sales-Chatbot.git
cd E-commerce-Sales-Chatbot
```

2.Install the dependencies
```
pip install -r requirements.txt
```
3.Add the .env file and add Gemini api key
```
GEMINI_API_KEY=your_google_generative_ai_key_here
```

4.Run the App
```
python app.py
```

5.Server Start at given url 
```
 http://localhost:5000
```

#💬 API Usage
1.Get Request
```
http://127.0.0.1:5000
```

#Responce
```
Welcome to the E-commerce Chatbot API
```

2. Search products

```
# http://127.0.0.1:5000/products?search=book
```
#Responce
```
[
{
"category": "book",
"description": "This is a description for book 1",
"id": 1,
"name": "Book Product 1",
"price": 510.0,
"stock": 99
},
```

3.Chat Post Request
```
 http://127.0.0.1:5000/chat

Body->raw->json paste below code
{
  "message": "Tell more about E-Commerce Sales them"
}


```

Responce
```
{
"response": "E-commerce sales encompass all sales activities conducted online. It's a vast field, and understanding it
requires breaking it down into several key aspects:\n\n**1. The Sales Process:** While the *channel* is different
(online vs. brick-and-mortar),
}

```


4.Get Request Session
Shows the Earlier chat history
```
http://127.0.0.1:5000/session
```

Responce
```
{
"bot": "I am an AI and cannot give medical advice. If you have a disease, you **must** see a doctor or other qualified
healthcare professional. They can properly diagnose your condition and recommend the appropriate treatment. Delaying
medical attention could be harmful.\n\nTo help a doctor
}
```

5.Reset history Post Request Delete all the earlier History
```
http://127.0.0.1:5000/reset
```

Responce
```
{
"status": "chat reset"
}
```















