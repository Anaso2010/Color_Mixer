import flet as ft

def main(page: ft.Page):

    def update(e):
        r = int(red_slider.value)
        g = int(green_slider.value)
        b = int(blue_slider.value)

        hexValue = f"#{r:02x}{g:02x}{b:02x}"

        page.bgcolor = hexValue
        rgb_display.value = f"RBB: ({r}, {g}, {b})"
        hex_display.value = f"Hex: {hexValue}"
        page.update()

    red_slider = ft.Slider(min=0, max=255, value=0, label="Red")
    green_slider = ft.Slider(min=0, max=255, value=0, label="Green")
    blue_slider = ft.Slider(min=0, max=255, value=0, label="Blue")

    rgb_display = ft.Text(value="RGB: (0, 0, 0)", size=20)
    hex_display = ft.Text(value="Hex: #000000", size=20)

    page.add(red_slider, green_slider, blue_slider, rgb_display, hex_display)

    red_slider.on_change = update
    green_slider.on_change = update
    blue_slider.on_change = update

ft.app(main)