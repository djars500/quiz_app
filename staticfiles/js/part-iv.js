(function () {
    //each droppable element needs this for its dragover event
    let allowDragover = function (event) {
            //prevent the browser from any default behavior
            event.preventDefault();
        },
        //each dragable element needs this for its dragstart event
        dragStartHandler = function (event) {
            let dragIcon = null;

            //set a reference to the element that is currenly being dragged
            event.originalEvent.dataTransfer.setData("id", event.target.id);
            //create a custom drag image
            dragIcon = document.createElement('img');

            //set the custom drag image
            event.originalEvent.dataTransfer.setDragImage(dragIcon, 100, 100);
        },


        //each of the four light-brown boxes at top have this bound to their drop event
        dropHandlerSingle = async function (event) {
            let id = '';

            //prevent the browser from any default behavior
            event.preventDefault();

            //only allow one child element at a time
            if ($(this).children().length) {
                return;
            }
            //get a reference to the element that is being dropped
            id = event.originalEvent.dataTransfer.getData("id");
            //add the hasChild class so that the UI can update
            $(event.target).addClass('hasChild');

            //trigger the custom event so that we can update the UI
            $(document).trigger('custom:dropEvent');

            //move the dragged element into the drop target
            event.target.appendChild(document.getElementById(id));

            let haschild = window.document.getElementsByClassName('drop-elements')
            let dropelements = window.document.getElementsByClassName('dropElement hasChild')


            if (haschild[0].children.length === dropelements.length) {

                const url = window.location.href
                let data = []
                let data_2 = {}
                const csrftoken = getCookie('csrftoken');
                data_2['csrfmiddlewaretoken'] = csrftoken;
                for (let i = 0; i < dropelements.length; i++) {
                    id = dropelements[i].getAttribute('value');
                    val_id = dropelements[i].children[0].getAttribute('id');
                    data_2[id] = val_id
                    data.push(
                        {
                            'id': dropelements[i].getAttribute('value'),
                            'value': dropelements[i].children[0].getAttribute('id')
                        }
                    )

                }

                data.push(
                    {"csrfmiddlewaretoken": csrftoken}
                )
                console.log(data, 'data')
                $.ajax({
                    type: 'POST',
                    url: `${url}save/`,
                    data: data_2,
                    success: function(response){
                        console.log(response, 'res')
                    },
                    error: function(error){
                        console.log(error, 'err')
                    }
                })
                // const response = await fetch(url, {
                //     method: 'POST',
                //     body: JSON.stringify(data),
                //     headers: {
                //         'Content-Type': 'application/json',
                //         "X-CSRFToken": csrftoken
                //     }
                // })
                // const json = await response.json();
                // console.log(JSON.stringify(json));

            }
        },
        //the box that holds the four blue dragable boxes on page load has this bound to its drop event
        dropHandlerMultiple = function (event) {
            event.preventDefault();

            let id = event.originalEvent.dataTransfer.getData("id");
            console.log(event, 'dropHandlerMultiple')
            if (event.target.id === "") {
                console.log('if', event.target.id)
                $(event.target).addClass('hasChild');

                event.target.appendChild(document.getElementById(id));

                $(document).trigger('custom:dropEvent');

            } else {
                console.log('else', event.target.id);
            }

        };

    $(document).ready(function () {
        //cache a reference to all four blue draggable boxes
        let $dragElements = $('.dragElement');

        //make each dragElement draggable
        $dragElements.attr('draggable', 'true');

        //bind the dragStartHandler function to all dragElements
        $dragElements.bind('dragstart', dragStartHandler);

        //bind the dropHandlerSingle function to all of the droppable elements (omit the original container)
        $('.droppable').not('.multipleChildren').bind('drop', dropHandlerSingle);

        //bind the dropHandlerMultiple function to the .droppable.multipleChildren element
        $('.droppable.multipleChildren').bind('drop', dropHandlerMultiple);

        //after something is dropped
        $(document).on('custom:dropEvent', function () {
            //make sure the DOM has been updated
            setTimeout(function () {
                //check each droppable element to see if it has a child
                $('.droppable').each(function () {
                    //if this element has no children
                    if (!$(this).children().length) {
                        //remove the hasChild class
                        $(this).removeClass('hasChild');
                    }
                });
            }, 50);
        });

        //bind the appropriate handlers for the dragover, dragenter and dragleave events
        $('.droppable').bind({
            dragover: allowDragover,
            dragenter: function () {
                //ignore this event for the original container of the drag elements
                if ($(this).hasClass('multipleChildren')) {
                    return;
                }

                $(this).addClass('dragEnter');
            },
            dragleave: function () {
                $(this).removeClass('dragEnter');
            }
        });
    })
})();

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

