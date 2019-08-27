# endpoint for user operations
from flask import request
from flask_login import current_user, login_required
from flask_restplus import Resource

from app.main.service.user_service import UserService
from app.main.util.dto import AuthDto, PostDto, UserDto

api = UserDto.api
user_auth = AuthDto.user_auth
user = UserDto.user
userInfo = UserDto.userInfo
payment = UserDto.payment
post = PostDto.article


@api.route('/')
class GetUserDetails(Resource):
    """ Fetch details of user by id """
    @api.doc('Endpoint to fetch details of a user by id')
    @api.marshal_with(userInfo, envelope='resource')
    @api.doc(params={'id': 'Id of the requested user'})
    def get(self):
        # Fetching the user id
        return UserService.get_by_id(id=request.args.get('id'))


@api.route('/getFeed')
class GetUserFeed(Resource):
    """ Get the user's feed based on priority of tags """
    @login_required
    @api.doc('Endpoint to get the user\'s feed based on tag priority')
    @api.marshal_list_with(post, envelope='resource')
    def get(self):
        return UserService.get_user_feed()


@api.route("/update")
class UpdateUserInfo(Resource):
    @login_required
    @api.doc(params={"update_dict": "Key value pairs of all update values"})
    @api.expect(userInfo)
    def post(self):
        update_dict = request.json
        return UserService.update_user_info(update_dict)


@api.route("/payment")
class Payment(Resource):
    @login_required
    @api.expect(payment)
    def post(self):
        post_data = request.json
        return UserService.save_user_payment(data=post_data)


@api.route('/get_payment')
class GetPayment(Resource):
    """ Getting the payments of user """
    @login_required
    @api.doc('Endpoint to get the payments done by a user.')
    @api.marshal_list_with(payment, envelope='resource')
    def get(self):
        return UserService.get_user_payment()


@api.route('/followedTags')
class FollowedTags(Resource):
    """ Getting tags followed by user """
    @login_required
    @api.doc('Endpoint to get the tags followed by a user')
    def get(self):
        return UserService.get_user_tags()


@api.route('/savedArticles')
class GetSavedArticles(Resource):
    """ Getting all articles saved by a user """
    @login_required
    @api.marshal_list_with(PostDto.article)
    def get(self):
        s = []
        for save in current_user.saves:
            article = dict()
            article["author_id"] = save.author.id
            article["author"] = save.author.username
            article["tags"] = save.tagDump()
            article["post_id"] = save.post_id
            article["title"] = save.title
            article["body"] = save.body
            article["post_time"] = save.post_time
            article["imgLinks"] = save.linkDump()
            s.append(article)

        return s
