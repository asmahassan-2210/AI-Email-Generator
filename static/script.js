// ==========================================
// AI EMAIL GENERATOR - script.js
// ==========================================


// Get HTML elements
const form = document.getElementById("emailForm");

const generateButton =
    document.getElementById("generateButton");

const buttonText =
    document.getElementById("buttonText");

const emptyState =
    document.getElementById("emptyState");

const resultContainer =
    document.getElementById("resultContainer");

const generatedEmail =
    document.getElementById("generatedEmail");

const copyButton =
    document.getElementById("copyButton");


// ==========================================
// GENERATE EMAIL
// ==========================================

form.addEventListener("submit", async function (event) {

    // Prevent page refresh
    event.preventDefault();


    // Get input values
    const recipient =
        document.getElementById("recipient").value.trim();

    const purpose =
        document.getElementById("purpose").value.trim();

    const tone =
        document.getElementById("tone").value;


    // Check required fields
    if (recipient === "" || purpose === "") {

        alert("Please fill in all the required fields.");

        return;
    }


    // Disable button while generating
    generateButton.disabled = true;

    buttonText.innerHTML = `
        <span class="loading">
            <span class="spinner"></span>
            Generating Email...
        </span>
    `;


    try {

        // Send data to FastAPI
        const response = await fetch("/generate", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                recipient: recipient,

                purpose: purpose,

                tone: tone

            })

        });


        // Convert response to JSON
        const data = await response.json();


        // ==================================
        // SUCCESS
        // ==================================

        if (data.success === true) {

            // Display generated email
            generatedEmail.textContent = data.email;


            // Hide empty message
            emptyState.classList.add("hidden");


            // Show generated email
            resultContainer.classList.remove("hidden");


            // Scroll to result on smaller screens
            resultContainer.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });

        }


        // ==================================
        // ERROR FROM FASTAPI / GEMINI
        // ==================================

        else {

            alert(
                "Unable to generate email.\n\n" +
                data.message
            );

        }


    }


    // ==================================
    // CONNECTION ERROR
    // ==================================

    catch (error) {

        console.error(
            "Error:",
            error
        );

        alert(
            "Could not connect to the server.\n\n" +
            "Please make sure FastAPI is running."
        );

    }


    // ==================================
    // RESTORE BUTTON
    // ==================================

    finally {

        generateButton.disabled = false;

        buttonText.textContent =
            "✨ Generate Email";

    }

});


// ==========================================
// COPY GENERATED EMAIL
// ==========================================

copyButton.addEventListener(
    "click",
    async function () {

        const email =
            generatedEmail.textContent;


        // Check if email exists
        if (!email) {

            alert(
                "There is no generated email to copy."
            );

            return;
        }


        try {

            // Copy email to clipboard
            await navigator.clipboard.writeText(email);


            // Change button text
            copyButton.textContent =
                "✓ Copied!";


            // Restore button text
            setTimeout(function () {

                copyButton.textContent =
                    "📋 Copy";

            }, 2000);


        }

        catch (error) {

            console.error(
                "Copy error:",
                error
            );

            alert(
                "Unable to copy the email."
            );

        }

    }
);