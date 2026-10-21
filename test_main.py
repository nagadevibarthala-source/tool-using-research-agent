
import unittest

from main import parse_agent_decision


class TestParseAgentDecision(unittest.TestCase):

    def test_valid_search_action(self):
        result = parse_agent_decision(
            '{"action": "search_web", "input": " AI agents "}'
        )
        self.assertEqual(
            result,
            {"action": "search_web", "input": "AI agents"},
        )

    def test_valid_finish_action(self):
        result = parse_agent_decision(
            '{"action": "finish", "input": ""}'
        )
        self.assertEqual(result, {"action": "finish", "input": ""})

    def test_invalid_json(self):
        result = parse_agent_decision("not valid JSON")
        self.assertEqual(result, {"action": "finish", "input": ""})

    def test_unsupported_action(self):
        result = parse_agent_decision(
            '{"action": "delete_files", "input": "test"}'
        )
        self.assertEqual(result, {"action": "finish", "input": ""})

    def test_empty_search_query(self):
        result = parse_agent_decision(
            '{"action": "search_web", "input": "   "}'
        )
        self.assertEqual(result, {"action": "finish", "input": ""})

    def test_invalid_fetch_url(self):
        result = parse_agent_decision(
            '{"action": "fetch_webpage_text", "input": "ftp://example.com"}'
        )
        self.assertEqual(result, {"action": "finish", "input": ""})

    def test_non_dictionary_json(self):
        result = parse_agent_decision("[]")
        self.assertEqual(result, {"action": "finish", "input": ""})


if __name__ == "__main__":
    unittest.main(verbosity=2)
