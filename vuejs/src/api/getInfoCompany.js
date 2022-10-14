var url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party";
var token = "24b001b01c74fdf306826d52ff2a996b8f96226b";



export const getCompany = async (inn) => {
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
