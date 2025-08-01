#!/usr/bin/env python3
"""
Script to populate the PRC Exam Practice database with sample data.
This includes professions and realistic PRC exam questions.
"""

import sqlite3
import os

# Database file
DATABASE = 'prc_exam.db'

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def populate_professions():
    """Add PRC professions to the database"""
    professions = [
        {
            'name': 'Nursing',
            'description': 'Practice questions for the Nursing licensure examination covering fundamentals, medical-surgical, pediatrics, and more.'
        },
        {
            'name': 'Pharmacy',
            'description': 'Test your knowledge in pharmaceutical sciences, pharmacology, clinical pharmacy, and drug dispensing.'
        },
        {
            'name': 'Medicine',
            'description': 'Comprehensive review for medical licensure covering internal medicine, surgery, pediatrics, and clinical practice.'
        },
        {
            'name': 'Dentistry',
            'description': 'Dental licensure exam preparation including oral anatomy, periodontics, endodontics, and oral surgery.'
        },
        {
            'name': 'Physical Therapy',
            'description': 'Physical therapy practice questions covering anatomy, exercise physiology, rehabilitation, and treatment techniques.'
        }
    ]
    
    with get_db() as conn:
        for profession in professions:
            conn.execute('''
                INSERT OR REPLACE INTO professions (name, description)
                VALUES (?, ?)
            ''', (profession['name'], profession['description']))
        print(f"✅ Added {len(professions)} professions")

def populate_nursing_questions():
    """Add sample nursing questions"""
    questions = [
        {
            'question': 'A 65-year-old patient with diabetes mellitus is admitted with diabetic ketoacidosis (DKA). Which of the following is the priority nursing intervention?',
            'option_a': 'Administer insulin subcutaneously',
            'option_b': 'Establish IV access and begin fluid resuscitation',
            'option_c': 'Check blood glucose level',
            'option_d': 'Obtain arterial blood gas',
            'correct_answer': 'B',
            'explanation': 'In DKA, the priority is fluid resuscitation to correct dehydration and shock. IV access must be established first to administer fluids and medications effectively.'
        },
        {
            'question': 'A nurse is caring for a postoperative patient who received general anesthesia. Which assessment finding requires immediate intervention?',
            'option_a': 'Temperature of 97.8°F (36.6°C)',
            'option_b': 'Blood pressure of 110/70 mmHg',
            'option_c': 'Respiratory rate of 8 breaths per minute',
            'option_d': 'Pulse rate of 88 beats per minute',
            'correct_answer': 'C',
            'explanation': 'A respiratory rate of 8 breaths per minute indicates respiratory depression, which is a serious complication of general anesthesia that requires immediate intervention.'
        },
        {
            'question': 'When administering medications to a pediatric patient, the nurse should primarily base the dosage on the child\'s:',
            'option_a': 'Age',
            'option_b': 'Height',
            'option_c': 'Weight',
            'option_d': 'Body surface area',
            'correct_answer': 'C',
            'explanation': 'Pediatric medication dosages are primarily calculated based on the child\'s weight (mg/kg) to ensure safe and effective dosing.'
        },
        {
            'question': 'A patient with heart failure is prescribed furosemide (Lasix). Which electrolyte should the nurse monitor most closely?',
            'option_a': 'Sodium',
            'option_b': 'Potassium',
            'option_c': 'Calcium',
            'option_d': 'Magnesium',
            'correct_answer': 'B',
            'explanation': 'Furosemide is a loop diuretic that can cause significant potassium loss. Hypokalemia can lead to dangerous cardiac arrhythmias.'
        },
        {
            'question': 'According to Maslow\'s hierarchy of needs, which patient need should the nurse address first?',
            'option_a': 'A patient requesting pain medication',
            'option_b': 'A patient with difficulty breathing',
            'option_c': 'A patient feeling anxious about surgery',
            'option_d': 'A patient asking about discharge planning',
            'correct_answer': 'B',
            'explanation': 'Breathing (oxygenation) is a basic physiological need and takes priority over all other needs according to Maslow\'s hierarchy.'
        }
    ]
    
    return questions

def populate_pharmacy_questions():
    """Add sample pharmacy questions"""
    questions = [
        {
            'question': 'Which of the following is the generic name for Lipitor?',
            'option_a': 'Simvastatin',
            'option_b': 'Atorvastatin',
            'option_c': 'Lovastatin',
            'option_d': 'Pravastatin',
            'correct_answer': 'B',
            'explanation': 'Atorvastatin is the generic name for Lipitor, a commonly prescribed HMG-CoA reductase inhibitor used to lower cholesterol.'
        },
        {
            'question': 'A prescription reads "Take 1 tablet BID for 7 days." How many tablets should be dispensed?',
            'option_a': '7 tablets',
            'option_b': '14 tablets',
            'option_c': '21 tablets',
            'option_d': '28 tablets',
            'correct_answer': 'B',
            'explanation': 'BID means twice daily. For 7 days: 1 tablet × 2 times per day × 7 days = 14 tablets.'
        },
        {
            'question': 'Which class of drugs requires a black box warning for increased risk of suicidal thoughts in young adults?',
            'option_a': 'Antihypertensives',
            'option_b': 'Antibiotics',
            'option_c': 'Antidepressants',
            'option_d': 'Antihistamines',
            'correct_answer': 'C',
            'explanation': 'Antidepressants carry a black box warning for increased risk of suicidal thinking and behavior in children, adolescents, and young adults.'
        },
        {
            'question': 'What is the maximum daily dose of acetaminophen for adults?',
            'option_a': '2000 mg',
            'option_b': '3000 mg',
            'option_c': '4000 mg',
            'option_d': '5000 mg',
            'correct_answer': 'C',
            'explanation': 'The maximum recommended daily dose of acetaminophen for adults is 4000 mg (4 grams) to prevent hepatotoxicity.'
        },
        {
            'question': 'Which medication requires therapeutic drug monitoring due to its narrow therapeutic index?',
            'option_a': 'Amoxicillin',
            'option_b': 'Digoxin',
            'option_c': 'Ibuprofen',
            'option_d': 'Omeprazole',
            'correct_answer': 'B',
            'explanation': 'Digoxin has a narrow therapeutic index, meaning the difference between therapeutic and toxic levels is small, requiring regular monitoring.'
        }
    ]
    
    return questions

