from requests import Session

class WhatPulse:
	def __init__(self) -> None:
		self.api = "https://api.whatpulse.org"
		self.session = Session()
		self.session.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_team_stats(self, team_name: str) -> dict:
		return self.session.get(
			f"{self.api}/team.php?team={team_name}&format=json").json()

	def get_team_pulse_stats(self, team_name: str) -> dict:
		return self.session.get(
			f"{self.api}/pulses.php?team={team_name}&format=json").json()

	def get_team_pulse_stats(self, user_id: str) -> dict:
		return self.session.get(
			f"{self.api}/pulses.php?user={user_id}&format=json").json()

	def get_user_stats(self, user_id: int) -> dict:
		return self.session.get(
			f"{self.api}/user.php?user={user_id}&format=json").json()
