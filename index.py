from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout

class WidgetsExample(BoxLayout):
	count = 0
	count_text = StringProperty("0")
	def on_button_click(self):
		self.count += 1
		self.count_text = str(self.count)

class MarchApp(App):
	pass

if __name__ == '__main__':
	MarchApp().run()