def populate_medicine_questions():
    """Add sample medicine questions"""
    questions = [
        {
            'question': 'A 45-year-old male presents with chest pain that worsens with inspiration and improves when leaning forward. The most likely diagnosis is:',
            'option_a': 'Myocardial infarction',
            'option_b': 'Pericarditis',
            'option_c': 'Pneumonia',
            'option_d': 'Pulmonary embolism',
            'correct_answer': 'B',
            'explanation': 'Pericarditis characteristically presents with chest pain that worsens with inspiration and improves when the patient leans forward (relief position).'
        },
        {
            'question': 'The first-line treatment for hypertension in a diabetic patient is:',
            'option_a': 'Beta-blockers',
            'option_b': 'Calcium channel blockers',
            'option_c': 'ACE inhibitors',
            'option_d': 'Diuretics',
            'correct_answer': 'C',
            'explanation': 'ACE inhibitors are first-line for diabetic patients with hypertension as they provide cardiovascular and renal protection.'
        },
        {
            'question': 'Which laboratory finding is most characteristic of iron deficiency anemia?',
            'option_a': 'Elevated MCV',
            'option_b': 'Decreased TIBC',
            'option_c': 'Elevated ferritin',
            'option_d': 'Decreased serum iron',
            'correct_answer': 'D',
            'explanation': 'Iron deficiency anemia is characterized by decreased serum iron, increased TIBC, and decreased ferritin levels.'
        }
    ]
    
    return questions

def populate_questions():
    """Add all sample questions to the database"""
    with get_db() as conn:
        # Get profession IDs
        professions = conn.execute('SELECT id, name FROM professions').fetchall()
        profession_map = {prof['name']: prof['id'] for prof in professions}
        
        question_count = 0
        
        # Add nursing questions
        if 'Nursing' in profession_map:
            nursing_questions = populate_nursing_questions()
            for q in nursing_questions:
                conn.execute('''
                    INSERT INTO questions 
                    (profession_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    profession_map['Nursing'],
                    q['question'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                    q['correct_answer'], q['explanation']
                ))
            question_count += len(nursing_questions)
        
        # Add pharmacy questions
        if 'Pharmacy' in profession_map:
            pharmacy_questions = populate_pharmacy_questions()
            for q in pharmacy_questions:
                conn.execute('''
                    INSERT INTO questions 
                    (profession_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    profession_map['Pharmacy'],
                    q['question'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                    q['correct_answer'], q['explanation']
                ))
            question_count += len(pharmacy_questions)
        
        # Add medicine questions
        if 'Medicine' in profession_map:
            medicine_questions = populate_medicine_questions()
            for q in medicine_questions:
                conn.execute('''
                    INSERT INTO questions 
                    (profession_id, question, option_a, option_b, option_c, option_d, correct_answer, explanation)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    profession_map['Medicine'],
                    q['question'], q['option_a'], q['option_b'], q['option_c'], q['option_d'],
                    q['correct_answer'], q['explanation']
                ))
            question_count += len(medicine_questions)
        
        print(f"✅ Added {question_count} questions")

def main():
    """Main function to populate the database"""
    print("🚀 Starting database population...")
    
    # Check if database exists
    if not os.path.exists(DATABASE):
        print("❌ Database not found. Please run the Flask app first to create the database.")
        return
    
    try:
        populate_professions()
        populate_questions()
        print("🎉 Database population completed successfully!")
        print("\n📊 Summary:")
        
        with get_db() as conn:
            prof_count = conn.execute('SELECT COUNT(*) as count FROM professions').fetchone()['count']
            q_count = conn.execute('SELECT COUNT(*) as count FROM questions').fetchone()['count']
            
            print(f"   • Professions: {prof_count}")
            print(f"   • Questions: {q_count}")
            
            # Show questions per profession
            results = conn.execute('''
                SELECT p.name, COUNT(q.id) as question_count
                FROM professions p
                LEFT JOIN questions q ON p.id = q.profession_id
                GROUP BY p.id, p.name
                ORDER BY p.name
            ''').fetchall()
            
            print("\n📚 Questions per profession:")
            for result in results:
                print(f"   • {result['name']}: {result['question_count']} questions")
        
    except Exception as e:
        print(f"❌ Error populating database: {e}")

if __name__ == '__main__':
    main()