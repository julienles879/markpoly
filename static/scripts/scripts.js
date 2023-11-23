document.addEventListener('DOMContentLoaded', function () {
    var showAnswerButton = document.getElementById('show-answer-toggle');
    var answerElement = document.getElementById('answer');

    showAnswerButton.addEventListener('click', function () {
        if (answerElement.style.display === 'none' || answerElement.style.display === '') {
            answerElement.style.display = 'block';
            showAnswerButton.textContent = 'Masquer la réponse';
        } else {
            answerElement.style.display = 'none';
            showAnswerButton.textContent = 'Afficher la réponse';
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    var showRulesButton = document.getElementById('show-rules-toggle');
    var rulesElement = document.getElementById('rules');

    showRulesButton.addEventListener('click', function () {
        if (rulesElement.style.display === 'none' || rulesElement.style.display === '') {
            rulesElement.style.display = 'block';
            showRulesButton.textContent = 'Masquer les règles';
        } else {
            rulesElement.style.display = 'none';
            showRulesButton.textContent = 'Afficher les règles';
        }
    });
});