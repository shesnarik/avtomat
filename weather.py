import flet as ft
from flet import *
import requests

def main(page: ft.Page):
    page.title = "Погодная программа"
    page.theme_mode = 'dark'
    page.vertical_aligment = ft.MainAxisAlignment.CENTER
    img = ft.Image(
        src=f"priora2.png",
        width=1500,
        height=100,
        fit=ft.ImageFit.CONTAIN,

    )
    images = ft.Row(expand=1, wrap=False)

    page.add(img, images)

    for i in range(0, 100):
        images.controls.append(
            ft.Image(
                src=f"priora2.png{i}",
                width=200,
                height=100,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(15),
        )
    )

    user_data = ft.TextField(label='Введите город', width=400, height=300)
    weather_data = ft.Text('')
    weather_cloud = ft.Text('')
    weather_wind = ft.Text('')
    weather_pressure = ft.Text('')

    def get_info(e):
        if len(user_data.value) < 1:
            return

        API = 'd83c50bc1064a67b7b55fd196c37623f'
        URL = f'https://api.openweathermap.org/data/2.5/weather?q={user_data.value}&appid={API}&units=metric&lang=RU'
        res = requests.get(URL).json()
        temp = res['main']['temp']
        wind = res['wind']['speed']
        cloud = res['weather'][0]['description']
        pressure = res['main']['pressure']
        weather_data.value = 'Температура: ' + str(temp)
        weather_cloud.value = 'Облачность:  ' + str(cloud)
        weather_wind.value = 'Скорость ветра: ' + str(wind) + ' м/с'
        weather_pressure.value = 'Давление: ' + str(pressure) + ' мм.рт.ст.'
        page.update()
        print(res)



    def change_them(e):

        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.SUNNY, on_click=change_them),
                ft.Text('Погодная программа')
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([user_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_data], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_cloud], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_wind], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([weather_pressure], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([ft.ElevatedButton(text='Получить', on_click=get_info)],alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)
