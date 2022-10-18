// forms DOM elements
initForm = document.getElementById("initSimulation")
runForm = document.getElementById("runSimulation")

// button access
initFormBtn = document.getElementById("initSimulationBtn")
runFormBtn = document.getElementById("runSimulationBtn")

// progression bar
progressBar = document.getElementById("simulationProgress")

// error display
simulationError = document.getElementById("simulationError")

// legend panel
legendPanel = document.getElementById("legendPanel")
legendTitle = document.getElementById("legendTitle")

// canvas
var simulationCanvas = document.getElementById('simulationCanvas');

var updateInterval = undefined;
var runningSimulation = false; 
var legendData = {}
var hotspots = [] // store information about elements
var possibleColors = ['#2ca02c', '#d69728', '#9497bd', '#8c564b', '#e377c2', '#7f7f5f', 
    '#bcbd72', '#17becf', '#1a55FF', '#1f27b4', '#ff1f0e']

var seasonIcons = {
    "Summer": {"icon": "thermometer-sun", "color": "#991f00"},
    "Fall": {"icon": "thermometer-low", "color": "#183867"},
    "Winter": {"icon": "thermometer-snow", "color": "#3070cf"},
    "Spring": {"icon": "thermometer-half", "color": "#995c00"}
}

function degToCompass(deg) {
    var val = Math.floor((deg / 45) + 0.5);
    var arr = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"];
    return arr[(val % 8)];
}

// get canvas offset values
function reOffset() {
    // get bounding box
    var BB = simulationCanvas.getBoundingClientRect();
    offsetX = BB.left;
    offsetY = BB.top;
}

// update values using reOffset function
var offsetX, offsetY;
reOffset();

// manage canvas resize if necessary
window.onscroll = function (e) {
    reOffset();
};

window.onresize = function (e) {
    reOffset();
};

function drawString(ctx, text, posX, posY, textColor, font, fontSize) {

    var maxChars = 0
	var lines = text.split("\n");


    for (i = 0; i < lines.length; i++) {
        if (maxChars < lines[i].length) 
            maxChars = lines[i].length
    }

    ctx.save();

    const w_canvas = simulationCanvas.width
    const h_canvas = simulationCanvas.height

    // move (x, y) of text position depending of border
    if (posX - 60 < 0)
        posX += 60

    if (posY - 60 < 0)
        posY += 60

    // compute width and height of rectangle
    rect_width = (4 * maxChars) * (fontSize / 15) + 10;
    rect_height = (lines.length * fontSize) + fontSize / 2;

    if (posX + rect_width + 40 > w_canvas)
        posX -= (rect_width + 80)

    if (posY + rect_height > h_canvas)
        posY -= (rect_height)

    // draw in background rectangle
    ctx.shadowOffsetX = fontSize / maxChars;
    ctx.shadowOffsetY = fontSize / lines.length;
    ctx.shadowBlur = fontSize / 4;
    ctx.shadowColor = 'rgba(21, 24, 50, 0.3)';
    ctx.rect(posX - 10, posY - (fontSize + 2), rect_width, rect_height)
    ctx.fillStyle = "#fff";
    ctx.strokeStyle = "#000"
    ctx.lineWidth = fontSize / 10;
    ctx.fill()
    ctx.restore()
    ctx.stroke()

	if (!font) font = "'serif'";
	if (!fontSize) fontSize = 16;
	if (!textColor) textColor = '#000000';
	ctx.save();
	ctx.font = fontSize + "px " + font;
	ctx.fillStyle = textColor;
	ctx.translate(posX, posY);
	for (i = 0; i < lines.length; i++) {
 		ctx.fillText(lines[i],0, i*fontSize);
	}
	ctx.restore();
}

