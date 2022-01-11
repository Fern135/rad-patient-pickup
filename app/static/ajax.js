import {
    util
} from "./util"; // utility functions

export class Ajax {

    constructor(url) {
        this.url = url;
        this.utility = new util();
    }

    setData(data = {}) {
        if (this.utility.isJson(data)) {
            this.data = data;
        } else {
            return (JSON.parse({ 'data': `${data} is not json format` })); // not in json format
        }
    }

    // setDomMod(mod_id_class) {
    //     this.mod_id_class = mod_id_class;
    // }

    setCSRftoken(token) { // Cross-Site Request Forgery
        this.token = token;
    }

    get() { // getting data from server
        try {
            fetch(this.url)
                .then(x => x.text())
                .then(y => { return y; }); // returns data
        } catch (err) {
            console.log(err.message);
        }
    }

    post() { // posting data to server
        try {
            fetch(this.url, {
                method: "POST",//<========== Adding method type
                mode: 'same-origin',  //<=== Do not send CSRF token to another domain.

                body: JSON.stringify( //<=== JSON format
                    this.data
                ),
                //<========================= Adding headers to the request
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    'X-CSRFToken': this.token // might not need
                }
            })

                // Converting to JSON
                .then(response => response.json())

                // Displaying results to console
                .then(json => console.log(json));

        } catch (err) {
            console.log(err.message);
        }
    }
}