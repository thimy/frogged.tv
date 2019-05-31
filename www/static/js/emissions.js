window.onload = function(e) {
  document.addEventListener('click', evt => {
    if (evt.target.classList.contains('submission__up')) {
      const url = 'submission__up?' + ''
      fetch('submission_vote?')
        .then(response => response.json())
        .then(data => {

        })
    }
  })
}
