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

    def pick_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            input_path_text.value = e.files[0].path
            nonlocal input_path
            input_path = e.files[0].path

            #Ver la imagen previamente
            with open(input_path,'rb') as img_file:
                preview.src = input_path
                preview.visible = True
            page.update()
            process_btn.disabled = False
            page.update()
    
    def save_file_result(e: ft.FilePickerResultEvent):
        if not e.path or not input_path:
            return
        status.visible = True
        status.value = 'Procesando imagen...'
        page.update()

        try:
            input_img = Image.open(input_path)
            output_img = remove(input_img)
            if not e.path.endswith('.png'):
                e.path += '.png'
            output_img.save(e.path)
            status.value = 'Imagen guardada exitosamente'
            status.color = ft.Colors.GREEN

        except Exception as ex:
            status.value = f'Error: {str(ex)}'
            status.color = ft.Colors.RED
        
        page.update()
    
    pick_files_dialog = ft.FilePicker(
        on_result=pick_file_result
    )

    save_file_dialog = ft.FilePicker(
        on_result=save_file_result
    )

    page.overlay.extend([pick_files_dialog, save_file_dialog])

    title = ft.Text('Remover fondos de imagenes', size=32, weight=ft.FontWeight.BOLD)
    subtitle = ft.Text('Seleccionar imagenes', size=16, color=ft.Colors.GREY_500)
    input_path_text = ft.Text('No se ha seleccionado ningún archivo', size=14, color=ft.Colors.GREEN_400)
    
    select_btn = ft.ElevatedButton(
        'Seleccionar Imagen',
        icon=ft.Icons.FILE_UPLOAD,
        on_click=lambda _: pick_files_dialog.pick_files(
            file_type=ft.FilePickerFileType.IMAGE
        )
    )

    process_btn = ft.ElevatedButton(
        'Procesar y Guardar',
        icon=ft.Icons.SAVE,
        disabled=True,
        on_click=lambda _: save_file_dialog.save_file(
            file_type = ft.FilePickerFileType.ANY,
            allowed_extensions = ['png'],
            file_name = 'output.png'
        )
    )

    preview = ft.Image(
        width=300,
        height=300,
        fit=ft.ImageFit.CONTAIN,
        visible=False,
        border_radius=ft.border_radius.all(10)
    )

    status = ft.Text(
        visible=False,
        text_align=ft.TextAlign.CENTER,
    )

    page.add(
        ft.Column(
            controls=[
                title,
                subtitle,
                input_path_text,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                select_btn,
                input_path_text,
                ft.Divider(height=20, color=ft.Colors.BLUE),
                preview,
                ft.Divider(height=20, color=ft.Colors.BLUE),
                process_btn,
                status,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)