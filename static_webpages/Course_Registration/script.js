// Auto-calculate total fee
let subjects = document.querySelectorAll(".subject");
let totalBox = document.getElementById("total");

subjects.forEach(item => {
    item.addEventListener("change", () => {
        let total = 0;

        subjects.forEach(sub => {
            if (sub.checked) {
                total += parseInt(sub.value);
            }
        });

        totalBox.innerText = "₹" + total;
    });
});

// Optional: form submit
document.getElementById("regForm").addEventListener("submit", function(e){
    e.preventDefault();

    let selectedSubjects = [];
    let totalFee = 0;

    subjects.forEach(sub => {
        if (sub.checked) {

            // Get subject name from the label text
            let subjectName = sub.parentElement.innerText.trim();
            selectedSubjects.push(subjectName);

            totalFee += parseInt(sub.value);
        }
    });

    if (selectedSubjects.length === 0) {
        showMessage("Please select at least one subject.", true);
        return;
    }

    let studentName = document.getElementById("name").value;

    let message =
        "Student Name: " + studentName + "\n\n" +
        "Selected Subjects:\n- " + selectedSubjects.join("\n- ") + "\n\n" +
        "Total Fee: ₹" + totalFee;

    showMessage(message, false);
});

// Function to display message in div container
function showMessage(message, isError) {
    const messageContainer = document.getElementById("messageContainer");
    const messageContent = document.getElementById("messageContent");
    
    messageContent.innerText = message;
    messageContainer.classList.remove("hidden");
    
    if (isError) {
        messageContainer.classList.add("error");
    } else {
        messageContainer.classList.remove("error");
    }
}

// Function to close the message
function closeMessage() {
    const messageContainer = document.getElementById("messageContainer");
    messageContainer.classList.add("hidden");
}
