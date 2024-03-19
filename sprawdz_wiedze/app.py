from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista pytań w formie słownika, gdzie klucz to pytanie, a wartość to lista odpowiedzi.
questions = {
    "Kto napisał 'W pustyni i w puszczy'?": ["A. Juliusz Słowacki", "B. Henryk Sienkiewicz", "C. Adam Mickiewicz", "D. Bolesław Prus"],
    "Kiedy wynaleziono koło?": ["A. W średniowieczu", "B. W starożytności", "C. W renesansie", "D. W Baroku "],
    "Jaka jest liczba ludności Polski?": ["A. 50 tys.", "B. 38 tys.", "C. 38 mln", "42 mln"],
    "Z czego powstają rodzynki?":["A. Z winogron", "B. Z rodzynkowca", "C. Z figowca"],
    "50% z 50 to:":["A. 1", "B. 5", "C. 15", "D. 25"]
}

# Lista zawierająca poprawne odpowiedzi do każdego pytania.
correct_answers = {
    "Kto napisał 'W pustyni i w puszczy'?": "B. Henryk Sienkiewicz",
    "Kiedy wynaleziono koło?": "B. W starożytności",
    "Jaka jest liczba ludności Polski?":"C. 38 mln",
    "Z czego powstają rodzynki?":"A. Z winogron",
    "50% z 50 to:":"D. 25"
}

# Inicjalizacja listy wyników.
results = {}


@app.route('/')
def index():
    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    score = 0 #liczba poprawnych odpowiedzi. Na początku na 0
    question_results = {} #szczegóły odpowiedzi 
    
    for question, options in questions.items():
        selected_option = request.form.get(question)
        is_correct = selected_option == correct_answers[question]
        
        question_results[question] = {
            'selected_option': selected_option,
            'is_correct': is_correct
        }

        if is_correct:
            score += 1
    
    results.clear()
    results['score'] = score
    results['total'] = len(questions) 
    results['question_results'] = question_results
    
    return redirect(url_for('show_results')) #przekierowanie do strony wynikow

# dekolaracja endpointu /results, Przekazanie danych do dynamicznie generowanego results.html
@app.route('/results')
def show_results():
    return render_template('results.html', results=results, questions=questions, correct_answers=correct_answers)

#przekierowanie do strony głównej quizu
@app.route('/retry')
def retry_quiz():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
