"""for user related operations"""

import datetime
from logging import getLogger
from random import sample

from flask_login import current_user
from sqlalchemy.orm.exc import NoResultFound

from app.main import db
from app.main.models.enums import PriorityType
from app.main.models.payments import Payment
from app.main.models.posts import Post
from app.main.models.tags import Tag
from app.main.models.users import User, userTagJunction

LOG = getLogger(__name__)


TAG_ID_INDEX = 1


class UserService:

    @staticmethod
    def get_by_id(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user is None:
                LOG.info('User with id: {} does not exit'.format(id))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User does not exist'
                }
                return response_object, 300
            return user, 200

        except Exception as e:
            LOG.error('Failed to fetch details for id :{}'.format('id'), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def get_user_feed():
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is None:
                LOG.info(
                    'User with id: {} does not exit'.format(
                        current_user.id))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User does not exist'
                }
                return response_object, 300

            taglist = user.tags
            more = []
            less = []
            neutral = []
            for tag in taglist:
                priority = current_user.getTagPriority(tag)
                if priority == PriorityType.more_of_these:
                    more.append(tag)
                elif priority == PriorityType.less_of_these:
                    less.append(tag)
                else:
                    neutral.append(tag)

            response_list = []

            try:
                response_list.append(
                    sample(Post.getArticlesByTags(more, connector="OR"), 12))
                response_list.append(
                    sample(Post.getArticlesByTags(neutral, connector="OR"), 7))
                response_list.append(
                    sample(Post.getArticlesByTags(less, connector="OR"), 1))
            except BaseException:
                response_list.append(Post.getRandomizedArticles(20))

            return response_list, 200

        except BaseException:
            LOG.error(
                'Failed to fetch feed for id :{}'.format(
                    current_user.id), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def update_user_info(update_dict):
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is None:
                LOG.info(
                    'User with id: {} does not exit'.format(
                        current_user.id))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User does not exist'
                }
                return response_object, 300

            for key in update_dict:
                if key in user.__dict__:
                    user.update_col(key, update_dict[key])

            response_object = {
                'status': 'Success',
                'message': 'Details updated Successfully'
            }
            return response_object, 200

        except Exception as e:
            LOG.error('Failed to update details for id :{}'.format(
                current_user.id), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def save_user_payment(data):
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is None:
                LOG.info(
                    'User with id: {} does not exit'.format(
                        current_user.id))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User does not exist'
                }
                return response_object, 300

            current_user.addPayment(data)
            response_object = {
                'status': 'Success',
                'message': 'Saved the payment into the users information.'
            }
            return response_object, 200

        except BaseException:
            LOG.error('Failed to save payment details for id :{}'.format(
                current_user.id), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def get_user_payment():
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is None:
                LOG.info(
                    'User with id: {} does not exit'.format(
                        current_user.id))
                response_object = {
                    'status': 'Invalid',
                    'message': 'User does not exist'
                }
                return response_object, 300

            return current_user.payments, 200

        except BaseException:
            LOG.error('Failed to get payment details for id :{}'.format(
                current_user.id), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def get_user_tags():
        try:
            try:
                userTagCols = db.session.query(userTagJunction).filter(
                    userTagJunction.c.user_id == current_user.id).all()

            except NoResultFound as _:
                LOG.debug('No tags found for user %s', current_user.id)
                UserTagID = []
            UserTagIDs = [row[TAG_ID_INDEX] for row in userTagCols]
            UserTags = []
            for tagID in UserTagIDs:
                tag = Tag.query.filter_by(id=tagID).first()
                UserTags.append({
                    "id": tag.id,
                    "name": tag.name
                })

            return UserTags, 200

        except BaseException:
            LOG.error('Failed to get tags for user id :{}'.format(
                current_user.id), exc_info=True)
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500
