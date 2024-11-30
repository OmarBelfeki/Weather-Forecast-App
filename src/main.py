
from pages.home import Home
from pages.detail import Detail
from pages.map import Map

import flet as ft

import logging
logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page) -> None:
    page.title = "Weather Forcast"
    page.window.height = 756
    page.window.width = 360
    page.window.always_on_top = True

    page.fonts = {
        "overpass": "/fonts/Overpass-VariableFont_wght.ttf"
    }

    theme = ft.Theme()
    theme.page_transitions.we = ft.PageTransitionTheme.CUPERTINO
    page.theme = theme
    page.update()

    def router(_) -> None:
        page.views.clear()
        match page.route:
            case "/":
                page.views.append(ft.View(route="/", controls=[Home(page)], padding=0))
            case "/detail":
                page.views.append(ft.View(route="/detail", controls=[Detail(page)], padding=0))
            case "/map":
                page.views.append(ft.View(route="/map", controls=[Map(page)], padding=0))
        page.update()

    page.on_route_change = router
    page.go("/")

ft.app(target=main, assets_dir="assets")
