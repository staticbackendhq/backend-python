import os
import unittest

from staticbackend import StaticBackend, Config
from staticbackend.errors import EmailError, LoginError, RecordNotFoundError


class TestStaticBackend(unittest.TestCase):
    def setUp(self) -> None:
        try:
            self.config = Config(
                api_token=os.environ["KEY"],
                root_token=os.environ["ROOT"],
                endpoint=os.environ["ENDPOINT"],
            )
        except:
            self.skipTest("Missing environment variables.")
        self.backend = StaticBackend(self.config)
        super().setUp()

    def test_user(self) -> None:
        """Test user management operations."""

        # If user login fails, an exception is raised.
        with self.assertRaises(LoginError):
            self.backend.user.login("notexists@foo.com", "bar")
        # When login success, the user jwt token is returned.
        state = self.backend.user.login(os.environ["EMAIL"], os.environ["PASSWORD"])
        self.assertRegex(
            state.token, r"^[a-zA-Z0-9_=]+.[a-zA-Z0-9_=]+.[a-zA-Z0-9_\+\-\/=]+$"
        )

        # Create existing user.
        with self.assertRaises(EmailError):
            self.backend.user.register(os.environ["EMAIL"], os.environ["PASSWORD"])

        # Reset password and login
        code = self.backend.user.send_reset_code(os.environ["EMAIL"])
        self.assertRegex(code, "^[a-zA-Z0-9]+$")
        result = self.backend.user.reset_password(
            os.environ["EMAIL"], code, os.environ["PASSWORD"] + "123"
        )
        self.assertTrue(result)
        state = self.backend.user.login(
            os.environ["EMAIL"], os.environ["PASSWORD"] + "123"
        )
        self.assertRegex(
            state.token, r"^[a-zA-Z0-9_=]+.[a-zA-Z0-9_=]+.[a-zA-Z0-9_\+\-\/=]+$"
        )
        code = self.backend.user.send_reset_code(os.environ["EMAIL"])
        self.backend.user.reset_password(
            os.environ["EMAIL"], code, os.environ["PASSWORD"]
        )

    def test_database(self) -> None:
        """Test database management operations."""
        state = self.backend.user.login(os.environ["EMAIL"], os.environ["PASSWORD"])
        # Reading from non-existent database.
        docs = state.database.list_documents("none_exists")
        self.assertEqual(docs.total, 0)

        # Operations on documents.
        db = "test_data"
        test_doc = {"foo": "baz"}
        updated_doc = {"foo": "bazbaz", "baz": "foo"}

        # Make sure document records does not exist.
        docs = state.database.list_documents(db)
        if docs.total > 0:
            for doc in docs.results:
                state.database.delete_document(db, doc["id"])

        # Creating a new record.
        doc = state.database.create_document(db, test_doc)
        self.assertEqual(doc, {**doc, **test_doc})
        # Updating the record.
        doc = state.database.update_document(db, doc["id"], updated_doc)
        self.assertEqual(doc, {**doc, **updated_doc, **{"id": doc["id"]}})
        # Reading the record.
        doc = state.database.get_document(db, doc["id"])
        self.assertEqual(doc, {**doc, **updated_doc, **{"id": doc["id"]}})
        # Listing records.
        docs = state.database.list_documents(db)
        self.assertEqual(docs.total, 1)
        self.assertEqual(docs.results[0], doc)
        # Deleting the record.
        count = state.database.delete_document(db, doc["id"])
        self.assertEqual(count, 1)
        docs = state.database.list_documents(db)
        self.assertEqual(docs.total, 0)

        # Reading a non-existent record.
        with self.assertRaises(RecordNotFoundError):
            state.database.get_document(db, doc["id"])
        # Updating a non-existent record.
        with self.assertRaises(RecordNotFoundError):
            state.database.update_document(db, doc["id"], updated_doc)
        # Deleting a non-existent record.
        count = state.database.delete_document(db, doc["id"])
        self.assertEqual(count, 0)

    def test_storage(self):
        state = self.backend.user.login(os.environ["EMAIL"], os.environ["PASSWORD"])
        self.assertRegex(
            state.token, r"^[a-zA-Z0-9_=]+.[a-zA-Z0-9_=]+.[a-zA-Z0-9_\+\-\/=]+$"
        )
        result = state.storage.upload_file(".gitignore")
        self.assertNotEqual(result["id"], "")
        self.assertNotEqual(result["url"], "")

        with open(".gitignore", "rb") as f:
            result = state.storage.upload(f, ".gitignore")
            print(result)
            self.assertNotEqual(result["id"], "")
            self.assertNotEqual(result["url"], "")
