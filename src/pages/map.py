import random

import flet as ft
from flet import map


class MAP:
    choice = random.choice([
        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
        "https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
        "https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
        "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
        "https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"
    ])

class Map(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()
        self.width = page.window.width
        self.height = page.window.height
        self.bgcolor = ft.Colors.WHITE
        self.expand = True

        self.search = ft.SearchBar(
            offset=ft.Offset(x=0, y=-5),
            width=304, height=57,
            bar_bgcolor=ft.Colors.WHITE,
            bar_leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#444E72",
                icon_size=30,
                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT),
                on_click=lambda e: e.page.go("/")
            ),
            bar_trailing=[ft.Icon(name=ft.Icons.MIC, color="#444E72", size=30)],
            bar_shape=ft.RoundedRectangleBorder(radius=15),
            bar_hint_text="Search here",
            bar_hint_text_style=ft.TextStyle(
                size=18,
                font_family="overpass",
                weight=ft.FontWeight.W_400,
                color="#838BAA"
            ),
            view_bgcolor=ft.Colors.WHITE,
            view_leading=ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="#444E72",
                icon_size=30,
                style=ft.ButtonStyle(overlay_color=ft.Colors.TRANSPARENT),
                on_click=lambda e: e.control.parent.close_view()
            ),
            view_trailing=[ft.Icon(name=ft.Icons.MIC, color="#444E72", size=30)],
            view_header_text_style=ft.TextStyle(color="#444E72"),
            view_hint_text="Search here",
            view_hint_text_style=ft.TextStyle(
                size=18,
                font_family="overpass",
                weight=ft.FontWeight.W_400,
                color="#838BAA"
            ),
            view_size_constraints=ft.BoxConstraints(max_height=400, min_width=page.window.width),
            controls=[
                ft.Container(
                    padding=ft.padding.all(value=25),
                    content=ft.Column(
                        controls=[
                            ft.Divider(height=25, color=ft.Colors.WHITE),
                            ft.Text(
                                value="Recent search",
                                size=14,
                                font_family="overpass",
                                weight=ft.FontWeight.BOLD,
                                color="#444E72"
                            ),
                            ft.Divider(height=25, color=ft.Colors.WHITE),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=28,
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.ACCESS_TIME_OUTLINED,
                                                color="#444E72",
                                                size=27
                                            ),
                                            ft.Text(
                                                value="Surabaya",
                                                size=18,
                                                font_family="overpass",
                                                weight=ft.FontWeight.BOLD,
                                                color="#444E72"
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        value="34° / 23°",
                                        size=18,
                                        font_family="overpass",
                                        weight=ft.FontWeight.BOLD,
                                        color="#444E72"
                                    )
                                ]
                            ),
                            ft.Divider(height=25, color=ft.Colors.WHITE),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=28,
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.ACCESS_TIME_OUTLINED,
                                                color="#444E72",
                                                size=27
                                            ),
                                            ft.Text(
                                                value="Surabaya",
                                                size=18,
                                                font_family="overpass",
                                                weight=ft.FontWeight.BOLD,
                                                color="#444E72"
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        value="34° / 23°",
                                        size=18,
                                        font_family="overpass",
                                        weight=ft.FontWeight.BOLD,
                                        color="#444E72"
                                    )
                                ]
                            ),
                            ft.Divider(height=25, color=ft.Colors.WHITE),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        spacing=28,
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.ACCESS_TIME_OUTLINED,
                                                color="#444E72",
                                                size=27
                                            ),
                                            ft.Text(
                                                value="Surabaya",
                                                size=18,
                                                font_family="overpass",
                                                weight=ft.FontWeight.BOLD,
                                                color="#444E72"
                                            )
                                        ]
                                    ),
                                    ft.Text(
                                        value="34° / 23°",
                                        size=18,
                                        font_family="overpass",
                                        weight=ft.FontWeight.BOLD,
                                        color="#444E72"
                                    )
                                ]
                            )
                        ]
                    )
                )
            ],
            on_tap=lambda e: e.control.open_view()
        )

        self.map = map.Map(
            expand=1,
            initial_center=map.MapLatitudeLongitude(34.19, 10.47),
            initial_zoom=6,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            on_init=lambda e: print(f"Initialized Map"),
            layers=[
                map.TileLayer(
                    url_template=MAP.choice,
                    on_image_error=lambda e: print("TileLayer Error")
                )
            ]
        )

        self.content = ft.Stack(
            alignment=ft.alignment.center,
            controls=[
                self.map,
                self.search
            ]
        )
