# 💬 🚀 Async Python Chat Server

## 📖 Project Overview
This is a **fun and lightweight asynchronous chat server** built in Python using `asyncio`.
Multiple clients can connect, chat **in real-time**, and send **direct messages** to each other using unique IDs.
💡 **Every client gets a unique ID**, so you always know who's online!

---

## ✨ Features
- 🏎 **Asynchronous** handling of multiple clients  
- 🆔 **Unique ID** for each client using timestamp + UUID  
- 👥 Track **online users** in the chat room  
- ✉️ Direct messaging using `target_id:message` format  
- 🔒 Thread-safe with `asyncio.Lock`  
- 🛑 Graceful handling of client disconnections  

---

## 🛠 Requirements
- Python 3.10+  
- `aioconsole` (for interactive client input)

Install dependencies:

```bash
pip install aioconsole
```

---

## ⚡ Installation
1. Clone the repository:  
```bash
git clone https://github.com/yourusername/async-chat-server.git
cd async-chat-server
```

2. (Optional) Create & activate a virtual environment:  
```bash
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
```

3. Install dependencies:  
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### Start the Server
```bash
python server.py
```
🌐 Listening on all interfaces (`0.0.0.0`) port `8080`.

### Start the Client
```bash
python client.py
```
Once connected, the client will receive a **unique ID** and can start sending messages.

---

## ✉️ Messaging Format
To send a message to a specific client, use the following format:
```
target_id:message
```
Example:
```
1234567890:Hello there!
```

---

## 🛠 How It Works
1. **Server**  
   - Assigns a unique client ID when a new client connects.  
   - Keeps track of online clients.  
   - Handles message delivery between clients asynchronously.  
   - Cleans up disconnected clients automatically.

2. **Client**  
   - Connects to the server.  
   - Reads messages asynchronously from the server.  
   - Sends messages asynchronously to other clients.

---

## 📄 License
This project is licensed under the MIT License. See `LICENSE` for details.

---

## 👤 Author
**Silencer**