function updateLegendAndContext(json) {

    // first, display expected data into legend
    const table = document.createElement('table');
    table.className = 'table';

    const tbody = document.createElement('tbody');

    alive_trees = json.trees.filter((element, _) => {
        return !element.fallen;
    }).length
    humus_trees = json.trees.length - alive_trees

    // for each data add `tr`
    // use of col-md in order to avoid refresh flickering behavior
    let trWeather = document.createElement('tr');
    trWeather.innerHTML = `<th class="col-md-3"><strong>Weather</strong></th>
        <td class="col-md-3"><i class="bi bi-sun-fill" style="color: #cca300"></i> ${(json.weather.sun * 100).toFixed(0)}<span style="font-size: 8px">%</span></td>
        <td class="col-md-3"><i class="bi bi-droplet-half" style="color: #0066cc"></i> ${(json.weather.humidity * 100).toFixed(0)}<span style="font-size: 8px">%</span></td>
        <td class="col-md-3"><i class="bi bi-wind" style="color: #1f2e2e;"></i> ${(json.weather.wind_speed).toFixed(0)} <span style="font-size: 8px">km/h (${degToCompass(json.weather.wind_angle)})</span></td>`;
        
    tbody.appendChild(trWeather);

    let trTree = document.createElement('tr');
    trTree.innerHTML = `<th scope="row"><strong>Trees</strong></th>
        <td><i class="legend-tree"></i>${alive_trees}</td>
        <td colspan="2"><i class="legend-humus"></i>${humus_trees} (humus)</td>`;

    tbody.appendChild(trTree);

    // TODO: add current number of animals information inside current table
    // use of class `legend-animal`

    let trSeed = document.createElement('tr');
    trSeed.innerHTML = `<th scope="row"><strong>Seeds</strong></th>
        <td><i class="legend-seed"></i>${json.seeds.length}</td>
        <td></td>
        <td></td>`;
    tbody.appendChild(trSeed);


    legendData = {}
    hotspots = []

    nspecies = 0

    // by default sort trees by specie name
    trees = json.trees.sort((a, b) => {return a.specie > b.specie})

    // load for each tree kind and seed
    for (let tree of trees) {

        if (!(tree.specie in legendData)) {
            
            // create default key for current specie
            legendData[tree.specie] = {
                'trees': 0,
                'humus': 0,
                'seeds': 0,
                'color': possibleColors[nspecies]
            }
            nspecies += 1;
        }

        if (!tree.fallen)
            legendData[tree.specie].trees += 1
        else
            legendData[tree.specie].humus += 1

        // add new tree element into hotspots
        hotspots.push({
            'x': tree.coordinate.x, 
            'y': tree.coordinate.y, 
            'radius': tree.radius,
            'legend': `Specie: ${tree.specie}\
                    \nPosition: (${tree.coordinate.x.toFixed(2)}, ${tree.coordinate.y.toFixed(2)})\
                    \nBranches: ${tree.branches.length} (broken: ${tree.broken_branches})\
                    \nAge: ${tree.age}\
                    \nMax age: ${tree.max_age.toFixed(0)}\
                    \nHeight: ${tree.height.toFixed(2)}\
                    \nWidth: ${tree.width.toFixed(2)}\
                    \nHealth: ${tree.health.toFixed(2)}\
                    \nFallen: ${tree.fallen}`
        })
    }

    // by default sort seeds by type name
    seeds = json.seeds.sort((a, b) => {return a.tree_type > b.tree_type})

    for (let seed of seeds) {

        if (!(seed.tree_type in legendData)) {
            
            legendData[seed.tree_type] = {
                'trees': 0,
                'humus': 0,
                'seeds': 1,
                'color': possibleColors[nspecies]
            }
            nspecies += 1;
        }

        hotspots.push({
            'x': seed.coordinate.x, 
            'y': seed.coordinate.y, 
            'radius': 0.2,
            'legend': `Specie: ${seed.tree_type}\
                    \nPosition: (${seed.coordinate.x.toFixed(2)}, ${seed.coordinate.y.toFixed(2)})\
                    \nFallen: ${seed.fallen}`
        })

        legendData[seed.tree_type].seeds += 1
    }

    for (const [key, value] of Object.entries(legendData)) {
        
        let tr = document.createElement('tr');
        tr.className = 'specie'
        tr.innerHTML = `<td class="col-md-3"><strong>${key}</strong></td>
            <td class="col-md-3"><i class="legend-tree" style="background-color: ${value.color}"></i>${value['trees']}</td>
            <td class="col-md-3"><i class="legend-humus" style="background-color: ${value.color}"></i>${value['humus']}</td>
            <td class="col-md-3"><i class="legend-seed" style="background-color: ${value.color}"></i>${value['seeds']}</td>`;

        tbody.appendChild(tr);
    }

    table.appendChild(tbody);

    // clear and append new content into panel
    legendPanel.innerHTML = "";
    legendPanel.appendChild(table);

    // update the legend panel too
    legendTitle.innerHTML = `
        <div class="row">
            <div class="col-md-9"><strong>Legend</strong>: ${json.current_date}</div>
            <div class="col-md-3"><i class="bi bi-${seasonIcons[json.season].icon}" style="color:${seasonIcons[json.season].color}"></i> ${json.season}</div>
        </div>`

    // update progress bar data
    progressBar.setAttribute('style', `width: ${json.progression}%;`)
    progressBar.setAttribute('aria-valuenow', json.progression)
    progressBar.innerHTML = `${json.progression.toFixed(0)}%`

    // check access to the run button and add/reset button
    if (!json['finished']) {
        
        initFormBtn.className = "btn btn-outline-success btn-sm"
        initFormBtn.innerHTML = `<i class="bi bi-arrow-repeat"></i>`

        runFormBtn.className = "btn btn-outline-success"
        // change icon depending of running state or not
        if (updateInterval !== undefined) {
            runFormBtn.innerHTML = `<i class="bi bi-pause">`
        } else {
            runFormBtn.innerHTML = `<i class="bi bi-play">`
            runFormBtn.disabled = false
        }

    } else {
        
        // if finished need to stop the current running process
        if (updateInterval !== undefined) {
            clearInterval(updateInterval);
            updateInterval = undefined;
            runningSimulation = false;
        }

        // disabled the run button if already stops
        runFormBtn.disabled = true
        runFormBtn.className = "btn btn-outline-secondary"
        runFormBtn.innerHTML = `<i class="bi bi-play">`

        // let the possibility to create another simulation
        initFormBtn.className = "btn btn-outline-success btn-sm"
        initFormBtn.innerHTML = `<i class="bi bi-plus-lg"></i>`
    }
}

