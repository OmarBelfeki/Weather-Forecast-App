import flet as ft

class Notif(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()

        self.padding = ft.padding.only(left=20, right=20)
        self.border_radius = ft.border_radius.only(top_right=30, top_left=30)
        self.bgcolor = ft.Colors.WHITE

        self.content = ft.Column(
            width=page.width,
            controls=[
                ft.Text( # 0
                    value="Your notification",
                    font_family="overpass",
                    size=25,
                    color="#444E72",
                    weight=ft.FontWeight.W_900,
                    style=ft.TextStyle(
                        shadow=[
                            ft.BoxShadow(
                                blur_radius=50,
                                offset=(-4, 8),
                                color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.BLACK),
                            ),
                            ft.BoxShadow(
                                blur_radius=6,
                                offset=(2, -3),
                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.BLACK),
                                blur_style=ft.ShadowBlurStyle.INNER
                            ),
                            ft.BoxShadow(
                                blur_radius=4,
                                offset=(-6, 4),
                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.WHITE),
                                blur_style=ft.ShadowBlurStyle.INNER
                            )
                        ]
                    )
                ),
                ft.Divider(height=5, color=ft.Colors.TRANSPARENT), # 1
                ft.Text(  # 2
                    value="New",
                    color="#444E72",
                    size=13,
                    weight=ft.FontWeight.W_300,
                ),
                ft.Container( # 3
                    data="1",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            #ft.Container(image_src="/icons/sun.png", width=24, height=24, bgcolor="red"),
                            ft.Icon(name=ft.Icons.SUNNY, color="#444E72"),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="10 minutes ago",
                                        color="#444E72",
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_400,
                                    ),
                                    ft.Text(
                                        value="A sunny day in your location, consider \nwearing your UV protection",
                                        color="#444E72",
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_700,
                                    ),
                                ]
                            ),
                            ft.Icon(name=ft.Icons.KEYBOARD_ARROW_DOWN, color="#444E72")
                        ]
                    ),
                    on_click=self.selected
                ),
                ft.Divider(height=5, color=ft.Colors.TRANSPARENT), # 4
                ft.Text( # 5
                    value="Earlier",
                    color="#444E72",
                    size=13,
                    weight=ft.FontWeight.W_300,
                ),
                ft.Container( # 6
                    data="2",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Icon(name=ft.Icons.WIND_POWER, color=ft.Colors.with_opacity(opacity=0.7, color="#444E72")),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="1 day ago",
                                        color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"),
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_400,
                                    ),
                                    ft.Text(
                                        value="A cloudy day will occur all day long, \ndon't worry about the heat of the sun",
                                        color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"),
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_700,
                                    ),
                                ]
                            ),
                            ft.Icon(name=ft.Icons.KEYBOARD_ARROW_DOWN, color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"))
                        ]
                    ),
                    on_click=self.selected
                ),
                ft.Container( # 7
                    data="3",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Icon(name=ft.Icons.CLOUD_OUTLINED, color=ft.Colors.with_opacity(opacity=0.7, color="#444E72")),
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        value="2 day ago",
                                        color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"),
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_400,
                                    ),
                                    ft.Text(
                                        value="Potential for rain today is 84%, don't \nforget to bring your umbrella.",
                                        color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"),
                                        font_family="overpass",
                                        size=13,
                                        weight=ft.FontWeight.W_700,
                                    ),
                                ]
                            ),
                            ft.Icon(name=ft.Icons.KEYBOARD_ARROW_DOWN, color=ft.Colors.with_opacity(opacity=0.7, color="#444E72"))
                        ]
                    ),
                    on_click=self.selected
                )
            ]
        )

    @staticmethod
    def selected(e: ft.ControlEvent) -> None:
        if e.control.content.controls[0].color == "#444E72":
            e.control.content.controls[0].color = ft.Colors.with_opacity(opacity=0.7, color="#444E72")
            e.control.content.controls[1].controls[0].color = ft.Colors.with_opacity(opacity=0.7, color="#444E72")
            e.control.content.controls[1].controls[1].color = ft.Colors.with_opacity(opacity=0.7, color="#444E72")
            e.control.content.controls[2].color = ft.Colors.with_opacity(opacity=0.7, color="#444E72")
        else:
            e.control.content.controls[0].color = "#444E72"
            e.control.content.controls[1].controls[0].color = "#444E72"
            e.control.content.controls[1].controls[1].color = "#444E72"
            e.control.content.controls[2].color = "#444E72"
        e.control.update()

