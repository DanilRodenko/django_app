from django.urls import path
from app.views import btc_sell, eth_sell, doge_sell, main_page, currency, main_menu, test_pandas, \
    news_from_twitter, login_user
urlpatterns = [
    path('btc_price', btc_sell),
    path('eth_price', eth_sell),
    path('doge_price', doge_sell),
    path('main_page', main_page),
    path('currency', currency),
    path('main_menu', main_menu),
    path('test', test_pandas),
    path('news', news_from_twitter),
    path('login', login_user)

]