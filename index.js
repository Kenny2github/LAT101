const sentence = document.getElementById('sentence');

/**
 * @param {HTMLTableCellElement} td
 */
function on(td) {
	sentence.classList.add(td.id);
	document.querySelectorAll('#explanations .' + td.id).forEach(e => {
		e.style.display = 'block';
	});
	td.classList.forEach(id => {
		document.querySelectorAll(`#explanations .${td.id}_${id}`).forEach(e => {
			e.style.display = 'block';
		});
	});
}
/**
 * @param {HTMLTableCellElement} td
 */
function off(td) {
	sentence.classList.remove(td.id);
	document.querySelectorAll('#explanations .' + td.id).forEach(e => {
		e.style.display = 'none';
	});
	td.classList.forEach(id => {
		document.querySelectorAll(`#explanations .${td.id}_${id}`).forEach(e => {
			e.style.display = 'none';
		});
	});
}

document.querySelectorAll('td[id]').forEach(td => {
	td.addEventListener('mouseenter', () => on(td));
	td.addEventListener('mouseout', () => off(td));
	td.addEventListener('click', () => {
		if (sentence.classList.contains(td.id)) off(td);
		else off(td);
	});
});
