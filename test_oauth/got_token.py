from flask_oauth import OAuth

# Create the Flask-OAuth's instance
oauth = OAuth()

# facebook 第三方登录接口
# Create the auth object for facebook.
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='<Your_app_number>',
    consumer_secret='<Your_app_secret>',
    request_token_params={'scope': 'email'})

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_oauth_token')