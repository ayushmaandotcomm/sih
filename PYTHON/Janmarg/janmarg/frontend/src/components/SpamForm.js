import React, { useState } from 'react';
import axios from 'axios';

const SpamForm = () => {
    const [textInput, setTextInput] = useState('');
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await axios.post('/api/spam', { text: textInput });
            setResult(response.data);
        } catch (err) {
            setError('Error classifying text. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <h2>Spam Classifier</h2>
            <form onSubmit={handleSubmit}>
                <textarea
                    value={textInput}
                    onChange={(e) => setTextInput(e.target.value)}
                    placeholder="Enter text to classify"
                    required
                />
                <button type="submit" disabled={loading}>
                    {loading ? 'Classifying...' : 'Classify'}
                </button>
            </form>
            {result && (
                <div>
                    <h3>Result:</h3>
                    <p>{result.is_spam ? 'Spam' : 'Not Spam'}</p>
                    <p>Confidence: {result.confidence}</p>
                </div>
            )}
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
};

export default SpamForm;