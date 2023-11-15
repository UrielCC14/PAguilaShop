const pElement = document.querySelector('.intercalated-bg');
const words = pElement.textContent.split(' ');
pElement.innerHTML = words.map((word, index) => `<span>${word}</span>`).join(' ');

/*window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    // Calculamos la nueva posición horizontal de la imagen
    const newRightPosition = `${scrollY}px`;
    const newTopPosition = `${scrollY}px`

    // Aplicamos la nueva posición a la imagen
    document.querySelector('img').style.right = newRightPosition;
    document.querySelector('img').style.top = newTopPosition;
});
*/

