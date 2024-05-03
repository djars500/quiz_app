const quizForm = document.getElementById("form-box");
const csrf = getCookie("csrftoken");
const elements = [...document.getElementsByClassName("answer")]
const data = {}
const url = window.location.href
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
        success: function(response){
            console.log(response, 'res')
        },
        error: function(error){
            console.log(error, 'err')
        }
    })

}

quizForm.addEventListener('submit', e => {
    e.preventDefault()
    sendData()
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