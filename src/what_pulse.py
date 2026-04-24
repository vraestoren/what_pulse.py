from requests import Session

class WhatPulse:
	def __init__(self) -> None:
		self.api = "https://api.whatpulse.org"
		self.session = Session()
		self.session.headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

	def _get(self, endpoint: str, params: dict = None) -> dict:
		return self.session.get(
			f"{self.api}{endpoint}", params=params or {}).json()

	def _build_params(self, **kwargs) -> dict:
		return {key: value for key, value in kwargs.items() if value is not None}

	def get_user_stats(
			self,
			user: str) -> dict:
		params = self._build_params(user=user, format="json")
		return self._get("/user.php", params)

	def get_user_pulse_stats(
			self,
			user: str) -> dict:
		params = self._build_params(user=user, format="json")
		return self._get("/pulses.php", params)

	def get_team_stats(
			self,
			team: str) -> dict:
		params = self._build_params(team=team, format="json")
		return self._get("/team.php", params)

	def get_team_pulse_stats(
			self,
			team: str) -> dict:
		params = self._build_params(team=team, format="json")
		return self._get("/pulses.php", params)
