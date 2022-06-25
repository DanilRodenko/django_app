from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import *
import requests as rq
import pandas as pd
import tweepy
import config

# Create your views here.

def btc_sell(request):
    lst = []
    for pair in TradingPairs.objects.filter(sell = 'BTC'):
        lst.append(pair.buy)
        lst.append(pair.sell)
    req = rq.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]['sell']
    return HttpResponse(f'{pair.sell}{pair.buy} = {sell_price}')

def eth_sell(request):
    lst = []
    for pair in TradingPairs.objects.filter(sell = 'ETH'):
        lst.append(pair.sell)
        lst.append(pair.buy)
    req = rq.get("https://yobit.net/api/3/ticker/eth_usd")
    response = req.json()
    sell_price = response["eth_usd"]['sell']
    return HttpResponse(f"{pair.sell}{pair.buy} - {sell_price}")

def doge_sell(request):
    lst = []
    for pair in TradingPairs.objects.filter(sell = 'DOGE'):
        lst.append(pair.sell)
        lst.append(pair.buy)
    req = rq.get("https://yobit.net/api/3/ticker/doge_usd")
    response = req.json()
    sell_price = response["doge_usd"]['sell']
    return HttpResponse(f"{pair.sell}{pair.buy} - {sell_price}")

def main_page(request):
    context = {
        'header' : 'DR Crypto Menu',
        'menu' : [
            'BTC',
            'ETH',
            'DOGE'
        ]
    }
    return render(
        request,
        'index.html',
        context
    )

def currency(request):
    req_btc = rq.get("https://yobit.net/api/3/ticker/btc_usd")
    response_btc = req_btc.json()
    sell_btc_price = response_btc["btc_usd"]['sell']
    req_eth = rq.get("https://yobit.net/api/3/ticker/eth_usd")
    response_eth = req_eth.json()
    sell_eth_price = response_eth["eth_usd"]['sell']
    req_doge = rq.get("https://yobit.net/api/3/ticker/doge_usd")
    response_doge = req_doge.json()
    sell_doge_price = response_doge["doge_usd"]['sell']
    req_ltc = rq.get("https://yobit.net/api/3/ticker/ltc_usd")
    response_ltc = req_ltc.json()
    sell_ltc_price = response_ltc["ltc_usd"]["sell"]
    req_xrp = rq.get("https://yobit.net/api/3/ticker/xrp_usd")
    response_xrp = req_xrp.json()
    sell_xrp_price = response_xrp["xrp_usd"]['sell']

    context = {
        'header' : 'Currency',
        'BTCUSD' : sell_btc_price ,
        'ETHUSD' : sell_eth_price,
        'DOGEUSD' : sell_doge_price,
        'LTCUSD' : sell_ltc_price,
        'XRPUSD' : sell_xrp_price
    }
    return render(
        request,
        'currency.html',
        context
    )

def main_menu(request):
    return render(
        request,
        'main_menu.html'
    )

def test_pandas(request):
    data = pd.read_csv('/Users/danil/PycharmProjects/DS_HomeWork4/adult.data.csv')
    male = data[(data['sex'] == 'Male')]
    context = {
        'male' : male.head()
    }
    return render(
        request,
        'news.html',
        context
    )

def news_from_twitter(request):
    try:
        api_key = config.api_key
        api_key_secret = config.api_key_secret

        access_token = config.access_token
        access_token_secret = config.access_token_secret

        #authentication

        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        public_tweets = api.home_timeline()

        columns = ['Time', 'User', 'Tweet']
        data = []
        for tweet in public_tweets:
            data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

        df = pd.DataFrame(data, columns=columns)
        df_fork_log = df[(df['User'] == 'ForkLog')]

        context = {
            'header': 'NEWS',
            'news': [
                df_fork_log['Tweet'].iloc[0],
                df_fork_log['Tweet'].iloc[1],
                df_fork_log['Tweet'].iloc[2],
                df_fork_log['Tweet'].iloc[3],
                df_fork_log['Tweet'].iloc[4],
                df_fork_log['Tweet'].iloc[5],
                df_fork_log['Tweet'].iloc[6],
                df_fork_log['Tweet'].iloc[7]
            ]
        }
        return render(
            request,
            'news.html',
            context
        )
    except tweepy.errors.TweepyException:
        # return render(request, 'main_menu.html')
        return HttpResponse('On vpn')

##login
def login_user(request):
    user = authenticate(
        username = request.POST['username'],
        password = request.POST['password']
    )
    if user is None:
        return render(request, 'error_login.html', {})
    else:
        return HttpResponseRedirect('main_menu')

