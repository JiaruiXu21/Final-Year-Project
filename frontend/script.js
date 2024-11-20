document.getElementById('questionnaire-form').addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the default form submission

    // Collect form data
    const formData = new FormData(e.target);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    try {
        // Send data to the backend
        const response = await fetch('http://127.0.0.1:5001/recommend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        // Parse and display the response
        const result = await response.json();
        alert(`Recommended Watch: ${result.recommendation}`);
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
});
