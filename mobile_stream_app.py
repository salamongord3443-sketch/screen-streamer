import threading
import time
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Ваш токен ngrok
NGROK_TOKEN = "3IH93HDfDr9rW7Ycdfk1lLZ5vid_5J3n8o3EHibiFEPhMgMiu"

class StreamApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.status_label = Label(text='Статус: Готов к трансляции', font_size=20)
        self.layout.add_widget(self.status_label)
        
        self.btn = Button(text='Запустить трансляцию', font_size=18, size_hint=(1, 0.3))
        self.btn.bind(on_press=self.toggle_stream)
        self.layout.add_widget(self.btn)
        
        self.is_streaming = False
        return self.layout

    def toggle_stream(self, instance):
        if not self.is_streaming:
            self.is_streaming = True
            self.btn.text = 'Остановить трансляцию'
            self.status_label.text = 'Статус: Трансляция активна!'
            threading.Thread(target=self.stream_loop, daemon=True).start()
        else:
            self.is_streaming = False
            self.btn.text = 'Запустить трансляцию'
            self.status_label.text = 'Статус: Остановлено'

    def stream_loop(self):
        # Здесь будет цикл захвата кадров с экрана Android
        while self.is_streaming:
            # На Android здесь будет вызываться Python-мост к MediaProjection API
            print("Передача кадров экрана на сервер...")
            time.sleep(0.1)

if __name__ == '__main__':
    StreamApp().run()