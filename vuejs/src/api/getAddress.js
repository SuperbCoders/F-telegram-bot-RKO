var url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/address";
var token = process.env.TOKEN_DADATA;
console.log(process.env.ALLOWED_DOMAIN_NAME);
console.log(process.env);
export const getAddress = async (query="") => {

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
