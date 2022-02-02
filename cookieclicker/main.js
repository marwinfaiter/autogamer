var autoclicker = setInterval(() => {
    try {
        var elements = [
            document.getElementById('bigCookie'),
            document.querySelector("[class='shimmer']"),
            document.querySelector("[class='crate upgrade enabled']"),
            document.querySelector("[class='product unlocked enabled']"),
        ];
        for (var element of elements) {
            if (element) element.click();
        }
    }
    catch (err) {
        clearInterval();
    }
  },
  1
);

clearInterval(autoclicker);
