var url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party";
var token = process.env.VUE_APP_TOKEN_DADATA;



export const getCompanyInn = async (inn) => {
    var query = inn;

    var options = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + token
        },
        body: JSON.stringify({query: query})
    }

    const response = await fetch(url, options);
    const data = await response.json();
    return data
    
}

export const getCompanyName = async (name) => {
    var query = name;

    var options = {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Token " + token
        },
        body: JSON.stringify({query: query})
    }

    const response = await fetch(url, options);
    const data = await response.json();
    return data
    
}
