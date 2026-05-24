async function loadDashboard() {
    try {
        // This URL must match where your Python server is running (usually localhost:8000)
        const response = await fetch('http://localhost:8000/api/grammar/daily');
        
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }

        const data = await response.json(); // Convert response to JSON
        
        // Update the DOM
        document.getElementById('lesson-text').innerText = data.content;
    } catch (error) {
        console.error("Error fetching lesson:", error);
        document.getElementById('lesson-text').innerText = "Could not load lesson. Is the server running?";
    }
}

window.onload = loadDashboard;