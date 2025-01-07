import flet as ft
from rembg import remove
from PIL import Image
import io
import os

def main(page: ft.Page):
    page.title = 'Remover fondos'
    #Alinear al centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    input_path = None

    title = ft.Text('Remover fondos de imagenes', size=32, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text('Seleccionar imagenes', size=16, color=ft.colors.GREY_500)
    input_path_text = ft.Text('No se ha seleccionado ningún archivo', size=14, color=ft.colors.GREEN_400)
    select_btn = ft.ElevatedButton(
        'Seleccionar Imagen',
        icon=ft.icons.FILE_UPLOAD
    )

    page.add(
        ft.Column(
            controls=[
                title,
                subtitle,
                input_path_text,
                ft.Divider(height=20, color=ft.colors.BLUE),
                select_btn,
                input_path_text,
            ]
        )
    )

ft.app(target=main)