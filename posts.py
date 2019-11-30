from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
POSTS = {
    "0": {
        "user_name": "Bobby",
        "vote": "Up Vote",
        "timestamp": get_timestamp()
    },
    "1": {
        "user_name": "Dennis",
        "vote": "Down Vote",
        "timestamp": get_timestamp()
    },
    "2": {
        "user_name": "John",
        "vote": "Up Vote",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [POSTS[key] for key in sorted(POSTS.keys())]
