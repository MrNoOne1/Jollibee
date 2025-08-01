// Quiz functionality for PRC Exam Practice App

class QuizApp {
    constructor(professionId) {
        this.professionId = professionId;
        this.currentQuestion = null;
        this.questionNumber = 1;
        this.isAnswered = false;
        
        this.initializeElements();
        this.bindEvents();
        this.loadFirstQuestion();
    }

    initializeElements() {
        // Get all DOM elements we'll need
        this.loadingContainer = document.getElementById('loading-container');
        this.questionContainer = document.getElementById('question-container');
        this.noQuestionsContainer = document.getElementById('no-questions-container');
        this.questionText = document.getElementById('question-text');
        this.questionNumberSpan = document.getElementById('question-number');
        this.optionButtons = document.querySelectorAll('.option-btn');
        this.feedbackContainer = document.getElementById('feedback-container');
        this.feedbackAlert = document.getElementById('feedback-alert');
        this.feedbackTitle = document.querySelector('.feedback-title');
        this.feedbackIcon = document.querySelector('.feedback-icon');
        this.correctAnswerSpan = document.getElementById('correct-answer');
        this.explanationP = document.getElementById('explanation');
        this.nextQuestionBtn = document.getElementById('next-question-btn');
        this.newQuestionBtn = document.getElementById('new-question-btn');
        this.currentScoreSpan = document.getElementById('current-score');
        this.totalQuestionsSpan = document.getElementById('total-questions');
        this.percentageSpan = document.getElementById('percentage');
    }

    bindEvents() {
        // Add click handlers to option buttons
        this.optionButtons.forEach(button => {
            button.addEventListener('click', (e) => this.handleAnswerClick(e));
        });

        // Add click handler to next question button
        this.nextQuestionBtn.addEventListener('click', () => this.loadNextQuestion());
        
        // Add click handler to new question button
        this.newQuestionBtn.addEventListener('click', () => this.loadNextQuestion());
    }

    async loadFirstQuestion() {
        try {
            await this.loadQuestion();
            await this.updateScore();
        } catch (error) {
            console.error('Error loading first question:', error);
            this.showError('Failed to load questions. Please try again.');
        }
    }

    async loadQuestion() {
        // Show loading state
        this.showLoading();

        try {
            const response = await fetch(`/api/question/${this.professionId}`);
            const data = await response.json();

            if (data.error) {
                this.showNoQuestions();
                return;
            }

            this.currentQuestion = data;
            this.displayQuestion();
        } catch (error) {
            console.error('Error loading question:', error);
            this.showError('Failed to load question. Please check your connection.');
        }
    }

    displayQuestion() {
        // Hide loading, show question
        this.loadingContainer.style.display = 'none';
        this.questionContainer.style.display = 'block';
        this.noQuestionsContainer.style.display = 'none';

        // Update question content
        this.questionText.textContent = this.currentQuestion.question;
        this.questionNumberSpan.textContent = this.questionNumber;

        // Update option buttons
        this.optionButtons.forEach(button => {
            const option = button.dataset.option;
            const optionText = button.querySelector('.option-text');
            optionText.textContent = this.currentQuestion.options[option];
            
            // Reset button state
            button.disabled = false;
            button.className = 'btn btn-outline-dark w-100 text-start option-btn';
        });

        // Hide feedback
        this.feedbackContainer.style.display = 'none';
        this.isAnswered = false;

        // Add fade-in animation
        this.questionContainer.classList.add('fade-in');
    }

