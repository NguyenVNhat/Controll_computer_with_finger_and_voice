// script.js

// Định nghĩa hàm captureScreen ở phạm vi toàn cục
function captureScreen() {
    fetch('/gettime', { method: 'POST' })
        .then(response => {
            if (response.ok) {
                console.log("Chụp màn hình thành công!");
            } else {
                console.error("Lỗi khi chụp màn hình.");
            }
        })
        .catch(error => {
            console.error("Lỗi khi chụp màn hình:", error);
        });
}

document.addEventListener('DOMContentLoaded', function() {
    var button = document.getElementById('captureButton');
    button.addEventListener('click', function() {
        captureScreen();
    });
});
