import React, { useState } from 'react';
import axios from 'axios';

const CategoryForm = () => {
    const [image, setImage] = useState(null);
    const [category, setCategory] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [result, setResult] = useState(null);

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
            const response = await axios.post('/api/category', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            setResult(response.data);
        } catch (err) {
            setError('Error classifying the image. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Image Category Classifier</h2>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleImageChange} required />
                <button type="submit" disabled={loading}>
                    {loading ? 'Classifying...' : 'Classify Image'}
                </button>
            </form>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {result && (
                <div>
                    <h3>Classification Result:</h3>
                    <p>Category: {result.category}</p>
                    <p>Confidence: {result.confidence}</p>
                </div>
            )}
        </div>
    );
};

export default CategoryForm;