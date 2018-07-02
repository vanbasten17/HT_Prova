from flask import Flask
from flask import request
from flask import render_template
from flask import json
import xkcd
import utils.comic_utils as comic_utils


app = Flask(__name__)

def initial_view():
	"""
    Loads the initial view of the application.

    Returns
    -------
    A rendered_template with the comic data to fill HTML
        
    """
	comic = xkcd.getRandomComic()
	comic_data = comic_utils.get_comic_data(comic)		
	return render_template('view.html', data=comic_data)

@app.route('/', methods=['GET', 'POST'])
def render_view():
	"""
    Entry point of the application.
    
    """
	return initial_view()

@app.route('/retrieve_comic/', methods=['GET', 'POST'])
def retrieve_comic():
	"""
    Deal with the AJAX request from client-side and returns a JSON response.
    In case of being requested by the client-side with a POST, change between the different modes.
    Otherwise, redirects to initial_view.

    Returns
    -------
    Response (JSON formatted)
        
    """
	if request.method == 'POST':
		first_comic_id = 1
		max_comic_id = xkcd.getLatestComicNum()
		json_request = request.get_json(force=True)
		current_comic_id = int(json_request['id'])
		mode = json_request['mode']
		comic = comic_utils.generate_comic_for_mode(current_comic_id, first_comic_id, max_comic_id, mode)
	
	else:
		return initial_view()

	comic_data = comic_utils.get_comic_data(comic)
	response = json.dumps(comic_data)

	return response

@app.errorhandler(404)
def page_not_found(e):
    """
    Prints an error message if an inexistent mapped url is requested.
    """
    return "<h1>This page doesn't exist</h1>"	
if __name__ == '__main__':
	"""
    Default parameters for running the application.
	localhost:5050

    """
	app.run()