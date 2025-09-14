// This file contains functions to interact with the FastAPI backend endpoints.

const API_BASE_URL = 'http://localhost:8000'; // Adjust the base URL as needed

export const classifySpam = async (text) => {
    const response = await fetch(`${API_BASE_URL}/spam`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
    });
    return response.json();
};

export const detectSynthetic = async (imageFile) => {
    const formData = new FormData();
    formData.append('image', imageFile);

    const response = await fetch(`${API_BASE_URL}/synthetic`, {
        method: 'POST',
        body: formData,
    });
    return response.json();
};

export const checkProvenance = async (imageFile) => {
    const formData = new FormData();
    formData.append('image', imageFile);

    const response = await fetch(`${API_BASE_URL}/provenance`, {
        method: 'POST',
        body: formData,
    });
    return response.json();
};

export const classifyCategory = async (imageFile) => {
    const formData = new FormData();
    formData.append('image', imageFile);

    const response = await fetch(`${API_BASE_URL}/category`, {
        method: 'POST',
        body: formData,
    });
    return response.json();
};