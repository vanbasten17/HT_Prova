def get_comic_data(comic):
	base_url = 'https://xkcd.com/'
	comic_id = parse_id(comic.getExplanation())

	comic_data = {
		'id': str(comic_id),
		'title': str(comic.getTitle()),
		'image_alt': str(comic.getImageName()),
		'image_link': str(comic.getImageLink()),
		'original_url': str(base_url + comic_id)
	}
	return comic_data

def parse_id(explanation):
	from urlparse import urlparse
	parsed_url = urlparse(explanation)
	return parsed_url.path[1:] #removes the slash