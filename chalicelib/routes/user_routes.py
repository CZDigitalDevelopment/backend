from chalice import Blueprint

# from domain.models import user_models
# from domain.database.settings import engine

# from chalicelib.interactors.authenticate_interactor import \
#     AuthenticateInteractor
#
# from sqlalchemy.orm import Session
#
# from domain.schemas.user_schemas import AuthRegister, AuthLogin

# from chalicelib.interactors.post_create_user_interactor import \
#     (PostCreateUserRequestModel,
#      PostCreateUserInteractor)
#
# from chalicelib.interactors.get_read_user_interactor import \
#     (GetReadUserRequestModel,
#      GetReadUserInteractor)
#
# from chalicelib.interactors.post_token_authenticate_interactor import \
#     (PostTokenAuthenticateRequestModel,
#      PostTokenAuthenticateInteractor)


# user_models.Base.metadata.create_all(bind=engine)

users = Blueprint(__name__)


@users.route('/', methods=['GET'])
def teste():
    return {'henrique': 'calenzo'}


# @users.route('/users', methods=['POST'])
# def post_create_user(user: AuthRegister,
# adapter: Session = Depends(UserAlchemyAdapter)):
#     request = PostCreateUserRequestModel(user)
#     interactor = PostCreateUserInteractor(request, adapter)
#
#     result = interactor.run()
#
#     return result()


# @users.route('/users', methods=['GET'])
# def get_read_user(user_id: int = Depends(AuthenticateInteractor().
#                                          auth_wrapper),
#                   adapter: Session = Depends(UserAlchemyAdapter)):
#     request = GetReadUserRequestModel(user_id)
#     interactor = GetReadUserInteractor(request, adapter)
#
#     result = interactor.run()
#
#     return result()
#
#
# @users.route('/auth', methods=['POST'])
# def post_token_authenticate(user: AuthLogin,
#                             adapter: Session = Depends(UserAlchemyAdapter)):
#     request = PostTokenAuthenticateRequestModel(user)
#     interactor = PostTokenAuthenticateInteractor(request, adapter)
#
#     result = interactor.run()
#
#     return result()
