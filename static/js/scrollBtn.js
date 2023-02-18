const scrollToTopBtn = document.getElementById("scrollToTopBtn");
const scrollToBottomBtn = document.getElementById("scrollToBottomBtn");

window.onscroll = function() {
    scrollFunction()
    /*$.ajax({
        type: "post",
        url: "/getMovieReviews",
        data: {"movie_imdb_id":movieData['imdb_id']},
        dataType: "json",
        success: function (data) {
            $("#loader").fadeOut();
            console.log(data)
            if (data['status'] == true) {

                //*  Reviews *
                showReviews(data['reviews-details']);

            }
        }
    });*/
};

function scrollFunction() {
    if (document.body.scrollTop > 1000 || document.documentElement.scrollTop > 1000) {
        scrollToTopBtn.style.display = "block";
        scrollToBottomBtn.style.display = "none";
    } else {
        scrollToTopBtn.style.display = "none";
        scrollToBottomBtn.style.display = "block";
    }
}
function topFunction() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
};

function bottomFunction() {
    document.getElementById('recommend-movie').scrollIntoView({
        behavior: "smooth"
    });
}


scrollToTopBtn.addEventListener("click", function(e) {
    e.preventDefault();
    topFunction();
});

scrollToBottomBtn.addEventListener('click', function(e) {
    e.preventDefault();
    bottomFunction();
});