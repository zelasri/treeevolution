// check current user uuid
async function checkUser() {

    // check if localstorage already contains user uuid
    prepared_data = {}

    if (localStorage.getItem('treevolution_uuid') !== null) {
        prepared_data['treevolution_uuid'] = localStorage.getItem('treevolution_uuid')
    }

    let response = await fetch('/check', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(prepared_data)
    });

    if (response.ok) { 

        // get the response body (the method explained below)
        let json = await response.json();

        if (localStorage.getItem('treevolution_uuid') === null) {
            localStorage.setItem('treevolution_uuid', json.uuid);
        }
    } 
    else {
        console.log("HTTP-Error: " + response.status);
    }
}

checkUser();