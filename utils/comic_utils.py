import xkcd

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

def generate_comic_for_mode(current_comic_id, first_comic_id, max_comic_id, mode):
    if mode == 'random':
        comic = xkcd.getRandomComic()
    if mode == 'previous':
        if first_comic_id < current_comic_id < max_comic_id:
            previous_comic_id = int(current_comic_id) - 1
            comic = xkcd.getComic(previous_comic_id)
        else:
            comic = xkcd.getComic(first_comic_id)
    if mode == 'next':
        if first_comic_id <= current_comic_id < max_comic_id:
            next_comic_id = int(current_comic_id) + 1
            comic = xkcd.getComic(next_comic_id)
        else:
            comic = xkcd.getComic(max_comic_id)
    return comic