class Home(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        super().__init__()

        self.padding = ft.padding.only(top=15, left=25, right=25)
        self.expand = True
        self.bgcolor = "#47B3E7"
        self.image = ft.DecorationImage(
            src="/images/home.png",
            fit=ft.ImageFit.FILL
        )

        self.sol = ft.Container(
            image_src="/images/sol.png",
            margin=ft.margin.only(left=30),
            width=237, height=197
        )

        self.header = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Row(
                                controls=[
                                    ft.Image(
                                        src="/icons/map.png",
                                        width=24, height=24
                                    ),
                                    ft.Text(
                                        value="Semarang",
                                        color=ft.Colors.WHITE,
                                        size=24,
                                        font_family="overpass"
                                    )
                                ]
                            ),
                            on_click=lambda e: e.page.go("/map")
                        ),
                        ft.Image(
                            src="/icons/opt.png",
                            width=24, height=24
                        )
                    ]
                ),
                ft.Image(
                    src="/icons/notif.png",
                    badge="15",
                )
            ]
        )

        self.content = ft.SafeArea(
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.header,
                    ft.Image(
                        src="/images/SUN.png",
                        width=141, height=141
                        #scale=0.5
                    ),
                    ft.Container(
                        width=353, height=340,
                        padding=ft.padding.all(value=15),
                        bgcolor=ft.Colors.with_opacity(opacity=0.3, color=ft.Colors.WHITE),
                        blur=2.5,
                        border=ft.border.all(width=1, color=ft.Colors.WHITE),
                        border_radius=ft.border_radius.all(value=20),
                        margin=ft.margin.only(top=0),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="Today, 12 September",
                                    size=18,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_600,
                                    style=ft.TextStyle(
                                        shadow=[
                                            ft.BoxShadow(
                                                blur_radius=2,
                                                offset=(-1, 1),
                                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.WHITE),
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            ),
                                            ft.BoxShadow(
                                                blur_radius=1,
                                                offset=(-2, 3),
                                                color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.BLACK),
                                            )
                                        ]
                                    )
                                ),
                                ft.Text(
                                    value="29",
                                    size=100,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_400,
                                    style=ft.TextStyle(
                                        shadow=[
                                            ft.BoxShadow(
                                                blur_radius=50,
                                                offset=(-4, 8),
                                                color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.BLACK),
                                            ),
                                            ft.BoxShadow(
                                                blur_radius=6,
                                                offset=(2, -3),
                                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.BLACK),
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            ),
                                            ft.BoxShadow(
                                                blur_radius=4,
                                                offset=(-6, 4),
                                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.WHITE),
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            )
                                        ]
                                    ),
                                    spans=[
                                        ft.TextSpan(
                                            text="°",
                                            style=ft.TextStyle(
                                                size=72,
                                                shadow=[
                                                    ft.BoxShadow(
                                                        blur_radius=50,
                                                        offset=(-4, 8),
                                                        color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.BLACK),
                                                    ),
                                                    ft.BoxShadow(
                                                        blur_radius=6,
                                                        offset=(2, -3),
                                                        color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.BLACK),
                                                        blur_style=ft.ShadowBlurStyle.INNER
                                                    ),
                                                    ft.BoxShadow(
                                                        blur_radius=4,
                                                        offset=(-6, 4),
                                                        color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.WHITE),
                                                        blur_style=ft.ShadowBlurStyle.INNER
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                ),
                                ft.Text(
                                    value="Cloudy",
                                    size=35,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_400,
                                    style=ft.TextStyle(
                                        shadow=[
                                            ft.BoxShadow(
                                                blur_radius=50,
                                                offset=(-4, 8),
                                                color=ft.Colors.with_opacity(opacity=0.1, color=ft.Colors.BLACK),
                                            ),
                                            ft.BoxShadow(
                                                blur_radius=6,
                                                offset=(2, -3),
                                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.BLACK),
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            ),
                                            ft.BoxShadow(
                                                blur_radius=4,
                                                offset=(-6, 4),
                                                color=ft.Colors.with_opacity(opacity=0.25, color=ft.Colors.WHITE),
                                                blur_style=ft.ShadowBlurStyle.INNER
                                            )
                                        ]
                                    )
                                ),
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(src="/icons/windy.png"),
                                        ft.Text(
                                            value="Wind   |   10 km/h",
                                            size=18,
                                            font_family="overpass",
                                            weight=ft.FontWeight.W_400,
                                        )
                                    ]
                                ),
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Image(src="/icons/hum.png"),
                                        ft.Text(
                                            value="Hum    |   54 %     ",
                                            size=18,
                                            font_family="overpass",
                                            weight=ft.FontWeight.W_400,
                                        )
                                    ]
                                )
                            ]
                        ),
                        on_click=lambda e: e.page.go("/detail")
                    ),
                    ft.Divider(height=7, color=ft.Colors.TRANSPARENT),
                    ft.Container(
                        width=220, height=64,
                        border_radius=ft.border_radius.all(value=20),
                        bgcolor=ft.Colors.WHITE,
                        content=ft.Row(
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text(
                                    value="Forecast report",
                                    size=18,
                                    font_family="overpass",
                                    weight=ft.FontWeight.W_400,
                                    color="#444E72"
                                ),
                                ft.Image(src="/icons/up.png")
                            ]
                        ),
                        on_click=lambda e: e.page.open(
                            ft.BottomSheet(
                                show_drag_handle=True,
                                bgcolor=ft.Colors.WHITE,
                                elevation=0.5,
                                content=Notif(page)
                            )
                        )
                    )
                ]
            )
        )
