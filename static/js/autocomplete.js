new autoComplete({
    data: {
      src: films,
    },
    selector: "#search-movie",
    threshold: 1,
    debounce: 100,
    searchEngine: "strict",
    resultsList: {
        render: true,
        container: source => {
            source.setAttribute("id", "movie_list");
            $("#errorTag").css('display', 'none');
        },
        destination: document.querySelector("#search-movie"),
        position: "afterend",
        element: "ul"
    },
    maxResults: 6,
    highlight: true,
    resultItem: {
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    noResults: () => {
        const result = document.createElement("li");
        result.setAttribute("class", "no_result");
        result.setAttribute("tabindex", "1");
        result.innerHTML = "No Suggestion";
        $("#errorTag").css('display', 'block');
        $("#errorTag").text("*"+result.textContent+", \movie not found in the database..");
    },
    onSelection: feedback => {
        document.getElementById('search-movie').value = feedback.selection.value;
        postMovie(feedback.selection.value);
    }
});