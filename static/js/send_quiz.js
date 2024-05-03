const quizForm = document.getElementById("form-box");
const csrf = getCookie("csrftoken");
const elements = [...document.getElementsByClassName("answer")]
const data = {}
const url = window.location.href

function isEveryQuestionAnswered() {
    const questionInputs = document.querySelectorAll('[class^="form-check-input"]');
    const questionIds = new Set();

    // Собираем уникальные идентификаторы вопросов
    questionInputs.forEach(input => questionIds.add(input.getAttribute('name')));

    // Проверяем, есть ли ответ для каждого вопроса
    for (const id of questionIds) {
        const answers = document.querySelectorAll(`input[name="${id}"]:checked`);
        if (answers.length !== 1) {
            return false;
        }
    }
    return true;
}

function updateSubmitButton() {
    if (isEveryQuestionAnswered()) {
        submitButton.disabled = false;
    } else {
        submitButton.disabled = true;
    }
}

quizForm.addEventListener('change', updateSubmitButton);
const sendData = () => {
    data['csrfmiddlewaretoken'] = csrf
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value;
        } else {
            if (!data[el.name]) {
                data[el.name] = null;
            }
        }
    })
    console.log(url)
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            console.log(response, 'res')
            // window.location.href = window.location.host + response['path']
            window.location = response.path
        },
        error: function (error) {
            console.log(error, 'err')
        }
    })

}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    if (isEveryQuestionAnswered()) {
        sendData();
    } else {
        alert('Пожалуйста, выберите по одному ответу на каждый вопрос!');
    }
    updateSubmitButton();
    // sendData()
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}