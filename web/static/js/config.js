inputRangeTreeNumber = document.getElementById("treeNumber")
inputRangeDaysNumber = document.getElementById("daysNumber")

/**
 * Enable to update the input range indicator for the number of tree
 * 
 * @param {Number} ntrees 
 */
function changeNTrees(ntrees) {
        
    inputRangeTreeNumber.innerHTML = ntrees;
}

/**
 * Enable to update the input range indicator for the number of days
 * 
 * @param {Number} ndays 
 */
function changeNDays(ndays) {
        
    inputRangeDaysNumber.innerHTML = ndays;
}