/**
 * Enable to update the current canvas simulation with json context data
 * 
 * @param {*} json data
 */
function updateCanvas(json) {

    // update the world canvas
    var context = simulationCanvas.getContext('2d');

    context.clearRect(0, 0, simulationCanvas.width, simulationCanvas.height);
    
    let w_factor = simulationCanvas.width / json.width;
    let h_factor = simulationCanvas.height / json.height;

    // add elements for each tree
    for (let tree of json.trees) {

        fillColor = legendData[tree.specie].color

        context.beginPath();
        context.arc(tree.coordinate.x * w_factor, tree.coordinate.y * h_factor, tree.radius * (h_factor + w_factor) / 2, 0, 2 * Math.PI, false);
        context.fillStyle = fillColor;
        context.fill();
        context.lineWidth = tree.fallen ? 12 : 4;
        context.strokeStyle = '#000000';
        context.stroke();
    }

    // add elements for each seeds
    for (let seed of json.seeds) {

        fillColor = legendData[seed.tree_type].color
    
        context.beginPath();
        context.rect(seed.coordinate.x * w_factor - 4, seed.coordinate.y * h_factor - 4, 8, 8);
        context.fillStyle = fillColor;
        context.fill();
        context.lineWidth = 4;
        context.strokeStyle = '#000000';
        context.stroke();
    }

    // TODO: add elements for each animals
    // How to draw triangle: https://www.kirupa.com/html5/drawing_triangles_on_the_canvas.html

    // set a new on mouse move event inside canvas
    // enable to display tree information during simulation
    // if tree information are displayed, then simulation is temporarily interrupted
    simulationCanvas.onmousemove = e => {

        // tell the browser we're handling this event
        e.preventDefault();
        e.stopPropagation();

        var checkInside = false;

        mouseX = parseInt(e.clientX - offsetX);
        mouseY = parseInt(e.clientY - offsetY);

        // need to clear and update again the canvas (in order to draw legend)
        context.clearRect(0, 0, simulationCanvas.width, simulationCanvas.height);
        
        // update from json data
        updateCanvas(json)

        const current_width = simulationCanvas.getBoundingClientRect().width;
        const current_height = simulationCanvas.getBoundingClientRect().height;
        
        // need to retrieve the current canvas size due to auto resize
        // it's in order to track mouse coordinate inside canvas and match trees and seeds positions
        let inner_w_factor = w_factor * (current_width / simulationCanvas.width);
        let inner_h_factor = h_factor * (current_height / simulationCanvas.height);
        
        // prepare an event for each tree inside the current simulation
        // each event display tree information using `drawString` function
        for (var i = 0; i < hotspots.length; i++) {

            var h = hotspots[i];
            var dx = mouseX - (h.x * inner_w_factor);
            var dy = mouseY - (h.y * inner_h_factor);

            // use of area in order to determine data
            if (dx * dx + dy * dy < h.radius * h.radius * inner_w_factor * inner_h_factor * 10) {

                context.beginPath();
                drawString(context, h.legend, h.x * w_factor + 40, h.y * h_factor - 20, "#000", "Arial", 50)

                checkInside = true;
                break;
            }
            else {
                checkInside = false;
            }
        }

        // stop while checking data
        if (checkInside && runningSimulation) {

            // stop simulation
            updateInterval = clearInterval(updateInterval)

            // update run button with play (simulation have been paused)
            runFormBtn.innerHTML = `<i class="bi bi-play">`

            // if simulation is paused, change the progressBar display
            if (!json.finished)
                progressBar.className = 'progress-bar progress-bar-striped bg-success'

        } else if (updateInterval === undefined && runningSimulation && !json.finished) {
            // check if necessary to run again the simulation
            updateInterval = setInterval(_ => {callSimulationServer('/step', 'POST')}, 100);
            progressBar.className = 'progress-bar bg-success'
        }
    };
}

