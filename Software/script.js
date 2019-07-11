const baseURL = 'https://exceed.superposition.pknn.dev';

fetch(baseURL + '/data/jitrada')
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
    });

fetch(baseURL + '/data/jitrada/door')
    .then((res) => res.text())
    .then((data) => console.log(data))
    .catch((err) => console.log(err));


function postData() {
    retun (fetch(baseURL + '/data/jitrada', {
        method: 'POST',
        body: JSON.stringify({
            "data":{
                "door": 'open',
                "buzzer": 'off',
                "light": 'on',
            }
        }),
        headers: {
            'Content-Type' : 'application/json'
        }
    }).then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.log(err))
    )
}

function putData() {
    return (fetch(baseURL + '/data/jitrada/door', {
        method: 'PUT',
        body: JSON.stringify({
            "value": 'close'
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.log(err))
    )
}