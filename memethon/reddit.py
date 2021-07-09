import sys
import requests


class Post:
    def __init__(self, data: dict):
        self._data = data

        for key, value in self._data.items():
            setattr(self, str(key).lower(), value)

    @property
    def raw_data(self):
        return self._data

    def __eq__(self, other):
        return isinstance(other, Post) and self._data["id"] == other._data["id"]

    def __ne__(self, other):
        return not self.__eq__(other)


class Subreddit(object):
    def __init__(self, data: dict):
        self._data = data

    #
    #     for key, value in self._data.items():
    #         setattr(self, str(key).lower(), value)
    #
    @property
    def raw_data(self):
        return self._data

    # def __eq__(self, other):
    #     return isinstance(other, Post) and self._data["id"] == other._data["id"]
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)


def get_posts_from_subreddit(subreddit: str = "dogecoin", category="", count: int = 10, **kwargs):
    default_agent = "Python ({0.major}.{0.minor}.{0.micro})".format(sys.version_info)
    user_agent = kwargs.get("user_agent", default_agent)
    response = requests.get(f"https://www.reddit.com/r/{subreddit}/{category}.json?count={count}",
                            headers={"User-agent": user_agent})
    for post_data in response.json()['data']['children']:
        yield Post(post_data["data"])


print(list(get_posts_from_subreddit())[0].url)
# for post in get_posts_from_subreddit():
#     print(post.title)
