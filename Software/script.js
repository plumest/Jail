const baseURL = 'https://exceed.superposition.pknn.dev';

// fetch(baseURL + '/data/jitrada')
//     .then((res) => res.json())
//     .then((data) => {
//         console.log(data);
//     });

// fetch(baseURL + '/data/jitrada/door')
//     .then((res) => res.text())
//     .then((data) => console.log(data))
//     .catch((err) => console.log(err));


function postData() {
    return (fetch(baseURL + '/data/jitrada', {
        method: 'POST',
        body: JSON.stringify({"data": {
            "door": 'open',
            "buzzer": 'open',
            "light": 'open',
        }}),
        headers: {
            'Content-Type' : 'application/json'
        }
    }).then((res) => res.json())
      .then((data) => console.log(data))
      .catch((err) => console.log(err))
    )
}
doorStatus = () => document.getElementById('customSwitch1').checked ? 'open': 'close';

function putData() {
    let statusDoor = '';
    let statusBuzzer = '';
    let statusLight = '';
    document.getElementById('customSwitch1').checked ? status = 'open': status = 'close'
    let data = {
        "door": statusDoor,
        "buzzer": statusBuzzer,
        "light": statusLight,
    }
    fetch(baseURL + '/data/jitrada/door', {
        method: 'PUT',
        body: JSON.stringify({data}),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then((res) => res.json())
    //   .then((data) => console.log(data))
    //   .catch((err) => console.log(err))
    
}

// "data":{
//     "door": 'open',
//     "buzzer": 'off',
//     "light": 'on',
// }


// doorStatus = () => console.log(document.getElementById('customSwitch1').checked)
