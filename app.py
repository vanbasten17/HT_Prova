from flask import Flask
from flask import request
from flask import render_template
from flask import json
import xkcd
import helpers.my_helpers as helper


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def render_view():
	comic = xkcd.getRandomComic()
	
	comic_data = helper.get_comic_data(comic)

	return render_template('view.html', data=comic_data)

@app.route('/retrieve_comic/', methods=['GET', 'POST'])
def retrieve_comic():
	json_request = request.get_json(force=True)
	mode = json_request['mode']
	current_comic_id = json_request['id']
	
	if mode == 'random':
		comic = xkcd.getRandomComic()

	
	if mode == 'previous':
		previous_comic_id = int(current_comic_id) - 1
		comic = xkcd.getComic(previous_comic_id)

	if mode == 'next':
		next_comic_id = int(current_comic_id) + 1
		comic = xkcd.getComic(next_comic_id)
			
	comic_data = helper.get_comic_data(comic)
	response = json.dumps(comic_data)

	return response

if __name__ == '__main__':
	app.run()