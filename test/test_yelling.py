from test.conftest import MockUQCSBot, TEST_CHANNEL_ID
from unittest.mock import patch


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_minuscule(uqcsbot: MockUQCSBot):
    """
    test minuscule string
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "wintermute")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 2


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_majuscule(uqcsbot: MockUQCSBot):
    """
    test majuscule string
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "WINTERMUTE")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_mixed(uqcsbot: MockUQCSBot):
    """
    test mixed case string
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "wiNTErMUTe")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 2


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: False)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_channel(uqcsbot: MockUQCSBot):
    """
    tests outside of #yeling
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "wintermute")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_thread_discreet_minuscule(uqcsbot: MockUQCSBot):
    """
    test minuscule string reply to thread
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "NEUROMANCER")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1
    thread = float(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])[-1].get('ts', 0))
    uqcsbot.post_message(TEST_CHANNEL_ID, "wintermute", reply_broadcast=False, thread_ts=thread)
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 3


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_thread_discreet_majuscule(uqcsbot: MockUQCSBot):
    """
    test majuscule string reply to thread
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "NEUROMANCER")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1
    thread = float(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])[-1].get('ts', 0))
    uqcsbot.post_message(TEST_CHANNEL_ID, "WINTERMUTE", reply_broadcast=False, thread_ts=thread)
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 2


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_thread_blatant_minuscule(uqcsbot: MockUQCSBot):
    """
    test minuscule string reply to thread and channel
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "NEUROMANCER")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1
    thread = float(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])[-1].get('ts', 0))
    uqcsbot.post_message(TEST_CHANNEL_ID, "wintermute", reply_broadcast=True, thread_ts=thread)
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 3


@patch("uqcsbot.scripts.yelling.in_yelling", new=lambda chan: True)
@patch("uqcsbot.scripts.yelling.is_human", new=lambda chan: True)
def test_thread_blatant_majuscule(uqcsbot: MockUQCSBot):
    """
    test majuscule string reply to thread and channel
    """
    uqcsbot.post_message(TEST_CHANNEL_ID, "NEUROMANCER")
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 1
    thread = float(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])[-1].get('ts', 0))
    uqcsbot.post_message(TEST_CHANNEL_ID, "WINTERMUTE", reply_broadcast=True, thread_ts=thread)
    assert len(uqcsbot.test_messages.get(TEST_CHANNEL_ID, [])) == 2
