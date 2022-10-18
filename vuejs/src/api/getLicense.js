export const getLicense = async () => {
    const response = await fetch("http://localhost:8000/api/get_license/", {
        method: "GET",
    });
    const data = await response.json();
    return data;
}