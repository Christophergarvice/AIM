AIM/
│
├── app/
│   ├── Flask_app.py             # Main Flask backend (port 5005)
│   ├── Process_Conversation.py  # AI/NLP text logic
│   ├── json_converter.py        # Handles daily log writing (JSON)
│   ├── summarize_daily_log.py   # Summarizes logs
│
├── static/
│   ├── Tampermonkey.js          # Browser connection script
│
├── logs/
│   ├── daily_log.json           # Stores daily logs
│
├── README.md                    # Setup instructions
└── requirements.txt             # Flask + dependencies
