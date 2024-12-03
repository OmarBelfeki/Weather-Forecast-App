import flet as ft


class Detail(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()

        page.theme = ft.Theme(
            scrollbar_theme=ft.ScrollbarTheme(
                track_visibility=True,
                track_color=ft.Colors.TRANSPARENT,
                track_border_color=ft.Colors.WHITE,
                thumb_visibility=True,
                thumb_color=ft.Colors.WHITE,
                min_thumb_length=125,
                radius=15,
                thickness=5,
            )
        )

        self.padding = ft.padding.only(top=35, left=25, right=25)
        self.expand = True
        self.bgcolor = "#47B3E7"
        self.image = ft.DecorationImage(
            src="/images/home.png",
            fit=ft.ImageFit.FILL
        )

        self.head = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        ft.IconButton(
                            content=ft.Icon(
                                name=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                                size=20,
                                color=ft.Colors.WHITE
                            ),
                            on_click=lambda e: e.page.go("/")
                        ),
                        ft.Text(
                            value="Back",
                            size=24,
                            font_family="overpass",
                            weight=ft.FontWeight.W_400,
                            color=ft.Colors.WHITE
                        )
                    ]
                ),
                ft.IconButton(
                    content=ft.Icon(
                        name=ft.Icons.SETTINGS_OUTLINED,
                        color=ft.Colors.WHITE,
                        size=24
                    )
                )
            ]
        )

        self.content = ft.Column(
            controls=[
                self.head,
                ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value="Today",
                            size=24,
                            font_family="overpass",
                            weight=ft.FontWeight.W_700,
                            color=ft.Colors.WHITE
                        ),
                        ft.Text(
                            value="Sep, 12",
                            size=18,
                            font_family="overpass",
                            weight=ft.FontWeight.W_300,
                            color=ft.Colors.WHITE
                        )
                    ]
                ),
                ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=5,
                    controls=[
                        ft.Container(
                            height=140,
                            content=ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        value=f"{29-i}°C",
                                        size=18,
                                        font_family="overpass",
                                        weight=ft.FontWeight.W_400,
                                        color=ft.Colors.WHITE
                                    ),
                                    ft.Image(
                                        src="/images/sol.png",
                                        width=43, height=43.67,
                                        scale=1.5
                                    ),
                                    ft.Text(
                                        value=f"1{4+i}.00",
                                        size=18,
                                        font_family="overpass",
                                        weight=ft.FontWeight.W_400,
                                        color=ft.Colors.WHITE
                                    )
                                ]
                            ),
                            on_click=self.__changed
                        )
                        for i in range(1, 6)
                    ]
                ),
                ft.Divider(height=12, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text(
                            value="Next Forecast",
                            size=24,
                            font_family="overpass",
                            weight=ft.FontWeight.W_900,
                            color=ft.Colors.WHITE
                        ),
                        ft.IconButton(
                            content=ft.Icon(
                                name=ft.Icons.CALENDAR_MONTH_OUTLINED,
                                color=ft.Colors.WHITE,
                                size=30
                            )
                        )
                    ]
                ),
                ft.Column(
                    scroll=ft.ScrollMode.ALWAYS,
                    height=250, width=350,
                    controls=[
                        ft.Row(
                            width=270,
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    value="Sep, 13",
                                    size=18,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_400,
                                    color=ft.Colors.WHITE
                                ),
                                ft.Image(
                                    src="/images/sol.png",
                                    width=43, height=43.67,
                                    scale=1.5
                                ),
                                ft.Text(
                                    value="21°",
                                    size=18,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_400,
                                    color=ft.Colors.WHITE
                                )
                            ]
                        )
                        for i in range(7)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                    controls=[
                        ft.Icon(
                            name=ft.Icons.SUNNY,
                            color=ft.Colors.WHITE,
                            size=24
                        ),
                        ft.Text(
                            value="AccWeather",
                            size=18,
                            font_family="overpass",
                            weight=ft.FontWeight.W_400,
                            color=ft.Colors.WHITE,
                            offset=(0, 0.1)
                        )
                    ]
                )
            ]
        )

    @staticmethod
    def __changed(e: ft.ControlEvent) -> None:
        e.control.alignment = ft.alignment.center
        e.control.width = 60
        e.control.height = 140
        e.control.border_radius = ft.border_radius.all(value=20)
        e.control.bgcolor = ft.Colors.with_opacity(opacity=0.2, color=ft.Colors.WHITE)
        e.control.parent.update()

        for i in e.control.parent.controls:
            if e.page.get_control(i.uid) != e.page.get_control(e.control.uid):
                e.control.data = None
                e.control.alignment = None
                e.control.width = None
                e.control.border_radius = None
                e.control.bgcolor = None
