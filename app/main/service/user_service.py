# for user related operations

import datetime
import traceback
from logging import getLogger
from random import sample

from app.main import db
from app.main.models.enums import PriorityType
from app.main.models.payments import Payment
from app.main.models.posts import Post
from app.main.models.tags import Tag
from app.main.models.users import User, userTagJunction
from flask_login import current_user

LOG = getLogger(__name__)


class UserService:

    @staticmethod
    def get_by_id(data):
        try:
            user = User.query.filter_by(id=data.get('id')).first()
            if user is None:
                LOG.info('User with id: {} does not exit'.format(data.get('id')))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object, 300

            return user,200

        except Exception as e:
            LOG.error('Failed to fetch details for id :{}'.format(data.get('id')))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def get_user_feed():
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is  None:
                LOG.info('User with id: {} does not exit'.format(current_user.id))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object, 300

            taglist = current_user.tag
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

            response_list.append(sample(Post.getArticlesByTags(more, connector="OR"), 12))
            response_list.append(sample(Post.getArticlesByTags(neutral, connector="OR"), 7))
            response_list.append(sample(Post.getArticlesByTags(less, connector="OR"), 1))

            return response_list, 200

        except:
            LOG.error('Failed to fetch feed for id :{}'.format(current_user.id))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500


    @staticmethod
    def update_user_info(data):
        try:
            user = User.query.filter_by(id=current_user.id).first()
            if user is  None:
                LOG.info('User with id: {} does not exit'.format(current_user.id))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object, 300

            for key in update_dict:
                if key in current_user.__dict__:
                    current_user.update_column(key, update_dict[key])

            response_object ={
                'status' : 'Success',
                'message' : 'Details updated Successfully'
            }
            return response_object,200

        except Exception as e:
            LOG.error('Failed to update details for id :{}'.format(current_user.id))
            LOG.debug(traceback.print_exc())
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
                LOG.info('User with id: {} does not exit'.format(current_user.id))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object, 300

            current_user.addPayment(data.get('Payment'))
            response_object ={
                'status' : 'Success',
                'message': 'Saved the payment into the users information.'
            }
            return response_object,200

        except:
            LOG.error('Failed to save payment details for id :{}'.format(current_user.id))
            LOG.debug(traceback.print_exc())
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
                LOG.info('User with id: {} does not exit'.format(current_user.id))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object,300

            return current_user.payments,200

        except:
            LOG.error('Failed to get payment details for id :{}'.format(current_user.id))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500

    @staticmethod
    def get_user_tags():
        try:
            user = userTagJunction.query.filter_by(user_id=current_user.id).first()
            if user is None:
                LOG.info('User with id: {} does not exit'.format(current_user.id))
                response_object ={
                    'status' :'Invalid',
                    'message' : 'User does not exist'
                }
                return response_object,300

            UserTagID = user["keyword_id"]
            UserTags = []
            for tagID in UserTagID:
                tag = Tag.query.filter_by(id=tagID).first()
                UserTags.append(tag)

            return UserTags,200

        except:
            LOG.error('Failed to get tags for user id :{}'.format(current_user.id))
            LOG.debug(traceback.print_exc())
            response_object = {
                'status': 'fail',
                'message': 'Try again',
            }
            return response_object, 500
