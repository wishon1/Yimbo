#!/usr/bin/python3
"""
unitest code to test the route file
"""
import unittest
from flask import url_for
from yimbo_appli import app, my_session
from yimbo_appli import Genre, Music

app = app

class TestRoutes(unittest.TestCase):
    """ Test suite for Flask application routes"""
    def setUp(self):
        """set up the test client and the database session"""
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Clean up after testint the route file"""
        pass

    def test_home_route(self):
        """Test the home route"""
        res = self.app.get("/")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"landing_page.html", res.data)

    def test_add_genre_route(self):
        """test the add_genre route"""
        with self.app:
            # simulate a login session
            with self.app.session_transaction() as sess:
                # used a mock user id
                sess["user_id"] = 1

                res = self.app.get('/music_by_genre/1')
                self.assertEqual(res.status_code, 200)
                self.assertIn(b"Index_2.html", res.data)

    def test_create_playlist_route(self):
        """test The create_playlist route"""
        with self.app:
            # Simulate login session
            with self.app.session_transaction() as sess:
            # this is a mock user id
                sess["user_id"] = 1
                
                res = self.app.get('/playlist/create')
                self.assertEqual(res.status_code, 200)
                self.assertIn(b"handle_playlist.html", res.data)

    def test_playlist_details_route(self):
        """Test The playlist details routes"""
        with self.app:
        #simulate a login session
            with self.app.session_transaction() as sess:
                # this is a mock user id
                sess["user_id"] = 1

                res = self.app.get('/playlist/1')
                self.assertEqual(res.status_code, 200)
                self.assertIn(b"playlist_details.html", res.data)


if __name__ == "__main__":
    unittest.main()


