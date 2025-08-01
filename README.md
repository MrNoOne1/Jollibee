# 🏥 PRC Exam Practice App

A simple and user-friendly web application to help Filipino PRC license takers practice for their professional exams. The app provides multiple-choice questions with explanations and tracks your progress.

## 🌟 Features

- **Multiple Professions**: Support for Nursing, Pharmacy, Medicine, Dentistry, and Physical Therapy
- **Interactive Quiz**: Click or use keyboard shortcuts (A, B, C, D) to answer questions
- **Real-time Feedback**: Instant answer checking with detailed explanations
- **Progress Tracking**: See your score and percentage as you practice
- **Mobile Friendly**: Works great on phones, tablets, and computers
- **Beautiful UI**: Clean, modern design using Bootstrap

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Flask (will be installed via requirements.txt)

### Installation

1. **Clone or download this project** to your computer

2. **Open terminal/command prompt** and navigate to the project folder:
   ```bash
   cd path/to/prc-exam-practice
   ```

3. **Install the required packages**:
   ```bash
   pip install Flask
   ```

4. **Run the app**:
   ```bash
   python app.py
   ```

5. **Open your web browser** and go to:
   ```
   http://localhost:5000
   ```

6. **Add sample questions** (first time only):
   - Open another terminal window
   - Run: `python populate_database.py`

That's it! Your PRC practice app is now running! 🎉

## 📱 How to Use

### Choosing a Profession
1. Visit the home page
2. Click on your profession (Nursing, Pharmacy, etc.)
3. You'll be taken to the quiz page

### Taking the Quiz
1. Read the question carefully
2. Click on your answer (A, B, C, or D)
3. You'll instantly see if you're correct with an explanation
4. Click "Next Question" to continue
5. Your score is tracked at the top

### Keyboard Shortcuts
- **A, B, C, D**: Select answer options
- **Enter**: Go to next question (after answering)

## 🏗️ Project Structure

```
prc-exam-practice/
├── app.py                  # Main Flask application
├── populate_database.py    # Script to add sample questions
├── requirements.txt        # Python dependencies
├── prc_exam.db            # SQLite database (created automatically)
├── templates/             # HTML templates
│   ├── base.html          # Base template
│   ├── home.html          # Home page
│   └── quiz.html          # Quiz page
└── static/               # CSS, JavaScript, images
    ├── css/style.css     # Custom styles
    └── js/
        ├── main.js       # General JavaScript
        └── quiz.js       # Quiz functionality
```

## 🔧 Technical Details

### Backend (Python/Flask)
- **Framework**: Flask (simple Python web framework)
- **Database**: SQLite (file-based, no setup required)
- **API Endpoints**: RESTful design for questions and scoring

### Frontend
- **Styling**: Bootstrap 5 (responsive design)
- **JavaScript**: Vanilla JS (no complex frameworks)
- **Icons**: Font Awesome
- **Responsive**: Works on all device sizes

### Database Tables
- **professions**: Stores available professions
- **questions**: Multiple-choice questions with explanations
- **user_sessions**: Tracks user progress and scores

## 📚 Adding More Questions

You can add more questions by:

1. **Editing the populate_database.py file**:
   - Add questions to the existing functions
   - Create new profession functions
   - Run the script again: `python populate_database.py`

2. **Using the database directly** (for advanced users):
   - Questions are stored in the `questions` table
   - Each question needs: profession_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation

### Question Format Example
```python
{
    'question': 'Your question text here?',
    'option_a': 'First option',
    'option_b': 'Second option',  
    'option_c': 'Third option',
    'option_d': 'Fourth option',
    'correct_answer': 'B',  # The correct option letter
    'explanation': 'Explanation of why this is correct...'
}
```

## 🎯 Future Enhancements

Ideas for improving the app:
- **User accounts**: Save progress across sessions
- **Question categories**: Organize by topics (e.g., Anatomy, Pharmacology)
- **Timed practice**: Simulate real exam conditions
- **Study modes**: Review wrong answers, bookmark questions
- **Statistics**: Detailed performance analytics
- **AI integration**: Generate new questions using AI
- **Offline mode**: Download questions for offline practice

## 🤝 Contributing

Want to help improve the app? Here are ways to contribute:

1. **Add more questions**: Create realistic PRC exam questions
2. **Improve design**: Enhance the user interface
3. **Fix bugs**: Report or fix any issues you find
4. **Add features**: Implement new functionality
5. **Translate**: Add support for Filipino/Tagalog

## ⚠️ Important Notes

- **Educational Use**: This app is for practice only, not official PRC material
- **Question Quality**: Sample questions are for demonstration - verify with official sources
- **Regular Updates**: Keep questions current with PRC exam patterns
- **Backup**: Regular backup of your database if you add many questions

## 🆘 Troubleshooting

### Common Issues

**App won't start:**
- Check if Python is installed: `python --version`
- Install Flask: `pip install Flask`
- Make sure you're in the right folder

**No questions showing:**
- Run the database population script: `python populate_database.py`
- Check if `prc_exam.db` file was created

**Database errors:**
- Delete `prc_exam.db` and restart the app to recreate it
- Check file permissions

**Port already in use:**
- Stop other applications using port 5000
- Or change the port in `app.py`: `app.run(debug=True, port=5001)`

## 📞 Support

If you need help:
1. Check this README first
2. Look for error messages in the terminal
3. Make sure all files are in the right place
4. Try restarting the app

## 📜 License

This project is for educational purposes. Feel free to use, modify, and share!

---

**Good luck with your PRC exam preparation! 🍀**

*Made with ❤️ for Filipino healthcare professionals*
