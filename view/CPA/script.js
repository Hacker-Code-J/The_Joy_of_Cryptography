document.getElementById('run-algo').addEventListener('click', function() {
    const blen = parseInt(document.getElementById('input-blen').value);
    const c1 = eavesdrop(0, blen);
    const c2 = eavesdrop(1, blen);

    document.getElementById('output-c1').textContent = `c1: ${c1}`;
    document.getElementById('output-c2').textContent = `c2: ${c2}`;
    const isEqual = c1 === c2;
    document.getElementById('output-comparison').textContent = `c1 equals c2: ${isEqual}`;
    
    // Call function to explain the result
    explainResult(isEqual, blen);
});

function eavesdrop(m, blen) {
    // Your actual logic here
    return `F(k, ${m}^${blen})`;
}

function explainResult(isEqual, blen) {
    let explanation = '';

    if (isEqual) {
        explanation = `Success: The algorithm correctly determined that c1 equals c2 for blen = ${blen}. This means... [additional explanation based on your algorithm's logic]`;
    } else {
        explanation = `Failure: The algorithm determined that c1 does not equal c2 for blen = ${blen}. This could be due to... [additional explanation based on your algorithm's logic]`;
    }

    document.getElementById('explanation').textContent = explanation;
}