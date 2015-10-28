(function() {
    // If injecting into an app that was already running at the time
    // the app was enabled, simply initialize it.
    if (document.documentElement) {
        initialize();
    }

    // Otherwise, we need to wait for the DOM to be ready before
    // starting initialization since add-ons are usually (always?)
    // injected *before* `document.documentElement` is defined.
    else {
        window.addEventListener('DOMContentLoaded', initialize);
    }

    function initialize() {
        // Build the 'M' element
        var container = document.createElement('div');
        container.id = 'statusbar-m';
        container.style.fontSize = '1.5rem';
        container.style.fontWeight = 'bold';
        container.style.color = '#fcee07';
        container.textContent = 'M';

        // If it's not already there, append the element to the status bar.
        var statusBar = document.querySelector('.statusbar');
        if (statusBar && !statusBar.contains(container)) {
            statusBar.appendChild(container);
        }
    }
}());
