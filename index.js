var dislikeCountInnerText;

function renderOrUpdateBar() {
  if (window.location.origin.match(/www\.youtube\.com/)) {
    if (window.location.pathname === "/watch") {
      var params = new URLSearchParams(window.location.search);
      var videoId = params.get("v");
      fetch(
        `https://8c6u7tq6ii.execute-api.us-east-1.amazonaws.com/prod/grabDislikeCount?video_id=${videoId}`
      )
        .then((x) => x.json())
        .then(function (data) {
          var YtdVideoDiv = document.querySelector(
            "#info-contents > ytd-video-primary-info-renderer"
          );

          var dislikeButton = [...document.querySelectorAll("#text")].find(
            (x) =>
              x.innerText.match(/DISLIKE|Dislike|dislike/) ||
              x.innerText == dislikeCountInnerText
          );

          dislikeButton.innerText = data.dislikes;
          dislikeCountInnerText = data.dislikes;

          YtdVideoDiv.style.borderBottomWidth = "3px";
          YtdVideoDiv.style.borderStyle = "solid";
          YtdVideoDiv.style.borderImage = `
            linear-gradient(
                to right,
                #493ae8 ${data.likesPercentAge}%, 
                red 10%
            )
            1 /              
            0px 0px 3px 0px /  
            0px 0px 0px 0px      
            round
    `;
        });
    }
  }
}

window.addEventListener("load", (event) => {
  renderOrUpdateBar();
});

const YtdWatchFlexy = document.querySelector("#page-manager > ytd-watch-flexy");
const config = { attributes: true };

observer = new MutationObserver(function (x, y) {
  x.forEach(function (mutation) {
    if (mutation.attributeName === "video-id") {
      console.log("Video Id has changed. Refreshing dislike bar");
      renderOrUpdateBar();
    }
  });
});

observer.observe(YtdWatchFlexy, config);
