from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

# import from constant
from constants.utils import UTILS


from tpblite import TPB

# Create a TPB object with a domain name
t = TPB('https://tpb.party')

# Or create a TPB object with default domain
t = TPB()

# Initialize app
app = Flask(__name__)

__UTILS = UTILS()


@app.route('/', methods=['POST', 'GET'])
def home():
    __MOVIE_NAME_LIST = __UTILS.getMovieNames()
    # Initialize variables
    __STATUS = False
    __ERROR = None
    
    # Get Top Search results
    __TOP_SEARCH = __UTILS.getTopSearch()

    
    return render_template('home.html',error=__ERROR, movieNamesList=__MOVIE_NAME_LIST, status=__STATUS, topSearch=__TOP_SEARCH)


@app.route('/getMovieDetails', methods=['POST', 'GET'])
def getMovieDetails():
    if request.method == "POST":
        searchMovieName = request.form.get('movie-name')
        print("searchMovieName: ",searchMovieName)
        __MOVIE_DETAILS, __CAST_DETAILS, _ = __UTILS.getMovieDetails(movie_name=searchMovieName)
        
        if (__MOVIE_DETAILS and __CAST_DETAILS) != None:
            return jsonify({
            'status':True,
            "movie-details":__MOVIE_DETAILS ,
            'cast-details':__CAST_DETAILS,
            })
        return jsonify({
            "status":False
        })
    return jsonify({
        "status":False
    })


@app.route('/getMovieReviews', methods=['POST', 'GET'])
def getMovieReviews():
    if request.method == "POST":
        movie_imdb_id = request.form.get('movie_imdb_id')
        __REVIEW_DICT =  __UTILS.scrap_review(imdb_id = movie_imdb_id)
        return jsonify({
            'status':True,
            "reviews-details":__REVIEW_DICT,
        })
    return jsonify({
        "status":False
    })

@app.route('/getRecommendedMovies', methods=['POST', 'GET'])
def getRecommendedMovies():
    if request.method == "POST":
        searchMovieName = request.form.get('movie-name')
        print("MOVIE_NAME: ",searchMovieName)
        __RECOMMEND_MOVIE_DETAILS_LIST = __UTILS.recommendMovie(movie_name=searchMovieName)
        print("__RECOMMEND_MOVIE_DETAILS_LIST: ",__RECOMMEND_MOVIE_DETAILS_LIST)
        __get = True
        return jsonify({
            'status':True,
            "recommend-movies":__RECOMMEND_MOVIE_DETAILS_LIST,
        })
    return jsonify({
        "status":False
    })
    
@app.route("/getTorrents", methods=["POST", "GET"])
def getTorrent():
    if request.method == "POST":
        movie_name = request.form.to_dict()['movie-name']
        torrents = t.search(movie_name)
        torrent = torrents.getBestTorrent(min_seeds=30, min_filesize='500 MiB', max_filesize='4 GiB')
        try:
            print(torrent.title, torrent.filesize, torrent.url)
            return jsonify({
                "status":True,
                "torrent-title":torrent.title,
                "torrent-filesize":torrent.filesize,
                "torrent-magnetlink":torrent.magnetlink
            })
        except:
            return jsonify({
                "status":False,
                "error-msg":"No torrent found..."
            })
    return jsonify({
        "status":False,
        "error-msg":"No torrent found..."
    })
    
@app.route("/get_movies_name", methods={"POST", "GET"})
def getMoviesName():
    if request.method== "GET":
        __MOVIE_NAME_LIST = __UTILS.getMovieNames()
        return jsonify({
            "status":True,
            "movieNamesList":__MOVIE_NAME_LIST
        })
    return jsonify({
        'status':False
    })


if __name__ == '__main__':
    app.debug = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.run()

