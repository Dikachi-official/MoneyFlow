// Dictate and pickout what the user is typing
const usernameField = document.querySelector("#usernameField")
const feedBackArea = document.querySelector(".invalid-feedback")
const emailField = document.querySelector("#emailField")
const emailfeedBackArea = document.querySelector(".emailfeedBackArea")

    emailField.addEventListener("keyup", (e) =>
    {
        const emailValue = e.target.value;

            emailField.classList.remove('is-invalid');
            emailfeedBackArea.style.display = "none";
            
            if (emailValue.length > 0)
            {
                fetch("/authentication/validate-email/", 
                {
                    body: JSON.stringify({ email: emailValue}),
                    method: "POST",
                })
                .then((res) => res.json ())
                .then((data) =>
                {
                    console.log("data", data);
                    if(data.email_error)
                    {
                        emailField.classList.add('is-invalid');
                        emailfeedBackArea.style.display = "block";
                        emailfeedBackArea.innerHTML = `<p>${data.email_error}</p>`
                    }
                });     
            }

    });


    usernameField.addEventListener("keyup", (e) => 
    { 
        const usernameValue = e.target.value;

        usernameField.classList.remove('is-invalid');
        feedBackArea.style.display = "none";
        
        if (usernameValue.length > 0)
        {
            fetch("/authentication/validate-username/", 
            {
                body: JSON.stringify({ username: usernameValue}),
                method: "POST",
            })
            .then((res) => res.json ())
            .then((data) =>
            {
                console.log("data", data);
                if(data.username_error)
                {
                    usernameField.classList.add('is-invalid');
                    feedBackArea.style.display = "block";
                    feedBackArea.innerHTML = `<p>${data.username_error}</p>`
                }
            });     
        }
    });
