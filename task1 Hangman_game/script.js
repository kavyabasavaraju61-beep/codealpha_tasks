const words = ["hackathon", "launch", "developer", "monitor", "arguments", "satisfy", "collabration", "prime", "communication", "eternity"];
let wordToGuess;
let guessedLetters;
let wrongGuesses;
const maxIncorrect = 6;

function resetGame() {
    wordToGuess = words[Math.floor(Math.random() * words.length)];
    guessedLetters = [];
    wrongGuesses = 0;
    document.getElementById("message").textContent = "";
    document.getElementById("wrongGuesses").textContent = wrongGuesses;
    document.getElementById("guessedLetters").textContent = "";
    document.getElementById("letterInput").value = "";
    updateWordDisplay();
}

function updateWordDisplay() {
    let display = "";
    for (let letter of wordToGuess) {
        display += guessedLetters.includes(letter) ? letter + " " : "_ ";
    }
    document.getElementById("wordDisplay").textContent = display.trim();
}

function guessLetter() {
    const input = document.getElementById("letterInput");
    const letter = input.value.toLowerCase();
    input.value = "";

    if (!letter.match(/[a-z]/) || letter.length !== 1) {
        alert("Please enter a valid letter.");
        return;
    }

    if (guessedLetters.includes(letter)) {
        alert("You already guessed that letter!");
        return;
    }

    guessedLetters.push(letter);

    if (wordToGuess.includes(letter)) {
        document.getElementById("message").textContent = "Good guess!";
    } else {
        wrongGuesses++;
        document.getElementById("wrongGuesses").textContent = wrongGuesses;
        document.getElementById("message").textContent = "Wrong guess!";
    }

    document.getElementById("guessedLetters").textContent = guessedLetters.join(", ");
    updateWordDisplay();
    checkGameStatus();
}

function checkGameStatus() {
    if (!document.getElementById("wordDisplay").textContent.includes("_")) {
        document.getElementById("message").textContent = "Congratulations, You won! The word was: " + wordToGuess;
    } else if (wrongGuesses >= maxIncorrect) {
        document.getElementById("message").textContent = "Oh no, You lost! The word was: " + wordToGuess;
    }
}

window.onload = resetGame;