📘 AI Language Translator – CodeAlpha Internship

This project is an AI-based Language Translator built using Python, Django, JavaScript, and LibreTranslate API.
It was developed as part of the CodeAlpha Artificial Intelligence Internship.

The translator allows users to input any text and instantly convert it into another language with a clean and modern UI.

🌟 Features

✔ Translate text between multiple languages
✔ Clean, simple user interface
✔ Uses LibreTranslate API for accurate translations
✔ Responsive and fast
✔ Easy to extend with more languages
✔ Fully functional Django web app

📂 Project Structure
AI Language Translator/
│
├── AI/                            
│   ├── Templates/
│   │   └── index.html      # Translator UI
│   ├── views.py            # Translation logic (API call)
│   ├── urls.py             # App routing
│   └── apps.py             
│
├── Intelligence/                  
│   ├── settings.py
│   ├── urls.py              # Main project routes
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── index.css       # UI styling
│   └── js/
│       └── translate.js    # Fetch API for translation
│
├── manage.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
✔ 1. Clone the repository
git clone https://github.com/Antro845/CodeAlpha_TRANSLATOR.git
cd CodeAlpha_TRANSLATOR

✔ 2. Create a virtual environment
python -m venv venv

✔ 3. Activate venv

Windows:

venv\Scripts\activate

✔ 4. Install project dependencies
pip install -r requirements.txt

✔ 5. Run Django development server
python manage.py runserver


Your translator will be available at:

👉 http://127.0.0.1:8000/

🚀 How to Use the Language Translator

1. Open the translator in your browser

2. Type or paste your text in the input box

3. Select the target language

4. Click Translate

5. The translated text appears instantly

🧠 Technology Stack

1. Python (Django Framework)

2. JavaScript (Fetch API)

3. HTML5 / CSS3

4. LibreTranslate API

5. JSON

📝 API Used

🔗 LibreTranslate API
A free and open-source translation engine used to handle language conversion.

📦 Requirements

The required packages are listed in:

--> requirements.txt


Install all packages with:
pip install -r requirements.txt

🏅 About CodeAlpha Internship

This project was completed as part of the:

📌 CodeAlpha Artificial Intelligence Internship Program

It demonstrates practical skills in:

1. API Integration

2. Web Development

3. Frontend & Backend Coordination

4. Natural Language Processing

5. UI/UX Design

📬 Contact

Developer: M. ANTRO PRATHIK SAM 
GitHub: https://github.com/Antro845

⭐ If you found this project useful, please star the repository!
