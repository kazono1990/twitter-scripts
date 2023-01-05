import tweepy


API_KEY = 'xxxxx'
API_KEY_SECRET = 'xxxxx'
BEARER_TOKEN = 'xxxxx'
ACCESS_TOKEN = 'xxxxx'
ACCESS_TOKEN_SECRET = 'xxxxx'


def get_tweepy_client():
    return tweepy.Client(
        bearer_token = BEARER_TOKEN,
        consumer_key = API_KEY,
        consumer_secret = API_KEY_SECRET,
        access_token = ACCESS_TOKEN,
        access_token_secret = ACCESS_TOKEN_SECRET
    )


def get_user_id(client):
    user = client.get_me()
    user_id = user.data.id
    return user_id


def get_following_account_list(client, user_id):
    account_info = client.get_users_following(id=user_id, max_results=1000)
    account_data = account_info.data
    follows = []
    if account_data is not None:
        for account in account_data:
            record = dict(id=account.id, name=account.name)
            follows.append(record)
    return follows


def get_follower_account_list(client, user_id):
    account_info = client.get_users_followers(id=user_id, max_results=1000)
    account_data = account_info.data
    followers = []
    if account_data is not None:
        for account in account_data:
            record = dict(id=account.id, name=account.name)
            followers.append(record)
    return followers


def detect_non_mutual_following_accounts(following_list, follower_list):
    non_mutual_following_account = []
    for account in following_list:
        if account not in follower_list:
            non_mutual_following_account.append(account)
    return non_mutual_following_account


def unfollow_non_mutual_account(client, non_mutual_following_list):
    for account in non_mutual_following_list:
        account_name = account.get('name')
        account_id = account.get('id')
        # print('{} (id: {}) is not following me.'.format(account_name, account_id))
        client.unfollow_user(account_id)
        # print('Successfuly unfollowed (Username: {}, Id: {})'.format(account_name, account_id))


def main():
    client = get_tweepy_client()
    user_id = get_user_id(client)
    following_list = get_following_account_list(client, user_id)
    follower_list = get_follower_account_list(client, user_id)
    # print("Num of followings: ", len(following_list))
    # print("Num of followers: ", len(follower_list))
    non_mutual_following_list = detect_non_mutual_following_accounts(following_list, follower_list)
    # print("Num of non-mutual following account: ", len(non_mutual_following_list))
    unfollow_non_mutual_account(client, non_mutual_following_list)


if __name__ == "__main__":
    main()
