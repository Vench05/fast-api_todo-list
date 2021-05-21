

function deleteReq(data) {
    req = new XMLHttpRequest()
    req.open('DELETE', `http://127.0.0.1:8000/todo/remove/${data.getAttribute('data-id')}`)
    req.send()
    location.reload()
}


function doneReq(data) {   
    const task_id = data.getAttribute('data-id') 
    const task_done = data.getAttribute('data-done') == 'True'
    const task_name = data.getAttribute('data-value') 
    console.log(task_done);
    const body = {
        "name": task_name,
        "done": !task_done
    }
    req = new XMLHttpRequest()
    req.open('PUT', `http://127.0.0.1:8000/todo/update/${task_id}`, true)
    req.setRequestHeader('Content-type', 'application/json');
    req.send(JSON.stringify(body))
    location.reload()
}