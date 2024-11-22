from rest_framework import status, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from users.models import UserDetails, UserToken
import jwt
from django.conf import settings


def response_json(status, detail, data):
    """
    Generate a JSON response dictionary with the specified status, detail, and data.

    Args:
        status (int): HTTP status code.
        detail (str): Detailed message or description.
        data (dict): Additional data to include in the response.

    Returns:
        dict: JSON response dictionary.
    """
    return {
        'status': status,
        'detail': detail,
        'data': data,
    }


class UserTokenAuthentication(TokenAuthentication):
    """
  Custom token-based authentication class for APIs requiring user authentication.

  This class fetch token from request headers and decode email, id from it to match with user table entries. It returns django user object.
  """

    def authenticate(self, request):
        """
      Authenticate the user based on the provided token in the request.

      Args:
          request: The request object.

      Returns:
          tuple: A tuple containing user and token if authentication is successful.

      Raises:
          AuthenticationFailed: If authentication fails, an exception is raised with an appropriate message.
      """
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            msg = Response(data={
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': "Please provide token"
            },
                           status=status.HTTP_401_UNAUTHORIZED)
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = Response(data={
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': "Invalid Token error"
            },
                           status=status.HTTP_401_UNAUTHORIZED)
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = Response(data={
                    'status': status.HTTP_401_UNAUTHORIZED,
                    'message': "Please provide token",
                },
                               status=status.HTTP_401_UNAUTHORIZED)
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = Response(data={
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': "Invalid Token error",
            },
                           status=status.HTTP_401_UNAUTHORIZED)

            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def authenticate_credentials(self, token):
        """
      Authenticate the provided token against the user and token records.

      Args:
          token: The authentication token.

      Returns:
          tuple: A tuple containing user and token if authentication is successful.

      Raises:
          AuthenticationFailed: If authentication fails, an exception is raised with an appropriate message.
      """
        model = self.get_model()
        try:
            payload = jwt.decode(leeway=10,
                                 jwt=token,
                                 key=settings.SECRET_KEY,
                                 algorithms=['HS256'])
            id = payload['id']
            email = payload['email']
            try:
                try:
                    user = UserDetails.objects.get(id=id,
                                                   email=email,
                                                   is_delete=False)
                except:
                    msg = Response(data={
                        'status': status.HTTP_404_NOT_FOUND,
                        'message': "User not found",
                    },
                                   status=status.HTTP_404_NOT_FOUND)
                    raise exceptions.AuthenticationFailed(msg)
                try:
                    user_token = UserToken.objects.get(user=user,
                                                       token=token,
                                                       is_delete=False)
                except:
                    msg = Response(data={
                        'status': status.HTTP_404_NOT_FOUND,
                        'message': "Token not found"
                    },
                                   status=status.HTTP_404_NOT_FOUND)
                    raise exceptions.AuthenticationFailed(msg)

                if str(token) != str(user_token.token):
                    msg = Response(data={
                        'status': status.HTTP_401_UNAUTHORIZED,
                        'message': "Invalid Token"
                    },
                                   status=status.HTTP_401_UNAUTHORIZED)
                    raise exceptions.AuthenticationFailed(msg)

            except UserDetails.DoesNotExist:
                msg = Response(data={
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': "User not found"
                },
                               status=status.HTTP_404_NOT_FOUND)

                raise exceptions.AuthenticationFailed(msg)

        except (jwt.InvalidTokenError, jwt.DecodeError,
                jwt.ExpiredSignatureError):
            msg = Response(data={
                'status': status.HTTP_401_UNAUTHORIZED,
                'message': "Token Expire"
            },
                           status=status.HTTP_401_UNAUTHORIZED)
            raise exceptions.AuthenticationFailed(msg)

        return (user, token)
