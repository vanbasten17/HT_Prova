import xkcd

def get_comic_data(comic):
    """
    Gets the object comic and return the desired attributes for the task.

    Parameters
    ----------
    comic: xkcd.Comic

    Returns
    -------
    Dictionary with necessary attributes.
        
    """
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
    """
    Gets the explanation string of a comic and returns the comic ID.

    Parameters
    ----------
    explanation: string explanation

    Returns
    -------
    String with the parsed ID.

    """
    from urlparse import urlparse
    parsed_url = urlparse(explanation)
    return parsed_url.path[1:] #removes the slash

def generate_comic_for_mode(current_comic_id, first_comic_id, max_comic_id, mode):
    """
    Given the current comic ID plus the limits, do the logic for the different modes defined.

    Modes
    ----------
    'random': gets a comic randomly
    'previous': gets the previous comic_id from the current_comic_id
    'next': gets the next comic_id from the current_comic_id

    Parameters
    ----------
    current_comic_id: current comic
    first_comic_id: lower boundary 
    max_comic_id: upper boundry
    mode: string 

    Returns
    -------
    xkcd.Comic object filled properly

    """
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