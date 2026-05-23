function toggleMenu() {
    console.log('toggle');

    var hiddenBar = document.getElementById("hidden-bar");
    
    if (hiddenBar.style.display === "none") {
        hiddenBar.style.display = "flex";
    } else {
        hiddenBar.style.display = "none";
    }
}

function toggleImage(event) {
    const imageElement = event.target;
    const originalImage = "images/fliproom-carl-raw-unsplash.jpg";
    const hoverImage = "images/controller-ron-lach-pexels.jpg";

    if (imageElement.src.includes(originalImage)) {
        imageElement.src = hoverImage;
    } else {
        imageElement.src = originalImage;
    }
}

function rangeSlide() {
    var opinion = document.getElementById("opinion");
    var rating = document.getElementById("rating").value;
    if (rating >= 8) {
        opinion.style.colour = "green";
        opinion.innerHTML = "We are glad you have enjoyed it! 😃";
    } else if (rating >= 5) {
        opinion.style.colour = "orange";
        opinion.innerHTML = "Please, tell us how can we improve? 😐";
    } else {
        opinion.style.colour = "red";
        opinion.innerHTML = "Sorry for your experience with us! 😥";
    }
    return false;
}

// EVENT LISTENER
// Toggle hidden menu at navigation bar
document.getElementById("nav-menu").addEventListener("click", toggleMenu);

// Listen the pointer when over the image
var mainImage = document.getElementById("main-image");
mainImage.addEventListener("mouseenter", toggleImage);
mainImage.addEventListener("mouseleave", toggleImage);

// CHARACTER GAME
// Display the entered character with different styles
function displayCharacter() {
    const input = document.getElementById("fav-character").value;
    const displayParagraph = document.getElementById("character-display");
    const displayText = document.getElementById("character-text");

    displayText.textContent = input;
    displayText.style.colour = getRandomcolour();
    displayText.style.fontSize = `${Math.floor(Math.random() * 16 + 20)}px`;

    displayParagraph.style.display = "block";
}

// Event listener to call the function
document.getElementById("display-button").addEventListener("click", displayCharacter);

// Compare the entered character with a randomly generated one
document.getElementById("compare-button").addEventListener("click", function () {
    const input = document.getElementById("fav-character").value;
    const randomCharacter = generateRandomCharacter();
    const resultParagraph = document.getElementById("comparison-result");

    if (input.toLowerCase() === randomCharacter.toLowerCase()) {
        resultParagraph.textContent = `You win! Your character "${input}" matches the random character "${randomCharacter}".`;
        resultParagraph.style.colour = "#4caf50";
    } else {
        resultParagraph.textContent = `No match! Your character "${input}" and the random character "${randomCharacter}" do not match.`;
        resultParagraph.style.colour = "#f44336";
    }

    resultParagraph.style.display = "block";
});

// Function to generate a random character name from a list
function generateRandomCharacter() {
    const characters = ["Mario", "Luigi", "Pikachu", "Link", "Sonic", "Inky", "Ken", "Ryu", "Donkey Kong"];
    return characters[Math.floor(Math.random() * characters.length)];
}

// Function to generate a random colour, with a hexa-decimal string representation
function getRandomcolour() {
    const colours = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "brown", "black", "gray"];
    return colours[Math.floor(Math.random() * colours.length)];
}

// THE GAME
// Character data
const characters = [
    {
        name: "Mario",
        alias: "Super Mario",
        weapon: "Fire Flower",
        actor: "Charles Martinet",
        bio: "An italian plumber from the Mushroom Kingdom known for rescuing Princess Peach from Bowser.",
        image: "images/mario.png"
    },
    {
        name: "Ryu",
        alias: "Prosperous",
        weapon: "Hands",
        actor: "Kyle Hebert",
        bio: "Experienced martial artist, aiming to become the strongest he can.",
        image: "images/ryu.png"
    },
    {
        name: "Inky",
        alias: "Aosuke",
        weapon: "Himself",
        actor: "N/A",
        bio: "One of te main ghost in Pacman",
        image: "images/inky.png"
    },
    {
        name: "Pikachu",
        alias: "N/A",
        weapon: "Thunderbolt",
        actor: "Ikue Otani",
        bio: "Pikachu is an Electric Pokemon and the loyal companion of Ash Ketchum",
        image: "images/pikachu.png"
    },
    {
        name: "Donkey Kong",
        alias: "King of the Jungle",
        weapon: "Barrel",
        actor: "N/A",
        bio: "Donkey Kong is a strong gorilla who protects his jungle and collects bananas.",
        image: "images/donkey_kong.png"
    },

];

// Function to start the game
function startGame() {
    const randomIndex = Math.floor(Math.random() * characters.length);
    const character = characters[randomIndex];

    document.getElementById("character-name").textContent = character.name;
    document.getElementById("character-alias").textContent = character.alias;
    document.getElementById("character-weapon").textContent = character.weapon;
    document.getElementById("character-actor").textContent = character.actor;
    document.getElementById("character-bio").textContent = character.bio;
    document.getElementById("character-image").src = character.image;

    document.getElementById("character-info").style.display = "block";
}

// Event listener for the start game button
document.getElementById("start-game-button").addEventListener("click", startGame);
