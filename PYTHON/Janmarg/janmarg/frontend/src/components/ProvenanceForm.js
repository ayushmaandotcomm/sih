import React, { useState } from 'react';
import axios from 'axios';

const ProvenanceForm = () => {
    const [image, setImage] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleImageChange = (event) => {
        setImage(event.target.files[0]);
    };

    const handleSubmit = async (event) => {
        event.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        const formData = new FormData();
        formData.append('image', image);

        try {
            const response = await axios.post('/api/provenance', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(response.data);
        } catch (err) {
            setError('Error processing the image. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Image Provenance Checker</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" accept="image/*" onChange={handleImageChange} required />
                <button type="submit" disabled={loading}>
                    {loading ? 'Processing...' : 'Check Provenance'}
                </button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {result && (
                <div>
                    <h3>Results:</h3>
                    <pre>{JSON.stringify(result, null, 2)}</pre>
                </div>
            )}
        </div>
    );
};

export default ProvenanceForm;