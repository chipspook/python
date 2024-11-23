import pytest
from television import Television

def test_power():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Wraps back to MIN_CHANNEL
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"
    tv.volume_up()
    tv.volume_up()  # MAX_VOLUME reached
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"
    tv.volume_up()  # Should stay at MAX_VOLUME
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"  # Muted
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"  # Unmuted
