from os import getenv
from pyyoutube import Api
from json import dumps

api_key = getenv("ACCESS_TOKEN")
api = Api(api_key=api_key)


def handler(event, context):
    video_id = event["queryStringParameters"]["video_id"]
    video_by_id = (
        api.get_video_by_id(video_id=video_id).items.pop().to_dict()["statistics"]
    )
    _likes = int(video_by_id["likeCount"])
    likes = _likes / 1000 if _likes > 1000 else _likes
    _dislikes = int(video_by_id["dislikeCount"])
    dislikes = _dislikes / 1000 if _dislikes > 1000 else _dislikes
    return {
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "https://www.youtube.com",
            "Access-Control-Allow-Methods": "OPTIONS,GET",
        },
        "statusCode": 200,
        "body": dumps(
            {
                "likes": f"{likes:.1f}K" if _likes > 1000 else likes,
                "dislikes": f"{dislikes:.1f}K" if _dislikes > 1000 else dislikes,
                "likesPercentAge": round((_likes / (_likes + _dislikes)) * 100),
                "dislikesPercentAge": round((_dislikes / (_likes + _dislikes)) * 100),
            }
        ),
    }