/**
 * Generic function in order to call specific route with specific method ['POST', 'GET']
 * Update the current simulation context and display canvas simulation state
 * 
 * @param {*} route 
 * @param {*} currentMethod 
 */
async function callSimulationServer(route, currentMethod) {
    // check current running state using and initialize the world if exists
    let response = await fetch(route, {
        method: currentMethod
    });

    if (response.ok) { 

        // hide error
        simulationError.style.display = 'none';

        // get the response body (the method explained below)
        let json = await response.json();

        reOffset();
        updateLegendAndContext(json);
        updateCanvas(json);
    } 
    else {

        // if error during process, stop the current simulation
        if (updateInterval !== undefined) {
            updateInterval = clearInterval(updateInterval);
        }

        let json = await response.json();

        // display the current error and inform the user
        simulationError.innerHTML = 
        `<div class="alert alert-warning d-flex align-items-center" role="alert">
            <span class="bi flex-shrink-0 me-2" width="24" height="24"><i class="bi bi-exclamation-triangle-fill"></i></span>
            <div>
                ${json.error}
            </div>
        </div>`
        simulationError.style.display = 'block';

        // simulation is no longer available (not loaded)
        legendPanel.innerHTML = '<div style="margin-top: 1em; text-align: center;"><p><i>No current simulation available</i></p></div>'

        console.log("HTTP-Error: " + response.status);
    }
}

// by default init the current page
callSimulationServer('/state', 'GET');

/**
 * Once the reset or init form submit, call the init route
 * @param {Event} e 
 */
initForm.onsubmit = async e => {
    e.preventDefault();
    e.stopPropagation();
    callSimulationServer('/init', 'POST');
}

/**
 * Enable to start or resume (if paused) the simulation
 * @param {Event} e 
 */
runForm.onsubmit = async e => {
    e.preventDefault();
    e.stopPropagation();

    // check if run or pause state
    if (updateInterval !== undefined) {
        runningSimulation = false;
        updateInterval = clearInterval(updateInterval)
        runFormBtn.innerHTML = `<i class="bi bi-play">`
    } else {
        runningSimulation = true;
        updateInterval = setInterval(_ => {callSimulationServer('/step', 'POST')}, 200);
    }
}
