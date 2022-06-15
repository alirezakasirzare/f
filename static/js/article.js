const heartDOM = document.querySelector('.js-heart');
// initialized like to false when user hasnt selected
let liked = false;

heartDOM.onclick = (event) => {
    // check if liked 
    liked = !liked; // toggle the like ( flipping the variable)

    // this is what we clicked on
    const target = event.currentTarget;

    if (liked) {
        // remove empty heart if liked and add the full heart
        target.classList.remove('far');
        target.classList.add('fas', 'pulse');
    } else {
        // remove full heart if unliked and add empty heart
        target.classList.remove('fas');
        target.classList.add('far');
    }
}

heartDOM.addEventListener('animationend', (event) => {
    event.currentTarget.classList.remove('pulse');
})




//============ copy ============
const shareBtn = document.querySelector('.share-btn');
const shareOptions = document.getElementById('share-options');
var link = document.getElementsByClassName("link");
link[0].innerHTML = window.location.href;




shareBtn.addEventListener('click', () => {
    shareOptions.classList.toggle('active');
})

function _handleClick(event) {
    event.preventDefault();

    var textarea = document.createElement("textarea");

    textarea.style.position = 'fixed';
    textarea.style.top = '-1px';
    textarea.style.left = '-1px';
    textarea.style.width = '1px';
    textarea.style.height = '1px';
    textarea.style.opacity = 0;
    textarea.style.pointerEvents = 'none';

    textarea.value = window.location.href;

    document.body.appendChild(textarea);

    textarea.select();

    try {
        var copiedURL = document.execCommand('copy');
        if (copiedURL) {
            alert('URL Copied');
        } else {
            console.log('Copy failed');
        }
    } catch (err) {
        console.log('Copy failed', err);
    }

    document.body.removeChild(textarea);
}

document.getElementById('copy').addEventListener('click', _handleClick, false);