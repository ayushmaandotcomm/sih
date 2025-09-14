import React, { useState } from 'react';
import axios from 'axios';

const SyntheticForm = () => {
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
            const response = await axios.post('/api/synthetic', formData, {
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
            <h2>Synthetic Image Detector</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" accept="image/*" onChange={handleImageChange} required />
                <button type="submit" disabled={loading}>
                    {loading ? 'Processing...' : 'Submit'}
                </button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {result && (
                <div>
                    <h3>Result:</h3>
                    <p>Type: {result.type}</p>
                    <p>Confidence: {result.confidence}</p>
                    <p>Notes: {result.notes}</p>
                </div>
            )}
        </div>
    );
};

export default SyntheticForm;