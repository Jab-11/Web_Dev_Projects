const maxInput = document.getElementById("max");
const minInput = document.getElementById("min");
const guessInput = document.getElementById("guess");
const result = document.getElementById("result");
let num;

function mrandom() {
    console.log("mrandom function called");

    const max = parseFloat(maxInput.value);
    const min = parseFloat(minInput.value);

    if (isNaN(max) || isNaN(min)) {
        result.textContent = "Invalid input. Please enter valid numbers for min and max.";
        return;
    }

    if (max < min) {
        result.textContent = "The max is less than min.";
    } else {
        num = Math.floor(Math.random() * (max - min + 1)) + min;
        console.log(num);

        localStorage.setItem('generatedNum', num);

        result.textContent = "";
        window.location.href = "game.html";
    }
}

function check() {
    const num = parseFloat(localStorage.getItem('generatedNum'));
    console.log(num);
    // Retrieve the user's guess from the input field
    const guess = parseFloat(guessInput.value);

    // Check if the guess is valid (not NaN)
    if (isNaN(guess)) {
        result.textContent = "Please enter a valid number.";
    } else {
        // Compare the guess with the generated number (num)
        if (guess === num) {
            result.textContent = "You guessed it right! :)";
        } else if (guess > num) {
            result.textContent = "Your guess is higher.";
        } else {
            result.textContent = "Your guess is lower.";
        }
    }
}