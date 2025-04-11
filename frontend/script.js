function startMonitoring() {
  fetch('http://localhost:8000/monitor', { method: 'POST' })
    .then(res => res.json())
    .then(data => document.getElementById('output').innerText = data.status)
    .catch(err => console.error(err));
}

function sendAlert() {
  fetch('http://localhost:8000/alert?message=Emergency%20Alert', { method: 'POST' })
    .then(res => res.json())
    .then(data => document.getElementById('output').innerText = data.alert)
    .catch(err => console.error(err));
}

fetch("http://localhost:8000/reminders")
  .then(res => res.json())
  .then(data => {
    const reminderDiv = document.getElementById("reminders");
    reminderDiv.innerHTML = "<h3>Daily Reminders:</h3><ul>" +
      data.reminders.map(r => `<li>${r}</li>`).join('') + "</ul>";
  });

fetch("http://localhost:8000/safety-check")
  .then(res => res.json())
  .then(data => {
    const safetyDiv = document.getElementById("safety");
    safetyDiv.innerHTML = `<h3>Safety Status:</h3><p>${data.safety_status}</p>`;
  });
