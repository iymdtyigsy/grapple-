let batteryLevel = 50;
let oilLevel = 50;
let batteryIncreasing = true;

// Fake updates every second
setInterval(() => {
    // Battery bounce animation
    if (batteryIncreasing) {
        batteryLevel += 2;
        if (batteryLevel >= 100) batteryIncreasing = false;
    } else {
        batteryLevel -= 2;
        if (batteryLevel <= 0) batteryIncreasing = true;
    }

    // Oil level simulation
    if (oilLevel < 100) {
        oilLevel++;
    }

    // Update battery display
    const batteryFill = document.getElementById("battery");
    batteryFill.style.width = batteryLevel + "%";
    batteryFill.style.backgroundColor =
        batteryLevel < 30 ? "red" :
        batteryLevel < 60 ? "yellow" : "green";

    document.getElementById("battery-text").textContent = "Battery: " + batteryLevel + "%";

    // Battery alert
    if (batteryLevel < 20) {
        showAlert("⚠️ Battery critically low!");
    }

    // Update oil
    document.getElementById("oil-progress").value = oilLevel;
    document.getElementById("oil-text").textContent = "Oil: " + oilLevel + "%";

    if (oilLevel === 100) {
        showAlert("✅ Oil tank is full!");
        setTimeout(() => {
            oilLevel = 0; // reset after 3 sec
        }, 3000);
    }
}, 1000);

// Fake button handlers
function toggleTube(on) {
    showAlert(on ? "Test Tube Dipping Started" : "Test Tube Dipping Stopped");
}

function toggleOil(on) {
    showAlert(on ? "Oil Retrieval Started" : "Oil Retrieval Stopped");
}

function moveBoat(direction) {
    if (direction === "stop") {
        showAlert("⏹ Boat Stopped!");
    } else {
        showAlert("Boat moving " + direction.toUpperCase() + "!");
    }
}

// Show alert in right panel
function showAlert(message) {
    const alertBox = document.getElementById("alert-box");
    alertBox.textContent = message;
    alertBox.style.display = "block";
    setTimeout(() => {
        alertBox.style.display = "none";
    }, 2000);
}

// Leaflet map initialization
const map = L.map('map').setView([0, 0], 2);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(map);
L.marker([0, 0]).addTo(map).bindPopup("Boat Location");
