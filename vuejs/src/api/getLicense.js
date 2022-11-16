export const getLicense = async () => {
    const response = await fetch("/api/get_license/", {
        method: "GET",
    });
    const data = await response.json();
    return data;
}