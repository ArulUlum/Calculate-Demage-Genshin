document.addEventListener('DOMContentLoaded', () => {
    const skillSwitch = document.getElementById('skill-switch');
    const form = document.getElementById('calculate');
    const reactionRadios = document.querySelectorAll('.reaction-options input[type="radio"]');

    // Ensure radio buttons start disabled
    reactionRadios.forEach(radio => {
        radio.disabled = true;
    });

    // Function to send form data and update the result
    const sendFormData = async () => {
        const formData = new FormData(form);

        // Send form data via fetch to the /calculate route
        const response = await fetch('/calculate', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest' // Tells the backend it's an AJAX request
            }
        });

        if (response.ok) {
            const result = await response.text();
            // Replace the current HTML with the updated data
            document.querySelector('.result').innerHTML = result;
        } else {
            console.error('Failed to update the data.');
        }
    };

    // Handle enabling/disabling radio buttons based on skill switch
    skillSwitch.addEventListener('change', async () => {
        const isSkillActive = skillSwitch.checked;
        reactionRadios.forEach(radio => {
            radio.disabled = !isSkillActive;  // Disable if skill is not active
        });
        // If skill becomes inactive, reset to default (None)
        if (!isSkillActive) {
            document.getElementById('reaction-none').checked = true;
        }

        // Send form data when the skill switch is changed
        await sendFormData();
    });

    // Handle sending form data when radio button is clicked
    reactionRadios.forEach(radio => {
        radio.addEventListener('change', async () => {
            // Send form data when a radio button is selected
            await sendFormData();
        });
    });
});
