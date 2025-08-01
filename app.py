from flask import Flask, render_template, request, jsonify, session
import sqlite3
import random
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Database setup
DATABASE = 'prc_exam.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This makes it easier to work with results
    return conn

def init_db():
    """Initialize the database with tables"""
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS professions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT
            )
        ''')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                profession_id INTEGER,
                question TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                explanation TEXT,
                FOREIGN KEY (profession_id) REFERENCES professions (id)
            )
        ''')
        
        conn.execute('''
            CREATE TABLE IF NOT EXISTS user_sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                profession_id INTEGER,
                score INTEGER DEFAULT 0,
                total_questions INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()

# Initialize database when app starts
with app.app_context():
    init_db()

@app.route('/')
def home():
    """Home page - profession selection"""
    with get_db() as conn:
        professions = conn.execute('SELECT * FROM professions').fetchall()
    return render_template('home.html', professions=professions)

@app.route('/quiz/<int:profession_id>')
def quiz(profession_id):
    """Quiz page for selected profession"""
    # Initialize session if needed
    if 'session_id' not in session:
        session['session_id'] = os.urandom(16).hex()
        session['score'] = 0
        session['total_questions'] = 0
    
    # Get profession name
    with get_db() as conn:
        profession = conn.execute('SELECT name FROM professions WHERE id = ?', (profession_id,)).fetchone()
        if not profession:
            return "Profession not found", 404
    
    return render_template('quiz.html', profession=profession['name'], profession_id=profession_id)

@app.route('/api/question/<int:profession_id>')
def get_question(profession_id):
    """API endpoint to get a random question for the profession"""
    with get_db() as conn:
        questions = conn.execute('''
            SELECT * FROM questions WHERE profession_id = ?
        ''', (profession_id,)).fetchall()
        
        if not questions:
            return jsonify({'error': 'No questions available for this profession'})
        
        # Pick a random question
        question = random.choice(questions)
        
        return jsonify({
            'id': question['id'],
            'question': question['question'],
            'options': {
                'A': question['option_a'],
                'B': question['option_b'],
                'C': question['option_c'],
                'D': question['option_d']
            }
        })

@app.route('/api/check-answer', methods=['POST'])
def check_answer():
    """API endpoint to check if the answer is correct"""
    data = request.get_json()
    question_id = data.get('question_id')
    user_answer = data.get('answer')
    
    with get_db() as conn:
        question = conn.execute('''
            SELECT correct_answer, explanation FROM questions WHERE id = ?
        ''', (question_id,)).fetchone()
        
        if not question:
            return jsonify({'error': 'Question not found'})
        
        is_correct = user_answer.upper() == question['correct_answer'].upper()
        
        # Update session score
        if 'score' not in session:
            session['score'] = 0
            session['total_questions'] = 0
        
        if is_correct:
            session['score'] += 1
        session['total_questions'] += 1
        
        return jsonify({
            'correct': is_correct,
            'correct_answer': question['correct_answer'],
            'explanation': question['explanation'],
            'score': session['score'],
            'total': session['total_questions']
        })

@app.route('/api/score')
def get_score():
    """Get current session score"""
    return jsonify({
        'score': session.get('score', 0),
        'total': session.get('total_questions', 0)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)