let score = JSON.parse(localStorage.getItem('score')) || { wins: 0, loss: 0, tie: 0 };
updateScore();

function playGame(playerMove) {
  const computerMove = pickComputerMove();
  let result = '';

  if (playerMove === computerMove) {
    result = 'Tie.';
  } else if (
    (playerMove === 'rock' && computerMove === 'scissors') ||
    (playerMove === 'paper' && computerMove === 'rock') ||
    (playerMove === 'scissors' && computerMove === 'paper')
  ) {
    result = 'You win.';
  } else {
    result = 'You lose.';
  }

  if (result === 'You win.') score.wins++;
  else if (result === 'You lose.') score.loss++;
  else score.tie++;

  localStorage.setItem('score', JSON.stringify(score));
  updateScore();
  updateResult(result);
  updateMoves(playerMove, computerMove);
}

function updateScore() {
  document.querySelector('.js-p').innerHTML =
    `Wins: ${score.wins} | Loss: ${score.loss} | Tie: ${score.tie}`;
}

function updateResult(result) {
  document.querySelector('.js-result').innerHTML = result;
}

function updateMoves(player, computer) {
  document.querySelector('.js-move').innerHTML = `
    You <img src="images/${player}-emoji.png" class="move-icon">
    <img src="images/${computer}-emoji.png" class="move-icon"> Computer`;
}

function pickComputerMove() {
  const moves = ['rock', 'paper', 'scissors'];
  return moves[Math.floor(Math.random() * 3)];
}

function zero() {
  score = { wins: 0, loss: 0, tie: 0 };
  localStorage.setItem('score', JSON.stringify(score));
  updateScore();
}
