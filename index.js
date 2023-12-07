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

document.querySelectorAll('#sentence tr').forEach(tr => {
	const td = tr.querySelector('td[id]');
	if (td === null) return; // not a td row
	td.tabIndex = 0;
	tr.addEventListener('mouseenter', () => on(td));
	tr.addEventListener('mouseleave', () => off(td));
	tr.addEventListener('click', () => {
		document.querySelectorAll('td[id]').forEach(td2 => off(td2));
		on(td);
	});
	td.addEventListener('focus', () => on(td));
	td.addEventListener('blur', () => off(td));
});

Array.from(document.getElementsByTagName('abbr')).forEach(abbr => {
	abbr.tabIndex = 0;
});
