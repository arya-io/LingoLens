# LingoLens: Translator & Sentiment Analysis

🌐 **LingoLens** is a Streamlit-based web application that provides two powerful language tools:
1. **Language Translation**: Translate text between a wide range of languages using the `deep-translator` library.
2. **Sentiment Analysis**: Analyze the sentiment (positive, neutral, or negative) of a given text using `TextBlob`.

---

## 🔧 Features

- **Language Translation**:  
  Translate text in real-time into over 100+ languages with the help of `GoogleTranslator`.
  
- **Sentiment Analysis**:  
  Determine the sentiment polarity of a given text (positive, neutral, or negative).

- **User-Friendly Interface**:  
  Built with `Streamlit`, the app is clean, intuitive, and easy to use.

---

## 🛠️ Technologies Used

- **Python**
- **Streamlit**: For building the user interface.
- **TextBlob**: For sentiment analysis.
- **Deep-Translator**: For multi-language translation.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.7 or higher installed on your machine.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/arya-io/LingoLens.git
   cd LingoLens
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
3. Run the app:
   ```bash
   streamlit run app.py
4. Open the app in your browser at http://localhost:8501.

## 📁 File Structure
   ```bash
   LingoLens/
   │
   ├── app.py                  # Main Streamlit app file
   ├── language_options.py     # Language codes and their mappings
   ├── requirements.txt        # List of required libraries
   └── README.md               # Project documentation
   ```

## 📚 Supported Languages
- Includes over 100+ languages for translation. See the full list in `language_options.py`.

## 🎯 Future Enhancements
- Add more NLP features, such as text summarization.
- Enhance translation functionality with support for additional APIs.
- Integrate a database for logging translations and sentiment results.

## 🤝 Contributing
Contributions are welcome! If you'd like to contribute:

1. Fork this repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
3. Make your changes and commit:
   ```bash
   git commit -m "Add feature-name"
4. Push your branch:
   ```bash
   git push origin feature-name
5. Create a pull request.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgments
- Streamlit: For providing an easy-to-use framework for building web apps.
- TextBlob: For sentiment analysis tools.
- Deep-Translator: For multilingual translation capabilities.
