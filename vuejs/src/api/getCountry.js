var url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/country";
var token = process.env.VUE_APP_TOKEN_DADATA;

export const getCountry = async (query="") => {

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

