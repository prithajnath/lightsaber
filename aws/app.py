from os import getenv
from pyyoutube import Api
from json import dumps

api_key = getenv("ACCESS_TOKEN")
api = Api(api_key=api_key)


def format(count: int):
    if count > 1_000_000:
        formatted_count = count / 1_000_000
        if formatted_count == int(formatted_count):
            return f"{int(formatted_count)}M"
        return f"{formatted_count:.1f}M"
    if count > 1000:
        formatted_count = count / 1000
        if formatted_count == int(formatted_count):
            return f"{int(formatted_count)}K"
        return f"{formatted_count:.1f}K"
    return count


def handler(event, context):
    video_id = event["queryStringParameters"]["video_id"]
    video_by_id = (
        api.get_video_by_id(video_id=video_id).items.pop().to_dict()["statistics"]
    )
    _likes = int(video_by_id["likeCount"])
    _dislikes = int(video_by_id["dislikeCount"])
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
                "likes": format(_likes),
                "dislikes": format(_dislikes),
                "likesPercentAge": round((_likes / (_likes + _dislikes)) * 100),
                "dislikesPercentAge": round((_dislikes / (_likes + _dislikes)) * 100),
            }
        ),
    }
