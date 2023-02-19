form = document.getElementById("form");
form.addEventListener("submit", function(e) {e.preventDefault(); simulate();});

const ROBOT_1_STRAT = moveToSafety;
const ROBOT_2_STRAT = nonDeterministic;

var state = {
    N: 10,
    robot1_x: 0,
    robot1_y: 0,
    robot2_x: 9,
    robot2_y: 9,
    ctx: null,
    size: 800,
    image1: null, 
    image2: null,
    image3: null,
    timeout: null,
    crashed: false
}

function simulate() {
    clearTimeout(state.timeout);
    state.crashed = false;
    state.N = document.getElementById("N-input").value;
    state.robot1_x = 0;
    state.robot1_y = 0;
    state.robot2_x = state.N - 1;
    state.robot2_y = state.N - 1;
    cnvs = document.getElementById("canvas");
    state.size = cnvs.width
    state.ctx = cnvs.getContext("2d");
    state.image1 = new Image();
    state.image2 = new Image();
    state.image3 = new Image();
    state.image1.src = "robot.png";
    state.image2.src = "robotred.png";
    state.image3.src = "bang.png";
    update();
}

function update() {
    state.ctx.clearRect(0, 0, state.size, state.size);
    drawAreas();
    drawGrid();
    if (!state.crashed) {
        drawRobots();
        let step1 = ROBOT_1_STRAT();
        let step2 = ROBOT_2_STRAT();
        moveRobot1(step1);
        moveRobot2(step2);
    }
    state.timeout = setTimeout(update, 1000);
}

function drawAreas() {
    gridsize = state.size / state.N;

    state.ctx.fillStyle = "red";
    state.ctx.fillRect(0, 0, state.robot1_x*gridsize, state.size);
    state.ctx.fillRect(0, state.size - state.robot1_y*gridsize, state.size, state.size);

    state.ctx.fillStyle = "green";
    state.ctx.fillRect(0, 0, state.size, state.size - (state.robot2_y+1)*gridsize);
    state.ctx.fillRect((state.robot2_x+1)*gridsize, 0, state.size, state.size);
}

function drawGrid() {
    gridsize = state.size / state.N;
    state.ctx.beginPath();
    for (var i = 1; i < state.N; i++) {
        state.ctx.moveTo(0, i*gridsize);
        state.ctx.lineTo(state.size, i*gridsize);
    }
    for (var i = 1; i < state.N; i++) {
        state.ctx.moveTo(i*gridsize, 0);
        state.ctx.lineTo(i*gridsize, state.size);
    }
    state.ctx.stroke();
}

function drawRobots() {
    gridsize = state.size / state.N;

    if (state.robot1_x == state.robot2_x && state.robot1_y == state.robot2_y) {
        state.crashed = true;
        state.ctx.drawImage(state.image3, state.robot1_x*gridsize, state.size-(state.robot1_y+1)*gridsize, gridsize, gridsize);
    } else {
        state.ctx.drawImage(state.image1, state.robot1_x*gridsize, state.size-(state.robot1_y+1)*gridsize, gridsize, gridsize);
        state.ctx.drawImage(state.image2, state.robot2_x*gridsize, state.size-(state.robot2_y+1)*gridsize, gridsize, gridsize);
    } 
}

function moveRobot1(step) {
    state.robot1_x += step[0];
    state.robot1_y += step[1];
}

function moveRobot2(step) {
    state.robot2_x -= step[0];
    state.robot2_y -= step[1];
}

function nonDeterministic() {
    let r = Math.floor(2 * Math.random());
    return [r, 1-r];
}

function moveToSafety() {
    let x_dist = Math.abs(state.robot1_x - state.robot2_x);
    let y_dist = Math.abs(state.robot1_y - state.robot2_y);
    if (x_dist < y_dist) {
        return [1, 0];
    } else if (y_dist < x_dist) {
        return [0, 1];
    } else {
        let r = Math.floor(2 * Math.random());
        return [r, 1-r];
    }
}

function maximiseDistanceToSafety() {
    let s = moveToSafety();
    return [s[1], s[0]];
}

