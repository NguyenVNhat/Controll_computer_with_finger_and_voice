function captureScreen() {
    fetch('/screenshot', { method: 'POST' })
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
    
});