    async handleAnswerClick(event) {
        if (this.isAnswered) return;

        const selectedButton = event.currentTarget;
        const selectedAnswer = selectedButton.dataset.option;

        // Mark as answered to prevent multiple clicks
        this.isAnswered = true;

        // Add selected state to clicked button
        selectedButton.classList.add('selected');

        try {
            // Send answer to server
            const response = await fetch('/api/check-answer', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    question_id: this.currentQuestion.id,
                    answer: selectedAnswer
                })
            });

            const result = await response.json();
            
            if (result.error) {
                throw new Error(result.error);
            }

            // Show feedback
            this.showFeedback(result, selectedAnswer);
            
            // Update score display
            this.updateScoreDisplay(result.score, result.total);

        } catch (error) {
            console.error('Error checking answer:', error);
            showToast('Failed to check answer. Please try again.', 'danger');
            this.isAnswered = false;
            selectedButton.classList.remove('selected');
        }
    }

    showFeedback(result, selectedAnswer) {
        const isCorrect = result.correct;
        
        // Update all option buttons to show correct/incorrect states
        this.optionButtons.forEach(button => {
            button.disabled = true;
            const option = button.dataset.option;
            
            if (option === result.correct_answer) {
                button.classList.add('correct');
            } else if (option === selectedAnswer && !isCorrect) {
                button.classList.add('incorrect');
            }
        });

        // Update feedback content
        if (isCorrect) {
            this.feedbackAlert.className = 'alert alert-success';
            this.feedbackIcon.className = 'fas fa-check-circle';
            this.feedbackTitle.textContent = 'Correct! Well done!';
            showToast('Correct answer! Keep it up!', 'success');
        } else {
            this.feedbackAlert.className = 'alert alert-danger';
            this.feedbackIcon.className = 'fas fa-times-circle';
            this.feedbackTitle.textContent = 'Incorrect. Learn from this!';
        }

        this.correctAnswerSpan.textContent = `Option ${result.correct_answer}`;
        this.explanationP.textContent = result.explanation || 'No explanation available.';

        // Show feedback container
        this.feedbackContainer.style.display = 'block';
        this.feedbackContainer.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    async loadNextQuestion() {
        this.questionNumber++;
        await this.loadQuestion();
    }

    async updateScore() {
        try {
            const response = await fetch('/api/score');
            const data = await response.json();
            this.updateScoreDisplay(data.score, data.total);
        } catch (error) {
            console.error('Error updating score:', error);
        }
    }

    updateScoreDisplay(score, total) {
        this.currentScoreSpan.textContent = score;
        this.totalQuestionsSpan.textContent = total;
        this.percentageSpan.textContent = formatPercentage(score, total);
    }

    showLoading() {
        this.loadingContainer.style.display = 'block';
        this.questionContainer.style.display = 'none';
        this.noQuestionsContainer.style.display = 'none';
    }

    showNoQuestions() {
        this.loadingContainer.style.display = 'none';
        this.questionContainer.style.display = 'none';
        this.noQuestionsContainer.style.display = 'block';
    }

    showError(message) {
        this.loadingContainer.style.display = 'none';
        this.questionContainer.style.display = 'none';
        showError(this.loadingContainer, message);
        this.loadingContainer.style.display = 'block';
    }
}

// Initialize quiz when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the quiz page
    if (typeof PROFESSION_ID !== 'undefined') {
        window.quiz = new QuizApp(PROFESSION_ID);
    }
});

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    if (typeof window.quiz === 'undefined') return;
    
    // Only handle shortcuts if we're not in an input field
    if (event.target.tagName === 'INPUT' || event.target.tagName === 'TEXTAREA') return;
    
    // Handle A, B, C, D keys for answer selection
    const key = event.key.toLowerCase();
    if (['a', 'b', 'c', 'd'].includes(key) && !window.quiz.isAnswered) {
        const optionButton = document.querySelector(`[data-option="${key.toUpperCase()}"]`);
        if (optionButton && !optionButton.disabled) {
            optionButton.click();
        }
    }
    
    // Handle Enter or Space for next question
    if ((event.key === 'Enter' || event.key === ' ') && window.quiz.isAnswered) {
        event.preventDefault();
        window.quiz.nextQuestionBtn.click();
    }
});

// Add some helpful tooltips
document.addEventListener('DOMContentLoaded', function() {
    // Add tooltip to explain keyboard shortcuts
    if (document.querySelector('.quiz-container')) {
        showToast('💡 Pro tip: Use A, B, C, D keys to select answers and Enter for next question!', 'info');
    }
});