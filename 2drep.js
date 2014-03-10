function draw(width, height) {
    s = d3.select(".rep").append("svg")
	.attr("width", width)
        .attr("height", height)
        .attr("class", "rep");

    var boxHeight = 50;
    var boxWidth = 50;
    for (k = 0; k < 3; k++) {
	for (j = 0; j < 3; j++) {
	    s.append("rect")
		.attr("width", boxHeight)
	        .attr("class", "rep")
	        .attr("name", "s" + k + "-" + j)
	        .attr("height", boxWidth)
	        .attr("transform", "translate(" + k * boxHeight + "," + j*boxWidth + ")")
	        .style("stroke", "black")
	        .style("stroke-width", "1px")
	        .style("fill", function(d) {return "white";})
	        .on("mouseover", function (d) {this.style.fill = "black";
					       d3.selectAll("circle." + this.getAttribute("name")) 
					      .style("stroke", 
						     function(d) {
							 d._stroke = d.stroke; 
							 return "black";})
					      .style("stroke-width", 10);})
	        .on("mouseout", function (d)  {this.style.fill = "white";
		    d3.selectAll("circle." + this.getAttribute("name")) 
					      .style("stroke", 
						     function(d) {
							 return "None";})
					      .style("stroke-width", 3);});
	}
    }
}


function highlight(state) {
    rects = document.querySelectorAll('rect.rep')
    //rects = d3.selectAll("rect.rep");
    for (k = 0; k < rects.length; k++) {
	//console.log(rects[0].getAttribute("name")); console.log(state); 
	rects[k].getAttribute("name") == state  ? rects[k].style.fill = "black" : 0;
    }
}

function unhighlight(state) {
    rects = document.querySelectorAll('rect.rep')
    //rects = d3.selectAll("rect.rep");
    for (k = 0; k < rects.length; k++) {
	//console.log(rects[0].getAttribute("name")); console.log(state); 
	rects[k].getAttribute("name") == state  ? rects[k].style.fill = "white" : 0;
    }
}