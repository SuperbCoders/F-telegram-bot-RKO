export const getLicense = async () => {
    const response = await fetch(process.env.VUE_APP_HOST_API+"/api/get_license/", {
        method: "GET",
    });
    const data = await response.json();
    return data;
}