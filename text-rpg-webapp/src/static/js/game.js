document.addEventListener('DOMContentLoaded', () => {
    const characterForm = document.getElementById('character-form');
    if (characterForm) {
        characterForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('char-name').value;
            const classType = document.getElementById('char-class').value;
            
            const response = await fetch('/api/create_character', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, class_type: classType })
            });
            
            if (response.ok) {
                window.location.href = '/game';
            }
        });
    }
});