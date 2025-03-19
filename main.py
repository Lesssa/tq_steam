from store import Store
from about import About


def test_about():
    Store.verify_page()
    Store.open_about()
    About.verify_page()
    About.check_stats()


