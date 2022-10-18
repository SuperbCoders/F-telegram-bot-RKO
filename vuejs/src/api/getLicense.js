export const getLicense = async () => {
    const response = await fetch("https://rko-bot.spaaace.io/api/get_license/", {
        method: "GET",
    });
    const data = await response.json();
    return data;
}