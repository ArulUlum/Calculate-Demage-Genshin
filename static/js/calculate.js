document.addEventListener('DOMContentLoaded', () => {
    const skillSwitch = document.getElementById('skill-switch');
    const calculateForm = document.getElementById('calculate');

    skillSwitch.addEventListener('change', () => {
        // Kirim permintaan AJAX saat checkbox berubah
        const formData = new FormData(calculateForm);
        formData.append('skill_active', skillSwitch.checked ? 'on' : 'off'); // Tambahkan status checkbox

        fetch('/calculate', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(data => {
            // Perbarui hasil di halaman
            document.querySelector('.result').innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
    });
});
