# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import os


class ProxyCommand(sublime_plugin.WindowCommand):
	''' set proxy for current session'''

	options = ['Proxy', 'No Proxy', 'List Current Proxy']

	def display_list(self):
		self.window.show_quick_panel(self.options, self.on_done)

	def list_current_proxy(self):
		print('Current Proxy...')
		if 'HTTP_PROXY' in os.environ:
			print('HTTP_PROXY:', os.environ['HTTP_PROXY'])
		if 'HTTPS_PROXY' in os.environ:
			print('HTTPS_PROXY:', os.environ['HTTPS_PROXY'])

	def on_done(self, index):
		sublime.active_window().run_command("show_panel", {"panel": "console", "toggle": True})
		if index == 0:
			print('Set Proxy...')
			# replace with your own proxy.
			os.environ['HTTP_PROXY'] = 'http://proxy.xx.com:8080'
			os.environ['HTTPS_PROXY'] = 'http://proxy.xx.com:8080'
			self.list_current_proxy()
		elif index == 1:
			print('Unset Proxy...')
			if 'HTTP_PROXY' in os.environ:
				del os.environ['HTTP_PROXY']
			if 'HTTPS_PROXY' in os.environ:
				del os.environ['HTTPS_PROXY']
		else:
			self.list_current_proxy()

	def run(self):
		self.display_list()
