const notificationIcon = document.getElementById("notificationIcon");
const notificationPopup = document.getElementById("notificationPopup");
const notificationMessage = document.getElementById("notificationMessage");
const closeIcon = document.getElementById("closeIcon");

let notificationCount = 0; // Initialize notification count
let notificationSeen = false; // Initialize notification seen state

notificationIcon.addEventListener("click", function () {
    toggleNotification();
    hideNotificationCount(); // Add this line to hide the notification count
});


closeIcon.addEventListener("click", function () {
    hideNotification();
});

function showNotification() {
    // Get the user's previous checkup date (replace with your logic)
    const previousCheckupDate = new Date("2023-07-11"); // Example previous checkup date

    // Calculate next due date as 1 month from previous checkup date
    const nextDueDate = new Date(previousCheckupDate);
    nextDueDate.setMonth(nextDueDate.getMonth() + 1);

    const currentDate = new Date();
    const twoDaysBefore = new Date(nextDueDate);
    twoDaysBefore.setDate(twoDaysBefore.getDate() - 2);

    if (twoDaysBefore.toDateString() === currentDate.toDateString()) {
        const formattedDueDate = formatDate(nextDueDate);
        notificationMessage.innerHTML = `Reminder: You have a checkup on ${formattedDueDate}!`;
        notificationPopup.style.display = "block";
        notificationCount++; // Increase the notification count
        updateNotificationCount(); // Update notification count on new notification
    } else {
        notificationPopup.style.display = "none"; // Hide the notification popup
        hideNotificationCount(); // Hide the notification count for subsequent viewings
    }
}

function hideNotification() {
    notificationPopup.style.display = "none"; // Hide the notification popup
    closeNotification(); // Also decrease the notification count when the popup is hidden
}

function toggleNotification() {
    if (!notificationSeen) {
        notificationSeen = true; // Mark notification as seen for the first time
        hideNotificationCount(); // Hide the notification count for the first viewing
    }
    showNotification();
}

function hideNotificationCount() {
    notificationIcon.innerHTML = `<i class="fas fa-bell"></i>`; // Remove the notification count
}

function closeNotification() {
    notificationCount--; // Decrease the notification count
    updateNotificationCount(); // Update notification count on close
}

function updateNotificationCount() {
    if (notificationCount > 0) {
        // Update the bell icon with the notification count
        notificationIcon.innerHTML = `<i class="fas fa-bell"></i> ${notificationCount}`;
    } else {
        // If no notifications, remove the notification count
        notificationIcon.innerHTML = `<i class="fas fa-bell"></i>`;
    }
}

function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// Call the showNotification function on page load
showNotification();
