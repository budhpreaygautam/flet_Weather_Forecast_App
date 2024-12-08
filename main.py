import flet
from flet import *
import requests
import datetime

api_key = '64344d3ce6a0497999b174524240812'
location = "new delhi"
api_url = f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days=7&aqi=no&alerts=no"

# Fetch weather data from the API
response = requests.get(api_url)
weather_data = response.json()

# Weekday names
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def main(page: Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _expand(e):
        if e.data == "true":
            _c.content.controls[1].height = 560
            _c.content.controls[1].update()
        else:
            _c.content.controls[1].height = 660 * 0.40
            _c.content.controls[1].update()

    def _current_temp():
        current_temp = int(weather_data["current"]["temp_c"])
        current_condition = weather_data["current"]["condition"]["text"]
        current_icon = "https:" + weather_data["current"]["condition"]["icon"]
        wind_speed = int(weather_data["current"]["wind_kph"])
        humidity = int(weather_data["current"]["humidity"])
        feels_like = int(weather_data["current"]["feelslike_c"])

        return [current_temp, current_condition, current_icon, wind_speed, humidity, feels_like]

    def _current_extra():
        visibility = int(weather_data["current"]["vis_km"])
        pressure = round(weather_data["current"]["pressure_mb"] * 0.03, 2)
        sunset = weather_data["forecast"]["forecastday"][0]["astro"]["sunset"]
        sunrise = weather_data["forecast"]["forecastday"][0]["astro"]["sunrise"]

        extra_info = [
            [visibility, "Km", "Visibility", "https://cdn-icons-png.flaticon.com/512/414/414974.png"],
            [pressure, "inHg", "Pressure", "https://cdn-icons-png.flaticon.com/512/414/414927.png"],
            [sunset, "", "Sunset", "https://cdn-icons-png.flaticon.com/512/869/869869.png"],
            [sunrise, "", "Sunrise", "https://cdn-icons-png.flaticon.com/512/869/869869.png"],
        ]

        return [
            Container(
                bgcolor="white10",
                border_radius=12,
                alignment=alignment.center,
                content=Column(
                    alignment='center',
                    horizontal_alignment='center',
                    spacing=25,
                    controls=[
                        Container(
                            alignment=alignment.center,
                            content=Image(
                                src=data[3],
                                color='white',
                            ),
                            width=32,
                            height=32,
                        ),
                        Container(
                            content=Column(
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=0,
                                controls=[
                                    Text(
                                        str(data[0]) + " " + data[1],
                                        size=14,
                                    ),
                                    Text(
                                        data[2],
                                        size=11,
                                        color='white54',
                                    ),
                                ],
                            )
                        )
                    ],
                ),
            ) for data in extra_info
        ]

    def _top():
        today = _current_temp()

        today_extra = GridView(
            max_extent=150,
            expand=1,
            run_spacing=5,
            spacing=5,
        )
        for info in _current_extra():
            today_extra.controls.append(info)

        top = Container(
            width=350,
            height=660 * 0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.bottom_right,
                colors=["lightblue600", "lightblue900"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=450, curve="decelerate"),
            on_hover=lambda e: _expand(e),
            padding=15,
            content=Column(
                alignment='start',
                spacing=10,
                controls=[
                    Row(
                        alignment="center",
                        controls=[
                            Text(
                                "New Delhi, IN",
                                size=16,
                                weight="w500",
                            ),
                        ],
                    ),
                    Container(padding=padding.only(bottom=5)),
                    Row(
                        alignment="center",
                        spacing=30,
                        controls=[
                            Column(
                                controls=[
                                    Container(
                                        width=90,
                                        height=90,
                                        content=Image(
                                            src=today[2],
                                            fit="contain"
                                        )
                                    ),
                                ]
                            ),
                            Column(
                                spacing=5,
                                horizontal_alignment='center',
                                controls=[
                                    Text(
                                        "Today",
                                        size=12,
                                        text_align='center',
                                    ),
                                    Row(
                                        vertical_alignment="start",
                                        spacing=0,
                                        controls=[
                                            Container(
                                                content=Text(
                                                    today[0],
                                                    size=52,
                                                ),
                                            ),
                                            Container(
                                                content=Text(
                                                    "\u00b0",
                                                    size=28,
                                                    text_align="center",
                                                )
                                            ),
                                        ],
                                    ),
                                    Text(
                                        today[1],
                                        size=10,
                                        color="white54",
                                        text_align="center",
                                    )
                                ],
                            ),
                        ],
                    ),
                    Divider(height=8, thickness=1, color="white10"),
                    Row(
                        alignment="spaceAround",
                        controls=[
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="https://cdn-icons-png.flaticon.com/512/869/869869.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[3]) + " Km/h",
                                            size=11,
                                        ),
                                        Text(
                                            "Wind",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="https://cdn-icons-png.flaticon.com/512/414/414974.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[4]) + " %",
                                            size=11,
                                        ),
                                        Text(
                                            "Humidity",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                            Container(
                                content=Column(
                                    horizontal_alignment="center",
                                    spacing=2,
                                    controls=[
                                        Container(
                                            alignment=alignment.center,
                                            content=Image(
                                                src="https://cdn-icons-png.flaticon.com/512/869/869869.png",
                                                color="white",
                                            ),
                                            width=20,
                                            height=20,
                                        ),
                                        Text(
                                            str(today[5]) + "\u00b0",
                                            size=11,
                                        ),
                                        Text(
                                            "Feels Like",
                                            size=9,
                                            color="white54",
                                        ),
                                    ],
                                )
                            ),
                        ],
                    ),
                    today_extra,
                ],
            ),
        )
        return top

    def _bot_data():
        forecast = weather_data["forecast"]["forecastday"]
        bot_data = []
        for day in forecast:
            date = datetime.datetime.strptime(day["date"], "%Y-%m-%d")
            weekday = days[date.weekday()]
            condition = day["day"]["condition"]["text"]
            icon_url = "https:" + day["day"]["condition"]["icon"]
            temp_max = int(day["day"]["maxtemp_c"])
            temp_min = int(day["day"]["mintemp_c"])
            bot_data.append(
                Row(
                    spacing=5,
                    alignment='spaceBetween',
                    controls=[
                        Row(
                            expand=1,
                            alignment='start',
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Text(weekday)
                                )
                            ]
                        ),
                        Row(
                            expand=1,
                            controls=[
                                Container(
                                    content=Row(
                                        alignment='start',
                                        controls=[
                                            Container(
                                                width=20,
                                                height=20,
                                                alignment=alignment.center_left,
                                                content=Image(
                                                    src=icon_url
                                                ),
                                            ),
                                            Text(
                                                condition,
                                                size=11,
                                                color='white54',
                                                text_align='center',
                                            )
                                        ]
                                    )
                                )
                            ]
                        ),
                        Row(
                            expand=1,
                            alignment='end',
                            controls=[
                                Container(
                                    alignment=alignment.center,
                                    content=Row(
                                        alignment='center',
                                        spacing=5,
                                        controls=[
                                            Container(
                                                width=25,
                                                content=Text(
                                                    f"{temp_max}\u00b0",
                                                    text_align="start",
                                                )
                                            ),
                                            Container(
                                                width=25,
                                                content=Text(
                                                    f"{temp_min}\u00b0",
                                                    text_align="end",
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    ]
                )
            )
        return bot_data

    def _bottom():
        bot_column = Column(
            alignment='center',
            horizontal_alignment="center",
            spacing=25,
        )
        for data in _bot_data():
            bot_column.controls.append(data)

        bottom = Container(
            padding=padding.only(top=280, left=20, right=20, bottom=20),
            content=bot_column,
        )

        return bottom

    _c = Container(
        width=350,
        height=660,
        border_radius=35,
        bgcolor='black',
        padding=10,
        content=Stack(
            width=300, height=550,
            controls=[
                _bottom(),
                _top(),
            ],
        ),
    )
    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
