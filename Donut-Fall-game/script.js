document.addEventListener("DOMContentLoaded", () => {
    const gameContainer = document.getElementById("game-container");
    const basket = document.querySelector(".basket");
    const scoreDisplay = document.getElementById("score");
    
    let basketX = 160;
    const basketSpeed = 20;
    const gameWidth = 400;
    let gameOver = false;
    let score = 0;

    // Move the basket
    document.addEventListener("keydown", (event) => {
        if (event.key === "ArrowLeft" && basketX > 0) {
            basketX -= basketSpeed;
        } else if (event.key === "ArrowRight" && basketX < gameWidth - 80) {
            basketX += basketSpeed;
        }
        basket.style.left = `${basketX}px`;
    });

    // Create falling donuts
    function createFallingObject() {
        if (gameOver) return;

        const fallingObject = document.createElement("img");
        fallingObject.src = "donut.png"; 
        fallingObject.classList.add("falling-object");
        fallingObject.style.left = `${Math.random() * (gameWidth - 40)}px`;
        gameContainer.appendChild(fallingObject);

        let fallInterval = setInterval(() => {
            if (gameOver) {
                clearInterval(fallInterval);
                return;
            }
            let objectY = fallingObject.offsetTop + 5;
            fallingObject.style.top = `${objectY}px`;

            if (objectY > 460) {
                if (
                    basketX < fallingObject.offsetLeft + 40 &&
                    basketX + 80 > fallingObject.offsetLeft
                ) {
                    clearInterval(fallInterval);
                    gameContainer.removeChild(fallingObject);
                    score++; // Increase score
                    scoreDisplay.textContent = score;
                } else if (objectY > 480) { // If missed, game over
                    clearInterval(fallInterval);
                    gameContainer.removeChild(fallingObject);
                    alert(`Game Over! You scored ${score} points!`);
                    gameOver = true;
                }
            }
        }, 50);

        // Random new donuts
        setTimeout(createFallingObject, Math.random() * 2000 + 1000);
    }

    createFallingObject(); // Start the game
});
