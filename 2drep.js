function draw(width, height) {
    s = d3.select(".rep").append("svg")
	.attr("width", 150)
        .attr("height", 150)
        .attr("class", "rep");

    var boxHeight = 50;
    var boxWidth = 50;
    for (k = 2; k > -1; k--) {
	for (j = 2; j > -1; j--) {
	    s.append("rect")
		.attr("width", boxHeight)
	        .attr("class", "rep")
	        .attr("name", "s" + k + "-" + j)
	        .attr("height", boxWidth)
	        .attr("transform", "translate(" +  k * boxHeight + "," + 
		      (2-j)*boxWidth + ")")
	        .style("stroke", "black")
	        .style("stroke-width", "1px")
	        .style("fill", function(d) {
		    if (k == 1 && j == 0) {
			return "red";
		    }
		    else if (k == 2 && j == 2) {
			return "green";
		    } else {
			return "white";
		    }})
	        .on("mouseover", function (d) {
		    this.style._fill = this.style.fill;
		    this.style.fill = "black";
		    highlightNodes(this.getAttribute("name"));})
	        .on("mouseout", function (d)  {
		    this.style.fill = this.style._fill;
		    this.style._fill = null;
		    unhighlightNodes(this.getAttribute("name"));});
	    s.append("text")
            .text("FIRE PIT")
	        .attr("transform", "translate(" +  k * boxHeight + "," + 
		      (2-j)*boxWidth + ")")
	        //.attr("x", k * boxHeight) 
		//.attr("y", (2-j) * boxWidth)
	        .attr("text-anchor", "end")
	        .style("fill-opacity", 1.0)
	        .style("fill", "red");
	}
    }
}


function highlightState(state) {
    rects = document.querySelectorAll('rect.rep')
    //rects = d3.selectAll("rect.rep");
    for (k = 0; k < rects.length; k++) {
	if (rects[k].getAttribute("name") == state) {
	    rects[k].style._fill = rects[k].style.fill;
	    rects[k].style.fill = "black";
	}
    }
}

function unhighlightState(state) {
    rects = document.querySelectorAll('rect.rep')
    //rects = d3.selectAll("rect.rep");
    for (k = 0; k < rects.length; k++) {
	if (rects[k].getAttribute("name") == state) {
	    rects[k].style.fill = rects[k].style._fill;
	    rects[k].style._fill = null;
	}
    }
}

function highlightAction(state, action, states) {
    rects = document.querySelectorAll('rect.rep')
    console.log(states);
    for (k = 0; k < rects.length; k++) {
	for (j = 0; j < states.length; j++) {
	    nextState = states[j];
	    if (rects[k].getAttribute("name") == nextState) {
		rects[k].style._fill = rects[k].style.fill;
		rects[k].style.fill = "orange";
	    }
	}
	if (rects[k].getAttribute("name") == state) {
	    if (!rects[k].style._fill) {
		rects[k].style._fill = rects[k].style.fill;
	    }
	    rects[k].style.fill = "black";
	}
	
    }
}


function unhighlightAction(state, action, states) {
    rects = document.querySelectorAll('rect.rep')
    for (k = 0; k < rects.length; k++) {
	for (j = 0; j < states.length; j++) {
	    nextState = states[j];
	    if (rects[k].getAttribute("name") == nextState) {
		rects[k].style.fill = rects[k].style._fill;
		rects[k].style._fill = null;
	    }
	}
	if (rects[k].getAttribute("name") == state) {
	    console.log(rects[k].style._fill);
	    if (rects[k].style._fill) {
		rects[k].style.fill = rects[k].style._fill;
		rects[k].style._fill = null;

	    }
	}
	
    }
}

function highlightOneAction(state, action, nextState) {
    rects = document.querySelectorAll('rect.rep')
    for (k = 0; k < rects.length; k++) {
	if (rects[k].getAttribute("name") == state) {
	    rects[k].style._fill = rects[k].style.fill;
	    rects[k].style.fill = "black";
	}
	if (rects[k].getAttribute("name") == nextState) {
	    if (!rects[k].style._fill) {
		rects[k].style._fill = rects[k].style.fill;
	    }
	    rects[k].style.fill = "orange";
	}
    }
}


function unhighlightOneAction(state, action, nextState) {
    rects = document.querySelectorAll('rect.rep')
    for (k = 0; k < rects.length; k++) {
	if (rects[k].getAttribute("name") == nextState) {
	    rects[k].style.fill = rects[k].style._fill;
	    rects[k].style._fill = null;
	} 
	if (rects[k].getAttribute("name") == state) {
	    if (rects[k].style._fill) {
		rects[k].style.fill = rects[k].style._fill;
		rects[k].style._fill = null;

	    }

	}
    }
}
