from game import Game
from store import Store
from topselling import Topselling


def test_more_topsellers():
    Store.verify_page()
    Store.open_topselling()
    Topselling.verify_page()
    Topselling.open_more_topselling()
    Topselling.filter_topselling()
    found_games_info, found_games_real = Topselling.get_results()
    assert found_games_real == found_games_info

    name_search, release_date_search, price_search = Topselling.get_first_game_attr()
    Topselling.open_first_game()
    name, release_date, price = Game.get_attr()
    assert name_search == name and release_date_search == release_date and price_search == price


